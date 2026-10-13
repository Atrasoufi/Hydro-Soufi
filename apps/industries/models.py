from django.db import models

# from apps.media.models import Media
# from apps.products.models import Product


class Industry(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(
        "products.Product",
        related_name="industries",
        blank=True,
    )

    short_description = models.TextField(blank=True)

    icon = models.CharField(max_length=255, blank=True)
    cover_image = models.ForeignKey(
        "media.Media",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="cover_for_industry",
    )
    is_active = models.BooleanField(default=True)



