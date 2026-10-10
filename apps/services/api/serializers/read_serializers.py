from .base_serializers import ServiceBaseSerializer

class ServiceReadSerializer(ServiceBaseSerializer):
    class Meta(ServiceBaseSerializer.Meta):
        fields = ServiceBaseSerializer.Meta.fields

