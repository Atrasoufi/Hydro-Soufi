from django.contrib import admin
from .models import (
    Product,
    ProductCategories,
    ProductImages,
    ProductSpec,
    ProductVideos,
)

admin.site.register(Product)
admin.site.register(ProductCategories)
admin.site.register(ProductImages)
admin.site.register(ProductSpec)
admin.site.register(ProductVideos)
# Register your models here.
