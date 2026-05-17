from django.shortcuts import render

from django.db import models
from django.utils.text import slugify
from django.shortcuts import render, get_object_or_404
from .models import ContactMessage, BlogPost
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):

    return render(request, 'contact.html')


import json
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def contact_submit(request):
    if request.method == "POST":
        try:
            # Check if body is empty
            if not request.body:
                return JsonResponse({'status': 'error', 'message': 'Empty request body'}, status=400)

            data = json.loads(request.body)
            
            # Use .get() with defaults to avoid KeyErrors
            full_name = data.get('full_name', 'No Name')
            user_email = data.get('email', 'No Email')
            service = data.get('service', 'General Inquiry')
            message = data.get('message', '')

            # SMTP Sending Logic
            send_mail(
                subject=f"Contact Form: {service}",
                message=f"From: {full_name}\nEmail: {user_email}\n\nMessage:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            return JsonResponse({'status': 'success'})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)
        except Exception as e:
            # This prints the REAL error (like Gmail auth) to your terminal
            print(f"CRITICAL ERROR: {str(e)}") 
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Only POST allowed'}, status=405)



def digital_marketing(request):
    return render(request, 'digital-marketing.html')

def web_design(request):
    return render(request, 'web-design.html')

def video_Editing(request):
    return render(request, 'video-editing.html')

def social_media(request):
    return render(request, 'social-media.html')

def garphic_design(request):
    return render(request, 'garphic.html')

def policy(request):
    return render(request, 'policy.html')

def term(request):
    return render(request, 'term.html')


def webdev(request):
    return render(request, 'webdev.html')




from django.shortcuts import render, Http404

POSTS_DATA = {
    '1': {
        'id': 1,
        'title': 'The Hook Method: Viral Video Secrets',
        'category': 'Production',
        'image': 'https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?q=80&w=800',
        'excerpt': 'Learn how we engineer the first 3 seconds of social content to stop the scroll...',
        'content': """
            <p>To win on social media today, the first 3 seconds are everything. At Web Pro Arts, we don't just call it an opening; we call it <strong>"The Hook."</strong> In an era of infinite scroll and diminishing attention spans, the hook is the difference between a viral brand and a digital ghost.</p>
            <h3>The Anatomy of the 3-Second Rule</h3>
            <p>The human brain processes visual information 60,000 times faster than text. When a user is scrolling, their thumb moves at a constant rhythm. To break that rhythm, we must trigger a "Pattern Interrupt." This forces the brain to switch from passive consumption to active observation.</p>
            <ul>
                <li><strong>Visual Velocity:</strong> Rapid scene transitions in the first 1.5 seconds.</li>
                <li><strong>High-Contrast Overlays:</strong> Bold typography that tells the viewer exactly what they are going to learn.</li>
                <li><strong>The Curiosity Gap:</strong> Starting with a statement that can only be answered by watching further.</li>
            </ul>
            <h3>Why High-Contrast Text Overlays Matter</h3>
            <p>Over 80% of social media users consume video with the sound muted. This statistic alone dictates that your visual storytelling must be self-sufficient. We utilize high-contrast overlays—typically using our signature Cyan (#28b8d9) and Navy (#16598a) palette—to ensure readability against any background.</p>
            <h3>The Science of Rapid Scene Transitions</h3>
            <p>Static shots are the death of retention. In our editing suite, we follow the "2-Second Cut" rule. Every two seconds, something on the screen must change. This constant stream of new visual stimuli prevents the brain from entering a "boredom state." For performance marketing, this translates directly into higher View-Through Rates (VTR).</p>
            <p><strong>Summary:</strong> Your video's hook is your brand's digital first impression. Win the first 3 seconds, and you win the customer.</p>
        """
    },
    '2': {
        'id': 2,
        'title': 'Psychology of Color in SaaS Branding',
        'category': 'Branding',
        'image': 'https://i.pinimg.com/originals/bd/80/92/bd8092c59bcf3ae83117e910afbe12dc.jpg',
        'excerpt': 'Why top tech companies use high-contrast blue and aqua tones for trust...',
        'content': """
            <p>Colors aren't just aesthetic; they are emotional triggers that speak directly to the subconscious. In SaaS, where a user decides to stay or bounce in seconds, color is your most powerful tool. At <strong>Web Pro Arts</strong>, our foundation in Blue and Aqua is a calculated strategic move designed to project stability and innovation.</p>
            <h3>The Science of Visual Trust</h3>
            <p>Because users "rent" software, they need to feel it is secure. Blue has historically been the choice for tech giants like IBM and Intel because it lowers the heart rate and creates a sense of professional calm.</p>
            <h3>The "Action Color" Strategy</h3>
            <p>One of the biggest mistakes is using brand colors for everything. If your website is blue and your "Sign Up" button is also blue, it becomes invisible. We advocate for the <strong>Isolation Effect</strong>. By using a high-contrast accent—like our bright Cyan—against a dark Navy background, we create a visual "shout."</p>
            <h3>The Dark Mode Revolution</h3>
            <p>In 2026, Dark Mode is a requirement. When designing for dark mode, bright colors like Aqua become luminous, creating a futuristic aesthetic that resonates with tech-savvy founders.</p>
            <p><strong>Summary:</strong> People don't just buy what your software does; they buy how it makes them <em>feel</em>. Use color to make them feel powerful and secure.</p>
        """
    },
    '3': {
        'id': 3,
        'title': 'Mastering Meta Ads in the AI Era',
        'category': 'Performance',
        'image': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800',
        'excerpt': 'How Advantage+ campaigns are changing the way agencies manage budgets...',
        'content': """
            <p>The landscape of performance marketing has shifted. We are no longer in the era of manual "Interest Targeting." In 2026, the algorithm is the smartest person in the room. At <strong>Web Pro Arts</strong>, we’ve moved away from micro-managing audiences and toward <strong>Creative-Led Growth</strong>.</p>

            <h3>The Death of Interest Targeting</h3>
            <p>For years, media buyers spent hours selecting interests like "Entrepreneurs" or "Luxury Travel." Today, Meta’s AI—specifically the <strong>Advantage+</strong> suite—can identify your perfect customer better than any human. By using Broad Targeting, we allow the AI to analyze millions of data points to find the person most likely to convert.</p>

            <h3>The New Role of Creative Assets</h3>
            <p>If the AI handles the targeting, what does the agency do? We handle the <strong>Creative Strategy</strong>. In the modern era, your <em>ad creative is your targeting</em>. If we show a video about "High-Performance Servers," the AI will observe who watches that video and automatically find more people like them. The visual asset tells the machine who the customer is.</p>

            <h3>The Advantage+ Shopping Loop</h3>
            <p>For our e-commerce clients, we utilize <strong>Advantage+ Shopping Campaigns (ASC)</strong>. This automated system combines prospecting and re-targeting into a single campaign. It continuously tests different combinations of hooks, headlines, and descriptions to find the winning "Winner" ad that scales your ROAS (Return on Ad Spend).</p>

            <h3>Data-Driven Iteration</h3>
            <p>Success in paid media is no longer about "Setting and Forgetting." It is about a constant loop of <strong>Test -> Analyze -> Pivot</strong>. We look at metrics like:</p>
            <ul>
                <li><strong>Thumb-Stop Ratio:</strong> How many people watched the first 3 seconds?</li>
                <li><strong>Hold Rate:</strong> How many people stayed until the middle?</li>
                <li><strong>Conversion Rate (CVR):</strong> How many people actually clicked the "Buy" button?</li>
            </ul>

            <h3>Summary: Feed the Machine</h3>
            <p>To win with Meta Ads in 2026, you must stop fighting the AI and start feeding it. By providing the algorithm with high-quality video hooks and strategic brand messaging, Web Pro Arts ensures your budget is never wasted on the wrong audience.</p>
            <p><strong>Remember:</strong> Don't try to outsmart the machine; out-create your competition.</p>
        """},
'4': {
        'id': 4,
        'title': 'The Rise of Intelligent Micro-Interactions',
        'category': 'Development',
        'image': 'https://blog.gorrion.pl/staging/wp-content/uploads/2020/11/What-are-micro-interactions-and-how-do-they-influence-digital-products_.png',
        'excerpt': 'Using Machine Learning to create hyper-responsive user experiences...',
        'content': """
            <p>The difference between a "good" site and a "pro" site is in the details. At <strong>Web Pro Arts</strong>, we are implementing <strong>Intelligent Micro-Interactions</strong>—small animations and feedbacks powered by lightweight, on-device AI.</p>
            <h3>Predictive Hover States</h3>
            <p>By using low-latency ML models, your website can predict which button a user is about to click based on cursor velocity. We pre-fetch that data instantly, making the site feel like it’s "reading the user's mind."</p>
            <h3>Voice-Enabled Navigation</h3>
            <p>Standard search bars are becoming obsolete. We build custom natural language processing (NLP) modules directly into your site’s header, allowing users to navigate complex menus using only their voice. It’s hands-free, high-tech, and highly efficient.</p>
            <p><strong>Summary:</strong> A website should react to a user, not just wait for them. Intelligence is the new interactivity.</p>
        """
    },
    '5': {
        'id': 5,
        'title': 'The EEAT Factor: Humanizing Digital Content',
        'category': 'SEO Strategy',
        'image': 'https://api.backlinko.com/app/uploads/2025/07/what-is-e-e-a-t-1440x998.png',
        'excerpt': 'How to prove to Google that a human, not a bot, wrote your high-ranking content...',
        'content': """
            <p>As AI-generated content floods the web, Google has doubled down on <strong>EEAT</strong> (Experience, Expertise, Authoritativeness, and Trust). If your content feels robotic, it will vanish. At <strong>Web Pro Arts</strong>, we humanize your SEO through <strong>"First-Person Narrative"</strong> strategies.</p>
            <h3>The Experience Advantage</h3>
            <p>AI can aggregate facts, but it cannot share experiences. We weave real-world client results and "behind-the-scenes" insights into every article. This "Experience" signal tells Google that a real expert is behind the keyboard, boosting your credibility scores significantly.</p>
            <h3>Author Byline Optimization</h3>
            <p>We don't just post blogs; we build personas. By optimizing author schemas and linking to verified LinkedIn profiles, we create a digital paper trail of expertise. This turns your blog from a collection of articles into a recognized industry publication.</p>
            <p><strong>Summary:</strong> In the age of AI, your humanity is your greatest SEO competitive advantage.</p>
        """
    },
    '6': {
        'id': 6,
        'title': 'Voice Search & Semantic SEO Mastery',
        'category': 'SEO Strategy',
        'image': 'https://www.esols.net/wp-content/uploads/2024/02/Voice-Searc.png',
        'excerpt': 'Optimizing for how people actually talk to their devices in a mobile-first world...',
        'content': """
            <p>By 2026, over 60% of searches are conducted via voice. People don't type "best SEO agency Mumbai"; they ask, "Who is the best agency for web design near me?" This shift requires a move toward <strong>Semantic SEO</strong> and conversational syntax.</p>
            <h3>The Long-Tail Question Strategy</h3>
            <p>At <strong>Web Pro Arts</strong>, we structure content around the <strong>"Natural Language Processing" (NLP)</strong> patterns used by Siri, Alexa, and Gemini. By targeting specific "How-To" and "Why" questions, we capture the top-of-funnel traffic that traditional keyword research misses.</p>
            <h3>Local SEO & Mobile Dominance</h3>
            <p>Voice search is inherently local. We optimize your "Google Business Profile" and local landing pages with high-contrast, mobile-responsive layouts to ensure that when someone asks for a service, your brand is the first name spoken back. Speed, local relevance, and clear answers are the pillars of voice dominance.</p>
            <p><strong>Summary:</strong> Speak your customer's language, and the search engine will listen.</p>
        """
    }
}
        


from django.http import JsonResponse
from .bot_logic import get_bot_response

# views.py


import traceback
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .bot_logic import get_bot_response

from django.http import JsonResponse
from django.http import JsonResponse
from .bot_logic import get_bot_response
import traceback

def chat_api(request):
    if request.method == "POST":
        user_message = request.POST.get('message', '').strip()
        
        if not user_message:
            return JsonResponse({'reply': "Please type a message!"})

        try:
            # Call our bot logic
            reply = get_bot_response(user_message)
            return JsonResponse({'reply': reply})
            
        except Exception as e:
            # Check for the 'Expired' error specifically
            error_msg = str(e)
            print(f"CRITICAL ERROR: {error_msg}")
            
            if "expired" in error_msg.lower() or "400" in error_msg:
                friendly_reply = "System Maintenance: The API key has expired. Please update it in Render."
            else:
                friendly_reply = "I'm having trouble connecting. Please try again later!"
                
            return JsonResponse({'reply': friendly_reply}, status=200)

    return JsonResponse({'reply': "Method not allowed"}, status=405)


def blog_detail(request, post_id):
    post = POSTS_DATA.get(str(post_id))
    if not post:
        raise Http404("Post not found")
    return render(request, 'blog_detail.html', {'post': post})

def blogs(request):
    return render(request, 'blog.html', {'posts': POSTS_DATA})

def blog_detail(request, post_id):
    # Retrieve the specific post using the ID from the URL
    post = POSTS_DATA.get(str(post_id))
    if not post:
        raise Http404("Post not found")
    return render(request, 'blog_detail.html', {'post': post})

def bot_page(request):
    return render(request, 'bot_page.html')


def career(req):
    return render(req, 'career.html')