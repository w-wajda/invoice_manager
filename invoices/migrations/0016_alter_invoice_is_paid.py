# Generated by Django 4.2.5 on 2023-12-04 21:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoices", "0015_invoice_is_paid_alter_invoice_person"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="is_paid",
            field=models.BooleanField(default=False, verbose_name="Paid"),
        ),
    ]
