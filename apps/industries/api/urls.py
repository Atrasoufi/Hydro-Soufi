from django.urls import path, include
from .views.base_views import IndustryListAPIView, IndustryFilterListView, IndustryHomeListView



urlpatterns = [
    path('industries/',IndustryListAPIView.as_view(),name='industries-list'),
    path("filters/",IndustryFilterListView.as_view(),name="industry-filters",),
    path("home/",IndustryHomeListView.as_view(),name="industry-home",),
]