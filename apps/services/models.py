from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)

    short_description = models.TextField(blank=True)

    icon = models.CharField(max_length=255, blank=True)
    cover_image = models.ForeignKey(
        "media.Media",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="cover_for_service",
    )

    products = models.ManyToManyField(
    "products.Product",
    related_name="services",
    blank=True,
    )

    industries = models.ManyToManyField(
        "industries.Industry",
        related_name="services",
        blank=True,
    )

    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


