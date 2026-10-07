from django.db import models
from django.contrib.auth import get_user_model
from django_jalali.db import models as jmodels

# Create your models here.

User = get_user_model()

class EducationCategory:
    products = models.ManyToManyField(
        "products.Product",
        related_name="educations"
    )

    industries = models.ManyToManyField(
        "industries.Industry",
        related_name="educations"
    )

    services = models.ManyToManyField(
        "services.Service",
        related_name="educations"
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children"
    )

    name = models.CharField(max_length=255)

    slug = models.SlugField(
        max_length=255,
        unique=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    sort_order = models.IntegerField(default=0)


class EducationContent:
    category = models.ForeignKey(
        'EducationCategory',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='contents'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="education_contents"
    )

    title = models.CharField(max_length=255)

    slug = models.SlugField(
        max_length=255,
        unique=True
    )

    expert = models.TextField(
        null=True,
        blank=True
    )

    content = models.TextField(
        null=True,
        blank=True
    )

    CONTENT_TYPES = [
        ("ARTICLE", "Article"),
        ("VIDEO", "Video"),
        ("GUIDE", "Guide"),
        ("TECHNICAL", "Technical"),
    ]

    content_type = models.CharField(
        max_length=30,
        choices=CONTENT_TYPES,
        default='ARTICLE'
    )

    featured_media = models.ForeignKey(
        'media.Media',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='featured_contents'
    )

    STATUS = [
        ("DRAFT", "Drart"),
        ("PUBLISHED", "Published"),
        ("ARCHIVED", "Archived"),
    ]

    status = models.CharField(
        max_length=30,
        choices=STATUS,
        default='DRAFT'
    )

    published_at = jmodels.jDateTimeField(
        null=True,
        blank=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    created_at = jmodels.jDateTimeField(
        auto_now_add=True
    )

    updated_at = jmodels.jDateTimeField(
        auto_now=True
    )

class EducationMedia(models.Model):
    education = models.ForeignKey(
        "EducationContent",
        on_delete=models.CASCADE,
        related_name="media"

    )

    media = models.ForeignKey(
        "media.Media",
        on_delete=models.CASCADE,
        related_name="education_media"
    )

    media_type = models.CharField(max_length=30)

    sort_order = models.IntegerField(default=0)

    is_primary = models.BooleanField(default=False)

    caption = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["education", "media"],
                name="unique_education_media"
            )
        ]