# Generated by Django 4.0.1 on 2022-01-14 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0015_remove_company_street_and_number_company_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='phone_number',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Phone number'),
        ),
    ]
