# Generated by Django 4.0.1 on 2022-01-11 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0008_remove_item_unit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Unit',
        ),
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.CharField(default=1, max_length=10, verbose_name='Unit'),
            preserve_default=False,
        ),
    ]
