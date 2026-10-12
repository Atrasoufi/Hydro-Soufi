from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    short_description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)

    icon = models.CharField(max_length=255, blank=True)
    cover_image = models.ForeignKey(
        "media.Media",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="cover_for_service",
    )

    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    sort_order = models.IntegerField(default=0)


class ServiceProduct(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="service_products",
    )

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="service_products",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["service", "product"],
                name="unique_service_product",
            )
        ]


class IndustryService(models.Model):
    industry = models.ForeignKey(
        "industries.Industry",
        on_delete=models.CASCADE,
        related_name="industry_services",
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="industry_services",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["industry", "service"],
                name="unique_industry_service",
            )
        ]
