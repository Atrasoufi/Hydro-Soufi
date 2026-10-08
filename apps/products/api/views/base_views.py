from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.db.models import Prefetch
from ..serializers.base_serializers import ProductDetailSerializer
from ...models import Products, ProductImages


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
                        "alt_text",
                        "product",
                        "is_primary",
                        "media",
                        "media__file_url",
                    )
                    .order_by("id")
                ),
            )
        )
