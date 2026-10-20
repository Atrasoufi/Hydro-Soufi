from rest_framework import serializers
from ...models import Service


class ServiceBaseSerializer(serializers.ModelSerializer):
    cover_image = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = [
            "id",
            "name",
            "short_description",
            "cover_image",
            "icon",
            "is_featured",
            "is_active",
        ]
        read_only_fields = ["id", "slug"]

    def get_cover_image(self, obj):
        return obj.cover_image.file_url
