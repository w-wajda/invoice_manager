# Generated by Django 4.2.4 on 2023-09-05 20:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
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
                    "country",
                    models.CharField(
                        max_length=30,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z ]{2,}$", "Podaj kraj tylko literami"
                            )
                        ],
                        verbose_name="Kraj",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "kraje",
                "ordering": ["country"],
            },
        ),
    ]
