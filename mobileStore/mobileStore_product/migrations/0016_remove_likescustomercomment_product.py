# Generated by Django 4.1.12 on 2024-02-25 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobileStore_product', '0015_likescustomercomment_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likescustomercomment',
            name='product',
        ),
    ]
