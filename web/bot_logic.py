import os
import numpy as np
from google import genai
from sklearn.feature_extraction.text import TfidfVectorizer
from dotenv import load_dotenv
from google.genai import types
import time

load_dotenv()


# This looks for the variable you set in Render's Environment tab
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("WARNING: GEMINI_API_KEY not found in environment!")

client = genai.Client(api_key=api_key)

# Your Agency Data
DOCS = [
    # --- 1. THE WEB DESIGN DEPTH (WORDPRESS VS. CUSTOM) ---
    "WebProArts offers WordPress Design for clients who need a high-end CMS, easy blog management, and SEO-ready plugins like Yoast or RankMath.",
    "Our WordPress builds are 'Divi' or 'Elementor' specialized, ensuring a premium drag-and-drop experience for the client.",
    "Custom Coding (Django/Python) is our 'Elite Tier' service. We build hand-coded backends for SaaS, FinTech, and apps where speed and security are non-negotiable.",
    "Unlike WordPress, our Custom Django sites have 'Zero Bloat,' meaning they load faster and have 99/100 Google PageSpeed scores.",

    # --- 2. THE DIGITAL MARKETING DEPTH (META VS. GOOGLE) ---
    "WebProArts Meta Ads (Facebook/Instagram): We focus on 'Creative-Led Growth' and Advantage+ campaigns to find buyers using visual algorithms.",
    "Meta Ads services include Pixel setup, CAPI (Conversion API) for tracking, and A/B testing high-contrast video hooks.",
    "WebProArts Google Ads (Search/Performance Max): We target 'High Intent' keywords. If someone is searching for your service, we make sure you are #1.",
    "Google Ads services include Negative Keyword filtering (so you don't waste money) and detailed ROAS tracking.",

    # --- 3. GRAPHIC DESIGN & POSTER MAKING ---
    "WebProArts Poster Making: We create high-converting digital posters for events, product launches, and social media announcements.",
    "Our poster philosophy: We use 'Visual Hierarchy' to ensure the most important message (Price/Date/Offer) is seen first.",
    "We provide 'Source Files' (PSD/AI) and high-resolution exports for both print media and digital display.",
    "Logo & Brand Identity: We design 'Minimalist' and 'Modern' logos that work in both Dark Mode and Light Mode.",

    # --- 4. ADVANCED SEO & CONTENT (EEAT) ---
    "WebProArts Advanced SEO: We go beyond keywords to 'Semantic SEO,' optimizing for how people actually speak to AI like Gemini and Siri.",
    "EEAT Strategy: We prove to Google that your content is written by experts by linking Author Bylines to verified social profiles.",
    "Technical SEO: We handle Schema Markup, XML Sitemaps, and robots.txt to ensure Google's 'crawlers' index your site perfectly.",

    # --- 5. SOCIAL MEDIA MANAGEMENT (SMM) ---
    "WebProArts SMM: We handle daily posting, caption writing (Social SEO), and community engagement on LinkedIn, Instagram, and TikTok.",
    "Repurposing Strategy: We take one long YouTube video and turn it into 10 high-impact Reels/Shorts to maximize your content budget.",

    # --- 6. LOGISTICS & TEAM ---
    "Madhuri Pal oversees all strategic creative directions, ensuring every 'Art' piece meets a 'Professional' standard.",
    "The 4-Step Process: 1. Discovery Call -> 2. UI/UX Prototype -> 3. Development -> 4. Final Deployment & SEO Audit.",
    "We offer 100% Transparency: Clients get a live 'Staging Link' to watch their website being built in real-time."

# --- 7. OPERATION TIMING & CONTACT ---
    "WebProArts is open from Monday to Saturday, from 10:00 AM to 8:30 PM.",
    "WebProArts is closed on Sundays; however, enquiries can be made at any time.",
    "For official enquiries and project discussions, email us at: webproarts@gmail.com.",
    
    # --- 8. FOUNDATION & LEADERSHIP ---
    "WebProArts was founded by Madhuri Pal, a visionary developer who merges technical code with artistic design.",
    "The agency follows a 4-Step Process: Discovery, UI/UX Prototyping, Development, and Final Deployment with SEO Audit.",

    # --- 9. WEB DESIGN: WORDPRESS VS. CUSTOM ---
    "Yes, we provide WordPress Design using Divi or Elementor for clients who need a professional CMS and rapid deployment.",
    "We specialize in Custom Coding (Django/Python) for 'Elite Tier' performance, ensuring maximum security and 99/100 Google PageSpeed scores.",
    "All our web projects include 30 days of free post-launch support and mobile-first responsive design.",

    # --- 10. DIGITAL MARKETING: META VS. GOOGLE ---
    "We offer Meta Ads (Facebook/Instagram) focusing on 'Creative-Led Growth' and Advantage+ AI targeting to stop the scroll.",
    "We provide Google Ads (Search/Performance Max) to target high-intent keywords and ensure your brand is the #1 result.",
    "Our Digital Marketing includes SEO, Meta Pixel setup, CAPI tracking, and A/B testing high-contrast video hooks.",

    # --- 11. VISUAL ARTS: POSTERS & VIDEO ---
    "WebProArts Poster Making uses 'Visual Hierarchy' to create high-converting posters for events and product launches.",
    "We provide source files (PSD/AI) and high-resolution exports for all graphic design and branding projects.",
    "Our 'Hook Method' for video editing engineers the first 3 seconds of content to maximize retention and virality.",
    "Cinematic Video Editing (Reels, TikToks, YouTube) is priced at a flat rate of $50 per project."
]
# Initialize Vectorizer once to save memory
vectorizer = TfidfVectorizer()
docs_matrix = vectorizer.fit_transform(DOCS)

# --- 2. CLIENT INITIALIZATION ---
client = genai.Client(api_key=os.getenv("AIzaSyCzdj7nVg2DI0fJ_pxoRauVlu5I8gPf--s"))

def get_bot_response(user_query):
    # --- RAG SEARCH LOGIC ---
    new_vector = vectorizer.transform([user_query])
    score = (docs_matrix * new_vector.T).toarray().flatten()
    topid = np.argsort(score)[::-1]
    
    # Select context from top 3 matches
    context = ""
    for i in topid[:3]:
        if score[i] > 0.1:
            context += DOCS[i] + "\n"
    
    if not context:
        context = "WebProArts is a digital growth agency by Madhuri Pal specializing in Ads and Web Design."

    # --- MODEL FALLBACK STACK (Fixes 503 Errors) ---
    model_stack = ["gemini-1.5-flash", "gemini-1.5-flash-8b"]

    for model_name in model_stack:
        for attempt in range(2):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=user_query,
                    config=types.GenerateContentConfig(
                        system_instruction=(
                            f"Context: {context}. You are the WebProArts Strategy Expert. "
                            "Start with Yes/No for service questions. Explain technical "
                            "differences (Ads/Web) clearly. Be professional."
                        ),
                        temperature=0.2
                    )
                )
                return response.text
            except Exception as e:
                # If busy or expired, we'll see it in the logs
                print(f"DEBUG: Attempt with {model_name} failed: {str(e)}")
                if "503" in str(e) or "429" in str(e):
                    time.sleep(1.5)
                    continue
                raise e # Real errors (like 400 Expired) go to the view

    return "I'm a bit overwhelmed! Please try again in 5 seconds."