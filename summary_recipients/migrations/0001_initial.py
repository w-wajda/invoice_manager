# Generated by Django 4.2.5 on 2023-11-02 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("companies", "0010_delete_summaryrecipient"),
    ]

    operations = [
        migrations.CreateModel(
            name="SummaryRecipient",
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
                ("description", models.CharField(max_length=50, verbose_name="Opis")),
                ("day", models.IntegerField(verbose_name="Dzień wysłania")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "settlement_types",
                    models.IntegerField(
                        choices=[(0, "Co miesiąc"), (1, "Kwartalnie")],
                        verbose_name="Rodzaj rozliczenia",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="summary_recipients",
                        to="companies.company",
                        verbose_name="Firma",
                    ),
                ),
            ],
        ),
    ]
