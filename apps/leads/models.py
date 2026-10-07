from django.db import models
from django.contrib.auth import get_user_model
from django_jalali.db import models as jmodels

User = get_user_model()


# Create your models here.
class ContactRequest(models.Model):

    name = models.CharField(255)
    phone = models.CharField(30)
    email = models.CharField(255, null=True, blank=True)

    subject = models.CharField(255)
    message = models.TextField()

    status = models.CharField(default="NEW")

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="contact_requests",
    )

    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField()
