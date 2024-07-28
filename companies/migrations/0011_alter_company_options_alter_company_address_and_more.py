# Generated by Django 4.2.11 on 2024-07-25 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("countries", "0004_alter_country_options_alter_country_country_and_more"),
        ("companies", "0010_delete_summaryrecipient"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="company",
            options={"ordering": ["name"], "verbose_name_plural": "companies"},
        ),
        migrations.AlterField(
            model_name="company",
            name="address",
            field=models.CharField(max_length=100, verbose_name="Address"),
        ),
        migrations.AlterField(
            model_name="company",
            name="city",
            field=models.CharField(max_length=60, verbose_name="City"),
        ),
        migrations.AlterField(
            model_name="company",
            name="country",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="countries.country",
                verbose_name="Country",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="is_my_company",
            field=models.BooleanField(
                default=False, editable=False, verbose_name="Is my company"
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="company",
            name="phone_number",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Phone number"
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="zip_code",
            field=models.CharField(max_length=10, verbose_name="ZIP Code"),
        ),
    ]
