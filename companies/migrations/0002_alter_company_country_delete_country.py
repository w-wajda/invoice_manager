# Generated by Django 4.1.7 on 2023-04-06 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("countries", "0001_initial"),
        ("companies", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Country",
        ),
    ]
