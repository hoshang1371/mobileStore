# Generated by Django 4.1.12 on 2024-02-25 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobileStore_product', '0014_likescustomercomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='likescustomercomment',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mobileStore_product.product'),
            preserve_default=False,
        ),
    ]