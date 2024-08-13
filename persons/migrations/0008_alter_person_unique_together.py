# Generated by Django 4.2.15 on 2024-08-12 19:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("persons", "0007_person_nip_person_pesel"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="person",
            unique_together={
                ("first_name", "last_name", "address", "zip_code", "city", "user")
            },
        ),
    ]
