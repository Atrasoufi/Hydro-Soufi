from django.urls import path
from .views.read_views import ProductListView
from .views.base_views import ProductDetailView

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
]
