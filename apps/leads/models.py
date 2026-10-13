from django.db import models
from django.contrib.auth import get_user_model
from django_jalali.db import models as jmodels

User = get_user_model()


# Create your models here.
class ContactRequest(models.Model):

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=255, null=True, blank=True)

    subject = models.CharField(max_length=255)
    message = models.TextField()

    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField(auto_created=True)
