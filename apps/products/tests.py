from django.core.cache import cache
from django.test import TestCase
from django.urls import reverse

from apps.products.models import Product, ProductCategories


class ProductCacheTests(TestCase):
    def setUp(self):
        cache.clear()
        self.category = ProductCategories.objects.create(
            name="Hydraulic Pumps",
            description="Hydraulic pump products",
            is_active=True,
        )
        self.product = Product.objects.create(
            category=self.category,
            name="Hydraulic Pump X1",
            slug="hydraulic-pump-x1",
            short_description="High pressure solution",
            full_description="High pressure hydraulic pump",
            is_active=True,
            is_featured=True,
        )

    def tearDown(self):
        cache.clear()

    def test_product_category_list_is_cached(self):
        response = self.client.get(reverse("product_category"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(cache.keys("*"))

    def test_product_category_cache_is_cleared_on_update(self):
        self.client.get(reverse("product_category"))
        self.assertTrue(cache.keys("*"))

        self.category.name = "Updated Hydraulic Pumps"
        self.category.save()

        self.assertFalse(cache.keys("*"))
