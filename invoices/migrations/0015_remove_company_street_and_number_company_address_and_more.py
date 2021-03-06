# Generated by Django 4.0.1 on 2022-01-14 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0014_rename_street_company_street_and_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='street_and_number',
        ),
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(default=1, max_length=100, verbose_name='Address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vatrate',
            name='rate',
            field=models.PositiveIntegerField(unique=True, verbose_name='Rate'),
        ),
    ]
