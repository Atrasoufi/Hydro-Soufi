from django.db import models


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

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


    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question

