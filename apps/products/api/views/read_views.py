from serializers.read_serailizers import ProductListSerializer
from rest_framework.generics import ListAPIView
from ...models import Products, ProductImages
from django.db.models import Prefetch
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 10


class ProductListView(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]
    pagination_class = ProductPagination

    def get_queryset(self):
        return Products.objects.only(
            "id",
            "name",
            "slug",
            "short_description",
        ).prefetch_related(
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


class ProductFeaturedListView(ProductListView):

    def get_queryset(self):
        query = super().get_queryset()

        return query.filter(is_featured=True)
