# Generated by Django 4.2.5 on 2024-01-15 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("invoices", "0022_alter_correctioninvoicerelation_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="correctioninvoicerelation",
            options={"verbose_name_plural": "relacja faktur korygujących"},
        ),
        migrations.AddField(
            model_name="invoice",
            name="net_amount",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=9, verbose_name="Net amount"
            ),
        ),
        migrations.AlterField(
            model_name="correctioninvoicerelation",
            name="correction_invoice",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="correction_invoice_relation",
                to="invoices.invoice",
                verbose_name="Faktura korygująca",
            ),
        ),
    ]