from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from ...models import Service
from ..serializers.read_serializers import ServiceReadSerializer


from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


# Exposes active services with search over their names and descriptions.
@method_decorator(cache_page(60 * 5), name="dispatch")
class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ServiceReadSerializer

    queryset = (
        Service.objects.filter(is_active=True)
        .select_related("cover_image")
        .order_by("id")
    )

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    # filter_backends = [filters.SearchFilter]
    search_fields = ["name", "short_description"]

    # Returns up to four featured services for the homepage.
    @action(detail=False, methods=["get"])
    def home(self, request):
        services = self.get_queryset().filter(is_featured=True)[:6]

        serializer = self.get_serializer(services, many=True)
        return Response(serializer.data)
