# Generated by Django 4.2.11 on 2024-07-31 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("persons", "0006_alter_person_options_alter_person_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="nip",
            field=models.CharField(
                blank=True, max_length=13, null=True, verbose_name="NIP"
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="pesel",
            field=models.CharField(
                blank=True, max_length=11, null=True, verbose_name="PESEL"
            ),
        ),
    ]
