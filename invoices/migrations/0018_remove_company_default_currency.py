# Generated by Django 4.0.1 on 2022-01-14 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0017_alter_company_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='default_currency',
        ),
    ]
