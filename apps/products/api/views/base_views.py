from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.db.models import Prefetch
from ..serializers.base_serializers import ProductDetailSerializer
from ...models import Product, ProductImages, ProductSpec, ProductVideos


class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"

    def get_queryset(self):
        # Load the product and the related media/spec data in a single optimized query set.
        return Product.objects.select_related("category").prefetch_related(
            Prefetch(
                "images",
                queryset=(
                    ProductImages.objects.select_related("media")
                    .only(
                        "id",
                        "product",
                        "media",
                        "media__file_url",
                        "media__alt_text",
                        "is_primary",
                    )
                    .order_by("id")
                ),
            ),

            Prefetch(
                "videos",
                queryset=(
                    ProductVideos.objects.select_related("media")
                    .only(
                        "id",
                        "product",
                        "media",
                        "media__file_url",
                        "media__video_source",
                        "is_primary",
                    )
                    .order_by("id")
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
                    ).order_by("id")
                ),
                to_attr="product_specs",
            ),
        )
