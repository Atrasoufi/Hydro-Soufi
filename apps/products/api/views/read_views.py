from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from ..serializers.read_serailizers import (
    ProductListSerializer,
    ProductCategoryFilterSerializer,
    ProductFeaturedListSerializer,
)
from rest_framework.generics import ListAPIView
from ...models import Product, ProductImages, ProductCategories
from django.db.models import Prefetch
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from ...filters import ProductFilter

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class ProductPagination(PageNumberPagination):
    page_size = 10


# Lists searchable and filterable products with their primary images.
@method_decorator(cache_page(60 * 2), name="dispatch")
class ProductListView(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]
    pagination_class = ProductPagination

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]

    filterset_class = ProductFilter

    search_fields = [
        "name",
        "short_description",
    ]

    def get_queryset(self):
        return (
            Product.objects.only(
                "id",
                "name",
                "slug",
                "short_description",
            )
            .prefetch_related(
                Prefetch(
                    "images",
                    queryset=ProductImages.objects.filter(
                        is_primary=True,
                    )
                    .select_related("media")
                    .only(
                        "id",
                        "media",
                        "product",
                        "media__file_url",
                    ),
                    to_attr="primary_image",
                )
            )
            .order_by("-id")
        )


# Lists up to four featured products with their primary images.
@method_decorator(cache_page(60 * 5), name="dispatch")
class ProductFeaturedListView(ListAPIView):
    serializer_class = ProductFeaturedListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return (
            Product.objects.only(
                "id",
                "name",
                "slug",
            )
            .filter(is_featured=True)
            .prefetch_related(
                Prefetch(
                    "images",
                    queryset=ProductImages.objects.filter(
                        is_primary=True,
                    )
                    .select_related("media")
                    .only(
                        "id",
                        "media",
                        "product",
                        "media__file_url",
                    ),
                    to_attr="primary_image",
                )
            )
            .order_by("-id")[:4]
        )


# Lists product categories for filter options.


@method_decorator(cache_page(60 * 5), name="dispatch")
class ProductCategoryFilterView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductCategoryFilterSerializer

    def get_queryset(self):
        return ProductCategories.objects.only("id", "name")
