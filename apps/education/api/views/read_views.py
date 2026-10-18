from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from ...models import EducationContent, EducationMedia, EducationVideo
from django.db.models import Prefetch
from apps.education.api.serializers.read_serilazers import (
    EducationContentDetailSerializer,
)


class EducationContentDetailAPIView(RetrieveAPIView):
    lookup_field = "slug"
    permission_classes = [AllowAny]
    serializer_class = EducationContentDetailSerializer

    def get_queryset(self):
        # Load the published content together with its related images and videos to avoid extra queries.
        return (
            EducationContent.objects.filter(status="PUBLISHED")
            .select_related("featured_media")
            .prefetch_related(
                Prefetch(
                    "media",
                    queryset=EducationMedia.objects.select_related("media")
                    .only(
                        "id",
                        "education",
                        "media",
                        "is_primary",
                        "caption",
                        "media__file_url",
                        "media__alt_text",
                    )
                    .order_by("id"),
                ),
                Prefetch(
                    "videos",
                    queryset=EducationVideo.objects.select_related("media")
                    .only(
                        "id",
                        "education",
                        "media",
                        "is_primary",
                        "caption",
                        "media__file_url",
                        "media__video_source",
                    )
                    .order_by("id"),
                ),
            )
        )
