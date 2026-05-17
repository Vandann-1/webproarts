from django.db import models

# Create your models here.

from django.db import models

class ContactMessage(models.Model):
    fullname = models.CharField(max_length=100)

    email = models.EmailField()
    subject = models.CharField(max_length=50) # web-dev, marketing, etc.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True) # webproarts.com/blog/your-post-title
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='blog_thumbs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug =(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class googlereview(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating} Stars"    