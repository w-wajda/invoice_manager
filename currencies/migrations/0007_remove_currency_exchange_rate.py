# Generated by Django 4.2.3 on 2023-08-02 19:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("currencies", "0006_alter_currency_options_currency_exchange_rate"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="currency",
            name="exchange_rate",
        ),
    ]
