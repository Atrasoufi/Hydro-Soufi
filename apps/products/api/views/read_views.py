from serializers.read_serailizers import ProductListSerializer
from rest_framework.generics import ListAPIView
from ...models import Products, ProductImages
from django.db.models import Prefetch


class ProductListView(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Products.objects.only(
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
                "media__file_url",
            ),
            to_attr="primary_image",
        )
    )
