from .base_serializers import EducationContentSerializer

class EducationContentDetailSerializer(EducationContentSerializer):
    class Meta(EducationContentSerializer.Meta):
        fields = EducationContentSerializer.Meta.fields + ['content']

