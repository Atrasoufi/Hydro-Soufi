from rest_framework import serializers
from ...models import Service


class ServiceBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "name",
            "slug",
            "short_description",
            "icon",
            "is_featured",
            "is_active",
        ]
        read_only_fields = ["id", "slug"]
