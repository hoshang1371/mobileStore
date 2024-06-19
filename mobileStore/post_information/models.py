from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import RegexValidator

from django_jalali.db import models as jmodels
from django.utils.timezone import now

class PostPrice(models.Model):
    title = models.CharField(max_length=150, verbose_name='هزینه ارسال ')
    price = models.IntegerField(verbose_name='هزینه ی پست')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'هزینه ارسال'