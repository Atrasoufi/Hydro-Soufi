# Create your models here.
from django.conf import settings
from django.db import models


class Media(models.Model):
    # Stores uploaded media metadata used by the app for images and videos.

    class MediaType(models.TextChoices):
        IMAGE = "image" , "Image"
        VIDEO = "video" , "Video"

    class VideoSource(models.TextChoices):
        CDN = "cdn" , "Cdn"
        APARAT = "aparat" , "Aparat"

    media_type = models.CharField(max_length=10,choices=MediaType)
    video_source =  models.CharField(
        max_length=10,
        choices=VideoSource,
        blank=True
    )

    file_name = models.CharField(max_length=255)
    file_url = models.URLField(max_length=1000)

    file_type = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    alt_text = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField()

    class Meta:
        db_table = "media"

    def __str__(self):
        return self.file_name
