
from django.test import TestCase
from django.core.cache import cache
from django.urls import reverse

from apps.products.models import ProductCategories


class ProductCategoryCacheTests(TestCase):
    def setUp(self):
        cache.clear()
        self.category = ProductCategories.objects.create(
            name="Hydraulic Pumps",
            description="Hydraulic pump products",
        )

    def tearDown(self):
        cache.clear()

    def test_category_list_returns_categories(self):
        response = self.client.get(reverse("product_category"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            response.data[0]["name"],
            "Hydraulic Pumps",
        )
