# Generated by Django 4.2.5 on 2023-12-04 21:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("currencies", "0004_alter_exchangerate_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="exchangerate",
            options={"verbose_name_plural": "kursy wymiany"},
        ),
    ]
