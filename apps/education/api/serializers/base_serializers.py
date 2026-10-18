from rest_framework import serializers
from ...models import EducationContent, EducationCategory,EducationVideo,EducationMedia

class EducationImageSerializer(serializers.ModelSerializer):
    url = serializers.CharField(
        source="media.file_url",
        read_only=True,
    )

    alt_text = serializers.CharField(
        source="media.alt_text",
        read_only=True,
        allow_null=True,
    )

    class Meta:
        model = EducationMedia
        fields = [
            "id",
            "url",
            "alt_text",
            "is_primary",
            "caption",
        ]

class EducationVideoSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    source = serializers.CharField(
        source="media.video_source",
        read_only=True,
    )

    # Convert Aparat links into the frontend-compatible embed URL.
    def get_url(self, obj):
        media = obj.media

        if media.video_source == "aparat":
            video_id = media.file_url.rstrip("/").split("/")[-1]

            return (
                "https://www.aparat.com/video/video/embed/"
                f"videohash/{video_id}/vt/frame"
            )

        return media.file_url

    class Meta:
        model = EducationVideo
        fields = [
            "id",
            "url",
            "source",
            "is_primary",
            "caption",
        ]
class EducationContentSerializer(serializers.ModelSerializer):

    featured_media = serializers.SerializerMethodField()
    images = EducationImageSerializer(many=True, read_only=True)
    videos = EducationVideoSerializer(many=True, read_only=True)

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
            "images",
            "videos",
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
