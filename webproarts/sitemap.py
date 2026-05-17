from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from web.models import * # Ensure this matches your model name!

class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return [
            'home', 
            'about', 
            'contact.html', 
            'digital_marketing', 
            'web_design', 
            'video_editing',
            'social_media', 
            'graphic_design',
            'privacy_policy', 
            'terms_of_service', 
            'webdev',
            'blogs',
            'bot_pages',
            'career',
            'portfolio',
            
        ]

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        # Using .all() to get all blog posts
        return BlogPost.objects.all()

    def location(self, obj):
        # This maps to path('blogs/<int:post_id>/', ...)
        return reverse('blog_detail', args=[obj.id])