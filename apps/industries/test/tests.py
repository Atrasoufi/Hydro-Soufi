from django.core.cache import cache
from django.test import TestCase
from django.urls import reverse

from apps.industries.models import Industry


class IndustryCacheTests(TestCase):
    def setUp(self):
        cache.clear()
        self.industry = Industry.objects.create(
            name="Hydraulic Systems",
            short_description="Hydraulic support and systems",
            is_active=True,
        )

    def tearDown(self):
        cache.clear()

    def test_industry_list_is_cached(self):
        response = self.client.get(reverse("industries-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(cache.keys("*"))

    def test_industry_cache_is_cleared_on_update(self):
        self.client.get(reverse("industries-list"))
        self.assertTrue(cache.keys("*"))

        self.industry.name = "Updated Hydraulic Systems"
        self.industry.save()

        self.assertFalse(cache.keys("*"))
