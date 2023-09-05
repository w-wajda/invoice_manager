# Generated by Django 4.2.4 on 2023-09-05 20:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("companies", "0002_initial"),
        ("currencies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Invoice",
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
                    "invoice_number",
                    models.CharField(
                        max_length=30,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[0-9]+/[0-9]{4}$",
                                "Numer faktury należy wprowadzać cyfrowo, wyłącznie w formacie numer/rrrr",
                            )
                        ],
                        verbose_name="Numer faktury",
                    ),
                ),
                (
                    "invoice_type",
                    models.IntegerField(
                        choices=[(0, "Sprzedaż"), (1, "Zakupy")],
                        verbose_name="Typ faktury",
                    ),
                ),
                (
                    "recurring_frequency",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "Co tydzień"),
                            (1, "Co dwa tygodnie"),
                            (2, "Co miesiąc"),
                            (3, "Co trzy miesiące"),
                        ],
                        null=True,
                        verbose_name="Cykliczna częstotliwość",
                    ),
                ),
                (
                    "is_recurring",
                    models.BooleanField(default=False, verbose_name="Cykliczna"),
                ),
                (
                    "create_date",
                    models.DateField(
                        default=django.utils.timezone.now,
                        verbose_name="Data utworzenia",
                    ),
                ),
                (
                    "sale_date",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="Data sprzedaży"
                    ),
                ),
                (
                    "payment_date",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="Data płatności"
                    ),
                ),
                (
                    "payment_method",
                    models.IntegerField(
                        choices=[(0, "Przelew"), (1, "Gotówka")],
                        verbose_name="Rodzaj płatności",
                    ),
                ),
                (
                    "account_number",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[0-9A-Z ]{15,32}$",
                                "Wpisz numer rachunku składający się z min. 15 znaków bez znaków specjalnych",
                            )
                        ],
                        verbose_name="Numer konta",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client_invoice",
                        to="companies.company",
                        verbose_name="Kontrahent",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoice",
                        to="companies.company",
                        verbose_name="Firma",
                    ),
                ),
                (
                    "currency",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoice",
                        to="currencies.currency",
                        verbose_name="Waluta",
                    ),
                ),
            ],
            options={
                "ordering": ["-sale_date"],
            },
        ),
    ]
