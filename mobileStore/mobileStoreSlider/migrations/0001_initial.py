# Generated by Django 5.0.4 on 2024-07-30 19:14

import mobileStoreSlider.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SliderDown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='عنوان')),
                ('link', models.URLField(blank=True, max_length=100, null=True, verbose_name='ادرس')),
                ('description1', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('imageSlider', models.ImageField(blank=True, null=True, upload_to=mobileStoreSlider.models.upload_image_path, verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'اسلایدر پایین',
                'verbose_name_plural': 'اسلایدرها پایین',
            },
        ),
        migrations.CreateModel(
            name='SliderUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='عنوان')),
                ('link', models.URLField(blank=True, max_length=100, null=True, verbose_name='ادرس')),
                ('description1', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('description2', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('imageSlider', models.ImageField(blank=True, null=True, upload_to=mobileStoreSlider.models.upload_image_path, verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'اسلایدر بالا',
                'verbose_name_plural': 'اسلایدرها بالا',
            },
        ),
    ]
