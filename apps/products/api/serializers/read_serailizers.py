from rest_framework import serializers
from ...models import Product, ProductCategories


class ProductListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "short_description",
            "image",
        ]

    def get_image(self, obj):
        if not obj.primary_image:
            return None

        return obj.primary_image[0].media.file_url


class ProductCategoryFilterSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategories
        fields = ["id", "name"]
