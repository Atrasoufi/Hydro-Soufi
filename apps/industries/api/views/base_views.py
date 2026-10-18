from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from ...models import Industry
from apps.industries.api.serializers.base_serializers import (
    IndustrySerializer,
    IndustryFilterSerializer,
    IndustryHomeSerializer,
)


from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Lists active industries with their cover images.

@method_decorator(cache_page(60 * 5), name="dispatch")
class IndustryListAPIView(ListAPIView):
    serializer_class = IndustrySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return (
            Industry.objects.filter(is_active=True)
            .order_by("id")
            .select_related("cover_image")
        )


# Lists active, named industries for filter options.

@method_decorator(cache_page(60 * 5), name="dispatch")
class IndustryFilterListView(ListAPIView):
    serializer_class = IndustryFilterSerializer

    def get_queryset(self):
        return Industry.objects.filter(
            is_active=True,
            name__gt="",
        ).order_by("id")


# Provides up to four active, named industries for the homepage.


@method_decorator(cache_page(60 * 5), name="dispatch")
class IndustryHomeListView(ListAPIView):
    serializer_class = IndustryHomeSerializer

    def get_queryset(self):
        return ( Industry.objects.filter(
            is_active=True,
            name__gt="",
        ).order_by("id")
        .select_related('cover_image')[:4]
        )
