from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.db.models import Prefetch
from ..serializers.base_serializers import ProductDetailSerializer
from ...models import Products, ProductImages, ProductSpec


class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"

    def get_queryset(self):
        return Products.objects.select_related("category").prefetch_related(
            Prefetch(
                "images",
                queryset=(
                    ProductImages.objects.select_related("media")
                    .only(
                        "id",
                        "product",
                        "media",
                        "media__file_url",
                        "alt_text",
                        "is_primary",
                        "sorted_order",
                    )
                    .order_by("sorted_order", "id")
                ),
            ),
            Prefetch(
                "specs",
                queryset=(
                    ProductSpec.objects.only(
                        "id",
                        "product",
                        "specification_name",
                        "specification_value",
                    ).order_by("sort_order", "id")
                ),
            ),
        )
