
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from ...models import Service
from ..serializers import ServiceReadSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ServiceReadSerializer

    queryset = Service.objects.filter(
        is_active=True
    ).order_by("sort_order", "id")

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "short_description"]