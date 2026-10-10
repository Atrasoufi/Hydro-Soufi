from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from ...models import EducationContent
from apps.education.api.serializers.read_serilazers import (
    EducationContentDetailSerializer,
)


class EducationContentDetailAPIView(RetrieveAPIView):
    lookup_field = "slug"
    permission_classes = [AllowAny]
    serializer_class = EducationContentDetailSerializer

    def get_queryset(self):
        return EducationContent.objects.filter(status="PUBLISHED").select_related(
            "featured_media"
        )
