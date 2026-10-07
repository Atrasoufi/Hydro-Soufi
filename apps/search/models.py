from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.

class SearchLogs(models.Model):

    query = models.CharField(max_length=500)

    user_ip = models.CharField(max_length=100)

    result_count = models.IntegerField()

    created_at = jmodels.jDateTimeField()