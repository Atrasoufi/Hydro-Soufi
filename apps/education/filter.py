import django_filters

from .models import EducationContent


class EducationFilter(django_filters.FilterSet):
    class Meta:
        model = EducationContent
        fields = [
            "category",
        ]
