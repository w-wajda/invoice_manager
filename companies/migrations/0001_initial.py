# Generated by Django 4.2.4 on 2023-09-05 20:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=100, verbose_name="Nazwa")),
                (
                    "nip",
                    models.CharField(
                        max_length=13,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[0-9a-zA-Z]{8,16}$",
                                "Wprowadź NIP bez znaków specjalnych, składający się z min. 8 znaków",
                            )
                        ],
                        verbose_name="NIP",
                    ),
                ),
                (
                    "regon",
                    models.CharField(
                        max_length=14,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^([0-9]{9}|[0-9]{14})$",
                                "Regon należy wprowadzać wyłącznie cyframi składającymi się z min. 9 znaków",
                            )
                        ],
                        verbose_name="Regon",
                    ),
                ),
                ("address", models.CharField(max_length=100, verbose_name="Adres")),
                (
                    "zip_code",
                    models.CharField(
                        max_length=10,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[0-9]{2}-[0-9]{3}$",
                                "Kod pocztowy w liczbach tylko w formacie xx-xxx",
                            )
                        ],
                        verbose_name="Kod pocztowy",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        max_length=60,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z ]+$", "Wpisz miasto tylko literami"
                            )
                        ],
                        verbose_name="Miasto",
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[0-9]{9,}$", "Wprowadź numer telefonu tylko cyframi"
                            )
                        ],
                        verbose_name="Numer telefonu",
                    ),
                ),
                (
                    "is_my_company",
                    models.BooleanField(
                        default=False, editable=False, verbose_name="Czy moja firma"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "firmy",
                "ordering": ["name"],
            },
        ),
    ]
