from django.urls import path, include
from .views.base_views import (
    EducationContentListAPIView,
    EducationHomeAPIView,
    EducationCategoryAPIView,
)
from .views.read_views import EducationContentDetailAPIView

urlpatterns = [
    path("educations/", EducationContentListAPIView.as_view(), name="education-list"),
    path(
        "education/<slug:slug>/",
        EducationContentDetailAPIView.as_view(),
        name="education-detail",
    ),
    path('education/home/',EducationHomeAPIView.as_view(),name='education-home'),
    path('education/cagetory/',EducationCategoryAPIView.as_view(),name='education-category'),
]
