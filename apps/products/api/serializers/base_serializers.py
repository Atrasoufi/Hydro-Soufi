from rest_framework import serializers
from ...models import Products, ProductImages, ProductSpec, ProductCategories


class ProductCategorySerialiser(serializers.ModelSerializer):

    class Meta:
        model = ProductCategories
        fields = "__all__"


class ProductSpecSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ProductSpec
        fields = ["id", "specification_name", "specification_value"]


class ProductImageSerializer(serializers.ModelSerializer):
    url = serializers.CharField(
        source="media.file_url",
        read_only=True,
    )

    class Meta:
        model = ProductImages
        fields = [
            "id",
            "url",
            "alt_text",
            "is_primary",
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(
        many=True,
        read_only=True,
    )

    product_specs = ProductSpecSerialiser(many=True, read_only=True)

    class Meta:
        model = Products
        fields = [
            "id",
            "name",
            "slug",
            "short_description",
            "description",
            "images",
            "category",
            "product_specs",
            "is_active",
            "is_featured",
            "created_at",
        ]
