from django.db import models
from django_jalali.db import models as jmodels
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

    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField(auto_now=True)
    

class AboutSection(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    
    short_description = models.TextField()
    content = models.TextField()
    
    image_media = models.ForeignKey(
        Media,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="about_sections",
    )
    
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField(auto_now=True)