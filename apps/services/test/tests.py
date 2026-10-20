from django.core.cache import cache
from django.test import TestCase
from django.urls import reverse

from apps.services.models import Service


class ServiceCacheTests(TestCase):
    def setUp(self):
        cache.clear()
        self.service = Service.objects.create(
            name="Hydraulic Pump Service",
            short_description="Maintenance and installation support",
            is_active=True,
            is_featured=True,
        )

    def tearDown(self):
        cache.clear()

    def test_service_list_is_cached(self):
        response = self.client.get(reverse("service-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(cache.keys("*"))

    def test_service_cache_is_cleared_on_update(self):
        self.client.get(reverse("service-list"))
        self.assertTrue(cache.keys("*"))

        self.service.name = "Updated Hydraulic Service"
        self.service.save()

        self.assertFalse(cache.keys("*"))
