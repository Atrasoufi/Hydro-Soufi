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
            "sort_order",
        ]


class HomeServiceSerializer(ServiceBaseSerializer):
    class Meta(ServiceBaseSerializer.Meta):
        fields = [
            "name",
            "slug",
            "short_description",
            "icon",
        ]


class ServiceDetailSerializer(ServiceBaseSerializer):
    class Meta(ServiceBaseSerializer.Meta):
        fields = [
            "id",
            "name",
            "slug",
            "short_description",
            "full_description",
            "icon",
            "is_featured",
            "sort_order",
        ]