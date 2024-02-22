from django.db import models
# from django.contrib.auth.models import User
# from mobileStore_Social.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

from django.conf import settings
import os

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"

class Founders(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name='نام اواتار')
    position = models.CharField(max_length=150, verbose_name='جایگاه اواتار')
    description = models.TextField(verbose_name='توضیحات اواتار')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر اواتار')

    class Meta:
        verbose_name = 'مؤسس'
        verbose_name_plural = 'مؤسس ها'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"
    
    def get_image(self):
        if self.image:
            # print(settings.Public_Host)
            # return 'http://127.0.0.1:8000' + self.image.url
            return settings.ALLOWED_HOSTS[0] + self.image.url
        return ''
