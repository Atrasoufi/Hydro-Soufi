from rest_framework import serializers
from ...models import Service


class ServiceWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "name",
            "short_description",
            "icon",
            "is_featured",
            "is_active",
        ]
