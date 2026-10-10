from rest_framework import serializers
from ...models import Service


class ServiceWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "name",
            "slug",
            "short_description",
            "icon",
            "is_featured",
            "is_active",
        ]
        extra_kwargs = {
            "slug": {"required": False},
        }