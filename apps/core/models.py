from django.db import models

from apps.media.models import Media

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=255, blank=True)
    site_description = models.TextField(blank=True)
    
    logo_media = models.ForeignKey(
        Media,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="logo_for_sites",
    )
    
    favicon_media = models.ForeignKey(
        Media,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="favicon_for_sites",
    )
    
    phone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    
    address = models.TextField()
    
    instagram_url = models.URLField(max_length=500, blank=True)
    linkedin_url = models.URLField(max_length=500, blank=True)
    telegram_url = models.URLField(max_length=500, blank=True)
    whatsapp_url = models.URLField(max_length=500, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    