from django.contrib import admin
from .models import SiteSettings, Skills, ContactMessage


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'email', 'bio_short', 'bio_long', 'profile_image')
        }),
        ('Social Links', {
            'fields': ('github', 'linkedin', 'twitter', 'resume')
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords')
        }),
        ('Theme', {
            'fields': ('enable_dark_mode', 'primary_color', 'accent_color')
        }),
    )


@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    
    def has_add_permission(self, request):
        return False
    
    def save_model(self, request, obj, form, change):
        if 'is_read' in form.changed_data:
            super().save_model(request, obj, form, change)