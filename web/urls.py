from django.contrib import admin
from django.urls import path
from web.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("about/", about, name="about"),
    
    # Keeping contact.html without a slash to match your current link
    path("contact.html", contact, name="contact.html"), 
    path("contact-submit/", contact_submit, name="contact_form"), 
    
    path("digital-marketing/", digital_marketing, name="digital_marketing"),
    path("web-design/", web_design, name="web_design"),
    path("video-editing/", video_Editing, name="video_editing"),
    path("social-media/", social_media, name="social_media"),
    path("graphic-design/", garphic_design, name="graphic_design"),
    path("privacy-policy/", policy, name="privacy_policy"),
    path("terms-of-service/", policy, name="terms_of_service"),
    path("portfolio/", webdev, name='portfolio'),
    path("career/", career, name="career"),
    
    path('blogs/', blogs, name='blogs'), 
    path('blogs/<int:post_id>/', blog_detail, name='blog_detail'),
    path('chat-bot/', chat_api, name='chat_bot'),
    path('support/chat-bot/', bot_page, name='bot_pages'),
]