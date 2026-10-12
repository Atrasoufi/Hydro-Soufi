from django.db import models

# from apps.media.models import Media
# from apps.products.models import Product


class Industry(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(
        "products.Product",
        through="IndustryProduct",
        related_name="industries",
    )
    slug = models.SlugField(max_length=255, unique=True)

    short_description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)

    icon = models.CharField(max_length=255, blank=True)
    cover_image = models.ForeignKey(
        "media.Media",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="cover_for_industry",
    )
    is_active = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)


class IndustryProduct(models.Model):
    industry = models.ForeignKey(
        Industry,
        on_delete=models.CASCADE,
        related_name="industry_products",
    )

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="industry_products",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["industry", "product"],
                name="unique_industry_product",
            )
        ]
