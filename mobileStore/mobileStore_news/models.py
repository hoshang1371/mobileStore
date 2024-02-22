from django.db import models
import os

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"

class news(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')

    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''