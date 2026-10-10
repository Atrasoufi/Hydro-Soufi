from django.urls import path, include
from .views.base_views import IndustryListAPIView

urlpatterns = [
    path('industries/',IndustryListAPIView.as_view(),name='industries-list'),
]