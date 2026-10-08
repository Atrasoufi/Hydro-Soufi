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
