from django.contrib import admin
from .models import Service, ServiceProduct, IndustryService

admin.site.register(Service)
admin.site.register(ServiceProduct)
admin.site.register(IndustryService)

# Register your models here.
