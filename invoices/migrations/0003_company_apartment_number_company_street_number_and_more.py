# Generated by Django 4.0.1 on 2022-01-11 18:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20210409_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='apartment_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Apartment number'),
        ),
        migrations.AddField(
            model_name='company',
            name='street_number',
            field=models.CharField(default=1, max_length=10, verbose_name='Street number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(default=1, max_length=60, verbose_name='City'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='default_currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='invoices.currency', verbose_name='Default currency'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='nip',
            field=models.CharField(default=1, max_length=12, verbose_name='NIP'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='street',
            field=models.CharField(default=1, max_length=100, verbose_name='Street'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='zip_code',
            field=models.CharField(default=1, max_length=10, verbose_name='ZIP Code'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='invoices.company', verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='create_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Create date'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='invoices.currency', verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(default=1, max_length=30, verbose_name='Invoice number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_type',
            field=models.IntegerField(choices=[(0, 'Sales'), (1, 'Purchase')], default=1, verbose_name='Invoice type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Payment date'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_method',
            field=models.IntegerField(choices=[(0, 'Transfer'), (1, 'Cash')], default=1, verbose_name='Payment method'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='sale_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Sale date'),
        ),
        migrations.AlterField(
            model_name='item',
            name='vat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='invoices.vatrate', verbose_name='Vat'),
        ),
    ]
