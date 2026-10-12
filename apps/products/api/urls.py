from django.urls import path
from .views.read_views import (
    ProductListView,
    ProductCategoryFilterView,
    ProductFeaturedListView,
)
from .views.base_views import ProductDetailView

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
    path("categorys/", ProductCategoryFilterView.as_view(), name="product_category"),
    path("featured/", ProductFeaturedListView.as_view(), name="product_featured"),
]
