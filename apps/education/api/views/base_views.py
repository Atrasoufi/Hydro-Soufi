from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from django.db.models import Prefetch
from ...models import (
    EducationContent,
    EducationCategory,
    EducationMedia,
    EducationVideo,
)
from apps.education.api.serializers.base_serializers import (
    EducationContentSerializer,
    EducationHomeSerializer,
    EducationCategorySerializer,
)
from rest_framework import filters
from ...filter import EducationFilter
from django_filters.rest_framework import DjangoFilterBackend



from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class EducationPagination(PageNumberPagination):
    page_size = 12


# Lists published education content with filtering, title search, and pagination.
@method_decorator(cache_page(60 * 5), name="dispatch")
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
            )
        )

# Provides the latest published education content for the homepage.
@method_decorator(cache_page(60 * 2), name="dispatch")
class EducationHomeAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = EducationHomeSerializer

    def get_queryset(self):
        # Keep the homepage feed limited to the four newest published items.
        return (
            EducationContent.objects.only(
                "id", "is_featured", "slug", "title", "featured_media"
            )
            .filter(status="PUBLISHED", is_featured=True)
            .order_by("-id")
            .select_related("featured_media")[:4]
        )


# Lists only active education categories.
@method_decorator(cache_page(60 * 2), name="dispatch")
class EducationCategoryAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = EducationCategorySerializer

    def get_queryset(self):
        return EducationCategory.objects.filter(is_active=True)
