# Generated by Django 4.1.12 on 2024-02-20 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobileStore_product', '0011_alter_customercomment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercomment',
            name='CommentProduct',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='mobileStore_product.product', verbose_name='محصول پیام'),
            preserve_default=False,
        ),
    ]
