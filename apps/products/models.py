from django.db import models
from django.contrib.auth import get_user_model
from django_jalali.db import models as jmodels

# Create your models here.


class ProductCategories(models.Model):
    # parent_id =
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=200)
    description = models.TextField()

    # image_media_id = relation to media

    is_active = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)


class Products(models.Model):
    category_id = models.ForeignKey(
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


class ProductImages(models.Model):
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="images"
    )

    # media = related to media

    alt_text = models.CharField(max_length=50)

    is_primary = models.BooleanField(default=False)
    sorted_order = models.IntegerField(default=0)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=["product", "media"],
    #             name="unique_user_product",
    #         )
    #     ]
