# Generated by Django 4.1.12 on 2024-02-14 18:34

from django.db import migrations
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileStore_product', '0004_customercomment_created_customercomment_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercomment',
            name='created',
            field=django_jalali.db.models.jDateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='تاریخ ایجاد سبد شمسی'),
        ),
        migrations.AlterField(
            model_name='customercomment',
            name='updated',
            field=django_jalali.db.models.jDateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='تاریخ ایجاد سبد شمسی'),
        ),
    ]
