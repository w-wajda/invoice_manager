# Generated by Django 4.2.5 on 2023-09-26 19:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("companies", "0004_alter_company_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="city",
            field=models.CharField(
                max_length=60,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[a-zA-Z ]+$", "Wpisz miasto tylko w postaci liter"
                    )
                ],
                verbose_name="Miasto",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="nip",
            field=models.CharField(
                max_length=13,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9a-zA-Z]{8,16}$",
                        "Wpisz NIP bez znaków specjalnych, składający się z min. 8 znaków",
                    )
                ],
                verbose_name="NIP",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="phone_number",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9]{9,}$", "Wpisz numer telefonu tylko w postaci liczb"
                    )
                ],
                verbose_name="Numer telefonu",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="regon",
            field=models.CharField(
                max_length=14,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{9}|[0-9]{14})$",
                        "Wpisz Regon składający się z min. 9 liczb",
                    )
                ],
                verbose_name="Regon",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="zip_code",
            field=models.CharField(
                max_length=10,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9]{2}-[0-9]{3}$",
                        "Wpisz kod pocztowy składający się z liczb w formacie xx-xxx",
                    )
                ],
                verbose_name="Kod pocztowy",
            ),
        ),
    ]
