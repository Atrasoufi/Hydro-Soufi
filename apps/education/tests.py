from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.test import TestCase
from django.urls import reverse

from apps.education.models import EducationCategory, EducationContent

User = get_user_model()


class EducationCacheTests(TestCase):
    def setUp(self):
        cache.clear()
        self.user = User.objects.create_user(
            username="edu-admin",
            email="edu@example.com",
            password="StrongPass123!",
        )
        self.category = EducationCategory.objects.create(
            name="Hydraulic Basics",
            description="Basic education content",
            is_active=True,
        )
        self.education = EducationContent.objects.create(
            category=self.category,
            author=self.user,
            title="Hydraulic Basics Guide",
            slug="hydraulic-basics-guide",
            excerpt="Learn the basics",
            content="Hydraulic theory content",
            status="PUBLISHED",
            is_featured=True,
        )

    def tearDown(self):
        cache.clear()

    def test_education_list_is_cached(self):
        response = self.client.get(reverse("education-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(cache.keys("*"))

    def test_education_cache_is_cleared_on_update(self):
        self.client.get(reverse("education-list"))
        self.assertTrue(cache.keys("*"))

        self.education.title = "Updated Hydraulic Basics Guide"
        self.education.save()

        self.assertFalse(cache.keys("*"))
