from rest_framework import serializers
from ...models import Products, ProductImages


class ListProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = ["slug", "name", "shord_descriptoin"]

    def get_images(self, obj):
        if obj.primary_image:
            return obj.primary_image.url
