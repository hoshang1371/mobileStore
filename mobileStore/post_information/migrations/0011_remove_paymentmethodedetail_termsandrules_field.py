# Generated by Django 5.0.4 on 2024-11-02 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("post_information", "0010_paymentmethodedetail_termsandrules_field_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="paymentmethodedetail",
            name="TermsAndRules_field",
        ),
    ]