# Generated by Django 4.2.5 on 2024-01-03 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("invoices", "0017_alter_invoice_is_paid"),
    ]

    operations = [
        migrations.CreateModel(
            name="CorrectionInvoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "correction_invoice",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="correction_invoice",
                        to="invoices.invoice",
                        verbose_name="Correction Invoice",
                    ),
                ),
                (
                    "invoice",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoice",
                        to="invoices.invoice",
                        verbose_name="Faktura",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "correction invoices",
            },
        ),
    ]
