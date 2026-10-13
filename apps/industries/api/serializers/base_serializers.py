from rest_framework import serializers
from ...models import Industry


class IndustrySerializer(serializers.ModelSerializer):

    cover_image = serializers.SerializerMethodField()

    def get_cover_image(self, industry):
        res = industry.cover_image

        if res:
            return res.file_url

        return None

    class Meta:
        model = Industry
        fields = [
            "name",
            "short_description",
            "icon",
            "cover_image",
        ]


class IndustryFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ["id", "name"]


class IndustryHomeSerializer(serializers.ModelSerializer):
    cover_image = serializers.SerializerMethodField()

    class Meta:
        model = Industry
        fields = ["id", "name", "cover_image"]

    def get_cover_image(self, industry):
        if industry.cover_image:
            return industry.cover_image.file_url

        return None
