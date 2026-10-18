from django.db import models
from django.contrib.auth import get_user_model
from django_jalali.db import models as jmodels
from django.core.exceptions import ValidationError

# Create your models here.

User = get_user_model()


class EducationCategory(models.Model):

    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )

    name = models.CharField(max_length=255)

    description = models.TextField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class EducationContent(models.Model):

    products = models.ManyToManyField("products.Product", related_name="educations")

    industries = models.ManyToManyField(
        "industries.Industry", related_name="educations"
    )

    services = models.ManyToManyField("services.Service", related_name="educations")

    category = models.ForeignKey(
        "EducationCategory",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="contents",
    )

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="education_contents"
    )

    title = models.CharField(max_length=255)

    slug = models.SlugField(max_length=255, unique=True)

    excerpt = models.TextField(null=True, blank=True)

    content = models.TextField(null=True, blank=True)

    CONTENT_TYPES = [
        ("ARTICLE", "Article"),
        ("VIDEO", "Video"),
        ("GUIDE", "Guide"),
        ("TECHNICAL", "Technical"),
    ]

    content_type = models.CharField(
        max_length=30, choices=CONTENT_TYPES, default="ARTICLE"
    )

    featured_media = models.ForeignKey(
        "media.Media",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="featured_contents",
    )

    STATUS = [
        ("DRAFT", "Draft"),
        ("PUBLISHED", "Published"),
        ("ARCHIVED", "Archived"),
    ]

    status = models.CharField(max_length=30, choices=STATUS, default="DRAFT")

    is_featured = models.BooleanField(default=False)

    created_at = jmodels.jDateTimeField(auto_now_add=True)

    updated_at = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class EducationMedia(models.Model):
    education = models.ForeignKey(
        "EducationContent", on_delete=models.CASCADE, related_name="media"
    )

    media = models.ForeignKey(
        "media.Media", on_delete=models.CASCADE, related_name="education_media"
    )

    is_primary = models.BooleanField(default=False)

    caption = models.CharField(max_length=500, null=True, blank=True)

    def clean(self):
        # Only image-based media may be attached to educational media records.
        super().clean()

        if self.media_id and self.media.media_type != "image":
            raise ValidationError({
                "media": "Only image media can be assigned to education content."
            })

    def __str__(self):
        return f"{self.education.title} - {self.media.file_name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["education", "media"], name="unique_education_media"
            )
        ]

# Stores video attachments for education content, including the optional primary video.
class EducationVideo(models.Model):
    education = models.ForeignKey(
        "EducationContent",
        on_delete=models.CASCADE,
        related_name="videos",
    )

    media = models.ForeignKey(
        "media.Media",
        on_delete=models.CASCADE,
        related_name="education_videos",
    )

    is_primary = models.BooleanField(default=False)

    caption = models.CharField(
        max_length=500,
        blank=True,
    )

    def clean(self):
        super().clean()

        if self.media_id and self.media.media_type != "video":
            raise ValidationError({
                "media": "Only video media can be assigned to education content."
            })

    def __str__(self):
        return f"{self.education.title} - {self.media.file_name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["education", "media"],
                name="unique_education_video",
            ),
            models.UniqueConstraint(
                fields=["education"],
                condition=models.Q(is_primary=True),
                name="unique_primary_education_video",
            ),
        ]