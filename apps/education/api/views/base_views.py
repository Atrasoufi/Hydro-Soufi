from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from ...models import EducationContent
from apps.education.api.serializers.base_serializers import EducationContentSerializer
from rest_framework import filters
from ...filter import EducationFilter
from django_filters.rest_framework import DjangoFilterBackend


class EducationPagination(PageNumberPagination):
    page_size = 12


class EducationContentListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    pagination_class = EducationPagination
    serializer_class = EducationContentSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]

    filterset_class = EducationFilter

    search_fields = [
        "title",
    ]

    def get_queryset(self):
        return (
            EducationContent.objects.filter(status="PUBLISHED")
            .order_by("-published_at", "-id")
            .select_related("featured_media")
        )
