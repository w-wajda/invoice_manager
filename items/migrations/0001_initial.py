# Generated by Django 4.1.7 on 2023-04-10 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("invoices", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("vat_rates", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                (
                    "pkwiu",
                    models.CharField(max_length=50, null=True, verbose_name="PWKiU"),
                ),
                ("amount", models.PositiveIntegerField(verbose_name="Amount")),
                ("net_price", models.PositiveIntegerField(verbose_name="Net price")),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="invoices.invoice",
                        verbose_name="Invoice",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
                (
                    "vat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="item",
                        to="vat_rates.vatrate",
                        verbose_name="Vat",
                    ),
                ),
            ],
        ),
    ]
