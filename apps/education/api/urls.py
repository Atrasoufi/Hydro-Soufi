from django.urls import path, include
from .views.base_views import EducationContentListAPIView

urlpatterns = [
    path('education/',EducationContentListAPIView.as_view(),name='education-list'),
    path('education/<slug:slug>/',EducationContentListAPIView.as_view(),name='education-detail'),
]