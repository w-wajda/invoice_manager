# Generated by Django 4.2.5 on 2023-11-04 13:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="user",
        ),
    ]
