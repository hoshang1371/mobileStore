# Generated by Django 4.1.12 on 2024-02-20 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobileStore_product', '0008_alter_customercomment_commentproduct_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercomment',
            name='parent',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='mobileStore_product.customercomment', verbose_name='زیر دسته'),
        ),
    ]
