from django.db import models
from django.contrib.auth import get_user_model
from django_jalali.db import models as jmodels

# Create your models here.


class ProductCategories(models.Model):
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=200)
    description = models.TextField()

    # image_media_id = relation to media

    is_active = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)


class Products(models.Model):
    category = models.ForeignKey(
        ProductCategories, on_delete=models.PROTECT, related_name="products"
    )

    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=200)

    short_description = models.TextField()
    full_description = models.TextField()
    technical_description = models.TextField()

    product_code = models.CharField(100, unique=True)

    manufacturing_type = models.CharField(max_length=50)

    is_custom = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField()


class ProductSpec(models.Model):
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name="specs",
    )

    specification_name = models.CharField(max_length=255)

    specification_value = models.CharField(max_length=500)

    unit = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    sort_order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.specification_name}: {self.specification_value}"


class ProductImages(models.Model):
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="images"
    )

    media = models.ForeignKey(
        "media.Media", on_delete=models.PROTECT, related_name="product_images"
    )

    alt_text = models.CharField(max_length=50)

    is_primary = models.BooleanField(default=False)
    sorted_order = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["product"],
                condition=models.Q(is_primary=True),
                name="unique_primary_image_per_product",
            ),
            models.UniqueConstraint(
                fields=["product", "media"],
                name="unique_user_product",
            ),
        ]
