from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from ...models import Industry
from apps.industries.api.serializers.base_serializers import IndustrySerializer


class IndustryListAPIView(ListAPIView):
    serializer_class = IndustrySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return (
            Industry.objects.filter(is_active=True)
            .order_by("sort_order")
            .select_related("cover_image")
        )


from rest_framework import generics

from .models import Industry
from .serializers import (
    IndustryFilterSerializer,
    IndustryHomeSerializer,
)


class IndustryFilterListView(generics.ListAPIView):
    serializer_class = IndustryFilterSerializer

    def get_queryset(self):
        return Industry.objects.filter(
            is_active=True,
            name__gt="",
        ).order_by("sort_order", "id")


class IndustryHomeListView(generics.ListAPIView):
    serializer_class = IndustryHomeSerializer

    def get_queryset(self):
        return Industry.objects.filter(
            is_active=True,
            name__gt="",
        ).order_by("sort_order", "id")
