from rest_framework.routers import DefaultRouter

from .views.views import ServiceViewSet

router = DefaultRouter()
router.register("services", ServiceViewSet, basename="service")

urlpatterns = router.urls
