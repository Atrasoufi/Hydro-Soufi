from django.db import models

# Create your models here.

class EducationCategory:
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

    is_aactive = models.BooleanField(default=True)

    sort_order = models.IntegerField(default=0)

    