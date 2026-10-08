from django.db import models

class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    
    category = models.CharField(max_length=100)

    sort_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.question
    

class ProductFaq(models.Model):
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="product_faqs",
    )
    faq = models.ForeignKey(
        Faq,
        on_delete=models.CASCADE,
        related_name="product_faqs",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["product", "faq"],
                name="unique_product_faq",
            )
        ]
        
class ServiceFaq(models.Model):
    service = models.ForeignKey(
        "services.Service",
        on_delete=models.CASCADE,
        related_name="service_faqs",
    )
    faq = models.ForeignKey(
        Faq,
        on_delete=models.CASCADE,
        related_name="service_faqs",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["service", "faq"],
                name="unique_service_faq",
            )
        ]
        
class IndustryFaq(models.Model):
    industry = models.ForeignKey(
        "industries.Industry",
        on_delete=models.CASCADE,
        related_name="industry_faqs",
    )
    faq = models.ForeignKey(
        Faq,
        on_delete=models.CASCADE,
        related_name="industry_faqs",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["industry", "faq"],
                name="unique_industry_faq",
            )
        ]