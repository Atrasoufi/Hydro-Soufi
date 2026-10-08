from rest_framework import serializers
from ...models import Industry

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model =Industry
        fields = [
            'name',
            'slug',
            'short_description',
            'icon',
            'cover_image',
        ]
        
