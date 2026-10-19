from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.db.models import Prefetch
from ..serializers.base_serializers import ProductDetailSerializer
from ...models import Product, ProductImages, ProductSpec


from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page



@method_decorator(cache_page(60 * 2), name="dispatch")
class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"

    def get_queryset(self):
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
