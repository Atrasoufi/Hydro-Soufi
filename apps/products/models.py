from django.db import models
from django.contrib.auth import get_user_model
from django_jalali.db import models as jmodels
from django.core.exceptions import ValidationError

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
    description = models.TextField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategories, on_delete=models.PROTECT, related_name="products"
    )

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200)

    short_description = models.TextField()
    full_description = models.TextField()

    industry_product = models.ForeignKey(
        "industries.Industry",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="direct_products",
    )

    is_custom = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField()

    def __str__(self):
        return self.name


class ProductSpec(models.Model):
    product = models.ForeignKey(
        Product,
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

    def __str__(self):
        return f"{self.specification_name}: {self.specification_value}"


class ProductImages(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )

    media = models.ForeignKey(
        "media.Media", on_delete=models.PROTECT, related_name="product_images"
    )

    is_primary = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["product"],
                condition=models.Q(is_primary=True),
                name="unique_primary_image_per_product",
            ),
            models.UniqueConstraint(
                fields=["product", "media"],
                name="unique_product_image",
            ),
        ]

    def clean(self):
        super().clean()

        if self.media_id and self.media.media_type != "image":
            raise ValidationError({
                "media": "Only image media can be attached here."
            })

    def __str__(self):
        return f"{self.product.name} - {self.media.file_name}"


# Stores the video media linked to each product, including the primary video selection.
class ProductVideos(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="videos",
    )

    media = models.ForeignKey(
        "media.Media",
        on_delete=models.PROTECT,
        related_name="product_videos",
    )

    is_primary = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["product"],
                condition=models.Q(is_primary=True),
                name="unique_primary_video_per_product",
            ),
            models.UniqueConstraint(
                fields=["product", "media"],
                name="unique_product_video",
            ),
        ]

    def clean(self):
        # Only allow actual video media to be attached to a product video record.
        super().clean()

        if self.media_id and self.media.media_type != "video":
            raise ValidationError({
                "media": "Only video media can be attached here."
            })

    def __str__(self):
        return f"{self.product.name} - {self.media.file_name}"


    
