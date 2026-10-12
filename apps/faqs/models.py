from django.db import models


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    category = models.CharField(max_length=100)

    products = models.ManyToManyField(
        "products.Product",
        related_name="faqs",
        blank=True,
    )

    services = models.ManyToManyField(
        "services.Service",
        related_name="faqs",
        blank=True,
    )

    industries = models.ManyToManyField(
        "industries.Industry",
        related_name="faqs",
        blank=True,
    )

    sort_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question

