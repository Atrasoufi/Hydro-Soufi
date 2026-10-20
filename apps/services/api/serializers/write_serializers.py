from rest_framework import serializers
from ...models import Service


class ServiceWriteSerializer(serializers.ModelSerializer):
    cover_image = serializers.CharField()

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

    def get_cover_image(self, obj):
        return obj.cover_image.media.file_url
