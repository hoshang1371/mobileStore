# Generated by Django 5.0.4 on 2024-11-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post_information", "0012_alter_paymentmethodedetail_paymentdetails_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentmethodedetail",
            name="PaymentDetails",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="روش پرداخت"
            ),
        ),
        migrations.AlterField(
            model_name="postaddressdetail",
            name="carrierDetails",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="روش ارسال"
            ),
        ),
    ]