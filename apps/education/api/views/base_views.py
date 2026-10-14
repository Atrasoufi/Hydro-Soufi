from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from ...models import EducationContent, EducationCategory
from apps.education.api.serializers.base_serializers import (
    EducationContentSerializer,
    EducationHomeSerializer,
    EducationCategorySerializer,
)
from rest_framework import filters
from ...filter import EducationFilter
from django_filters.rest_framework import DjangoFilterBackend


class EducationPagination(PageNumberPagination):
    page_size = 12


# Lists published education content with filtering, title search, and pagination.
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
            .order_by("-id")
            .select_related("featured_media")
        )


# Provides the latest published education content for the homepage.
class EducationHomeAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = EducationHomeSerializer

    def get_queryset(self):
        # Keep the homepage feed limited to the four newest published items.
        return (
            EducationContent.objects.filter(status="PUBLISHED")
            .order_by("-id")
            .select_related("featured_media")[:4]
        )


# Lists only active education categories.
class EducationCategoryAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = EducationCategorySerializer

    def get_queryset(self):
        return EducationCategory.objects.filter(is_active=True)
