# Generated by Django 4.2.1 on 2023-06-02 10:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("countries", "0004_alter_country_country_alter_country_is_my_country"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="country",
            options={"ordering": ["pk"], "verbose_name_plural": "countries"},
        ),
        migrations.RemoveField(
            model_name="country",
            name="is_my_country",
        ),
    ]
