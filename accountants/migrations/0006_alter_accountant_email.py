# Generated by Django 4.2.5 on 2023-11-01 15:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accountants", "0005_alter_accountant_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accountant",
            name="email",
            field=models.EmailField(max_length=254, unique=True, verbose_name="Email"),
        ),
    ]