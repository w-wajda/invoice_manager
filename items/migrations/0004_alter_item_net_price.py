# Generated by Django 4.2.5 on 2024-01-31 21:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0003_remove_item_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="net_price",
            field=models.DecimalField(
                decimal_places=2, max_digits=9, verbose_name="Cena netto"
            ),
        ),
    ]
