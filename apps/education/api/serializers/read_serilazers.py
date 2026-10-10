from .base_serializers import EducationContentSerializer

class EducationContentDetailSerializer(EducationContentSerializer):
    class Meta(EducationContentSerializer.Meta):
        feilds = EducationContentSerializer.Meta.fields + ['content']

