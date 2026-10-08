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
            "slug",
            "short_description",
            "icon",
            "cover_image",
        ]
