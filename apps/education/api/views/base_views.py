from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from ...models import EducationContent
from apps.education.api.serializers.base_serializers import EducationContentSerializer


class EducationPagination(PageNumberPagination):
    page_size = 12


class EducationContentListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    pagination_class = EducationPagination
    serializer_class = EducationContentSerializer

    def get_queryset(self):
        return (
            EducationContent.objects.filter(status="PUBLISHED")
            .order_by("-published_at", "-id")
            .select_related("featured_media")
        )
