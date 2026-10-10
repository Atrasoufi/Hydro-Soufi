from django.urls import path
from .views.base_views import ContactRequestAPIView

urlpatterns = [
    path('consultation/',ContactRequestAPIView.as_view(),name='leads-consultation'),
]