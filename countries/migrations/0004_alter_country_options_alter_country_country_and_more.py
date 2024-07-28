# Generated by Django 4.2.11 on 2024-07-25 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("countries", "0003_alter_country_country"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="country",
            options={"ordering": ["country"], "verbose_name_plural": "countries"},
        ),
        migrations.AlterField(
            model_name="country",
            name="country",
            field=models.CharField(max_length=30, verbose_name="Country"),
        ),
        migrations.AlterField(
            model_name="country",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
    ]
