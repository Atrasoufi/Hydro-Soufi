from rest_framework import serializers

from ...models import Service


class ServiceReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "name",
            "slug",
            "short_description",
            "full_description",
            "icon",
            "is_featured",
            "is_active",
            "sort_order",
        ]
        read_only_fields = fields