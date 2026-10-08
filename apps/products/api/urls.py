from django.urls import path
from .views.read_views import ProductListView

urlpatterns = [path("products/", ProductListView.as_view(), name="product_list")]
