from django.contrib import admin
from .models import Product, ProductCategories, ProductImages, ProductSpec

admin.site.register(Product)
admin.site.register(ProductCategories)
admin.site.register(ProductImages)
admin.site.register(ProductSpec)
# Register your models here.
