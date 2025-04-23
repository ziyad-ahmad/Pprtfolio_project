from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class Category(models.Model):
    """Categories for portfolio projects"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('projects:category', kwargs={'slug': self.slug})


class Project(models.Model):
    """Portfolio projects"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name='projects')
    tags = TaggableManager()
    
    # Dates
    date_created = models.DateField(auto_now_add=True)
    date_completed = models.DateField(blank=True, null=True)
    
    # Media
    featured_image = models.ImageField(upload_to='projects/')
    image1 = models.ImageField(upload_to='projects/', blank=True)
    image2 = models.ImageField(upload_to='projects/', blank=True)
    image3 = models.ImageField(upload_to='projects/', blank=True)
    
    # Links
    live_url = models.URLField(blank=True)
    source_code_url = models.URLField(blank=True)
    
    # Settings
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date_completed', '-date_created']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={'slug': self.slug})


class Technology(models.Model):
    """Technologies used in projects"""
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True, 
                           help_text="Icon class (from included icon set)")
    projects = models.ManyToManyField(Project, related_name='technologies')
    
    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ['name']
    
    def __str__(self):
        return self.name