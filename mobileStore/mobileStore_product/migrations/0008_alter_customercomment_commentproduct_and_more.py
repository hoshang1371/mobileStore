# Generated by Django 4.1.12 on 2024-02-14 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mobileStore_product', '0007_alter_customercomment_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercomment',
            name='CommentProduct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mobileStore_product.product', verbose_name='محصول پیام'),
        ),
        migrations.AlterField(
            model_name='customercomment',
            name='created',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد پیام شمسی'),
        ),
        migrations.AlterField(
            model_name='customercomment',
            name='updated',
            field=django_jalali.db.models.jDateTimeField(auto_now=True, null=True, verbose_name='تاریخ تغییر پیام شمسی'),
        ),
        migrations.AlterField(
            model_name='customercomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر پیام'),
        ),
    ]
