from .models import SiteSettings

def site_settings(request):
    """Adds site settings to the template context"""
    try:
        settings = SiteSettings.objects.first()
        if not settings:
            # Return empty dict if no settings exist yet
            return {}
        return {'site_settings': settings}
    except:
        # Return empty dict if DB table doesn't exist yet (e.g. during migrations)
        return {}