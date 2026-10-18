from rest_framework import serializers
from ...models import Product, ProductImages, ProductSpec, ProductCategories, ProductVideos


class ProductCategorySerialiser(serializers.ModelSerializer):

    class Meta:
        model = ProductCategories
        fields = "__all__"


class ProductSpecSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ProductSpec
        fields = ["id", "specification_name", "specification_value"]


class ProductImageSerializer(serializers.ModelSerializer):
    url = serializers.CharField(
        source="media.file_url",
        read_only=True,
    )

    alt_text = serializers.CharField(
        source="media.alt_text",
        read_only=True,
        allow_null=True,
    )

    class Meta:
        model = ProductImages
        fields = [
            "id",
            "alt_text",
            "url",
            "is_primary",
        ]
class ProductVideoSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField()

    # Convert Aparat links to the embed URL required by the frontend player.
    def get_url(self, obj):

        media = obj.media

        if media.video_source == "aparat":
            video_id = media.file_url.rstrip("/").split("/")[-1]
            return (
                "https://www.aparat.com/video/video/embed/"
                f"videohash/{video_id}/vt/frame"
            )
            

        return media.file_url

    source = serializers.CharField(
        source="media.video_source",
        read_only=True,
    )

    class Meta:
        model = ProductVideos
        fields = [
            "id",
            "url",
            "source",
            "is_primary",
        ]

class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(
        many=True,
        read_only=True,
    )

    videos = ProductVideoSerializer(
    many=True,
    read_only=True,
    )

    product_specs = ProductSpecSerialiser(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "short_description",
            "full_description",
            "images",
            "videos",
            "category",
            "product_specs",
            "is_active",
            "is_featured",
            "created_at",
        ]
