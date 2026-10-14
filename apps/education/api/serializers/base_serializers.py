from rest_framework import serializers
from ...models import EducationContent, EducationCategory


class EducationContentSerializer(serializers.ModelSerializer):

    featured_media = serializers.SerializerMethodField()

    def get_featured_media(self, education_content):
        res = education_content.featured_media

        if res:
            return res.file_url

        return None

    class Meta:
        model = EducationContent
        fields = [
            "title",
            "slug",
            "excerpt",
            "content_type",
            "featured_media",
        ]


class EducationHomeSerializer(serializers.ModelSerializer):

    featured_media = serializers.SerializerMethodField()

    def get_featured_media(self, education_content):
        res = education_content.featured_media

        if res:
            return res.file_url

        return None

    class Meta:
        model = EducationContent
        fields = ["slug", "title", "featured_media"]


class EducationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationCategory
        fields = ["id", "name"]
