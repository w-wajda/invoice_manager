# Generated by Django 4.2.5 on 2024-01-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoices", "0016_alter_invoice_is_paid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="is_paid",
            field=models.BooleanField(default=False, verbose_name="Opłacona"),
        ),
    ]
