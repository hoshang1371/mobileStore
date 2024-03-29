# Generated by Django 4.1.12 on 2024-02-14 18:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mobileStore_product', '0003_customercomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='customercomment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customercomment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
