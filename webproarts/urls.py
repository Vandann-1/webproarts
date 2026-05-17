from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from webproarts.sitemap import*
from django.views.generic import TemplateView
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {
    'static': StaticSitemap,
    'blog': BlogSitemap, 
}

urlpatterns = [
    path('admin/', admin.site.urls),




    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt",
        content_type="text/plain",
        extra_context={"site_url": "https://webproarts.in"}
    )),

    path('sitemap-new.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('', include('web.urls')),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])