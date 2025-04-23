from django.db import models

class SiteSettings(models.Model):
    """Site-wide settings and personal information"""
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, help_text="Professional title")
    email = models.EmailField()
    bio_short = models.TextField(help_text="Short biography for homepage")
    bio_long = models.TextField(help_text="Detailed biography for about page")
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    resume = models.FileField(upload_to='resume/', blank=True)
    profile_image = models.ImageField(upload_to='profile/')
    
    # SEO and metadata
    meta_description = models.TextField(help_text="SEO meta description", blank=True)
    meta_keywords = models.CharField(max_length=255, help_text="SEO keywords", blank=True)
    
    # Theme settings
    enable_dark_mode = models.BooleanField(default=True)
    primary_color = models.CharField(max_length=7, default="#1E3A8A", 
                                    help_text="Primary color in hex format")
    accent_color = models.CharField(max_length=7, default="#0D9488",
                                   help_text="Accent color in hex format")
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return f"{self.name}'s Portfolio Settings"
    
    def save(self, *args, **kwargs):
        # Ensure there's only one instance
        if not self.pk and SiteSettings.objects.exists():
            return  # Don't save if an instance already exists
        return super().save(*args, **kwargs)


class Skills(models.Model):
    """Technical skills to display on portfolio"""
    CATEGORY_CHOICES = [
        ('FRONT', 'Frontend'),
        ('BACK', 'Backend'),
        ('DB', 'Database'),
        ('DEVOPS', 'DevOps'),
        ('DESIGN', 'Design'),
        ('OTHER', 'Other'),
    ]
    
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(help_text="Skill level from 1-100")
    icon = models.CharField(max_length=50, blank=True, 
                           help_text="Icon class (from included icon set)")
    
    class Meta:
        ordering = ['-proficiency', 'category', 'name']
    
    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    """Messages from the contact form"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Message from {self.name}: {self.subject}"