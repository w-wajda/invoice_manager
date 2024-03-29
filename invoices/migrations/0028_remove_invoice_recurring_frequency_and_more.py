# Generated by Django 4.2.10 on 2024-03-02 09:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoices", "0027_invoice_is_last_day"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="invoice",
            name="recurring_frequency",
        ),
        migrations.AlterField(
            model_name="invoice",
            name="is_last_day",
            field=models.BooleanField(
                default=False, verbose_name="Ostatni dzień miesiąca"
            ),
        ),
    ]
