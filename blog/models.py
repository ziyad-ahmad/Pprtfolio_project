from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class Category(models.Model):
    """Blog post categories"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})


class Post(models.Model):
    """Blog posts"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    subtitle = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog/')
    categories = models.ManyToManyField(Category, related_name='posts')
    tags = TaggableManager()
    
    # Publication details
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    # SEO
    meta_description = models.TextField(blank=True, 
                                       help_text="SEO meta description")
    
    class Meta:
        ordering = ['-published_date', '-created_date']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})