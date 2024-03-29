# Generated by Django 4.1.12 on 2024-02-14 18:37

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileStore_product', '0006_alter_customercomment_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercomment',
            name='created',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد سبد شمسی'),
        ),
        migrations.AlterField(
            model_name='customercomment',
            name='updated',
            field=django_jalali.db.models.jDateTimeField(auto_now=True, null=True, verbose_name='تاریخ تغییر سبد شمسی'),
        ),
    ]
