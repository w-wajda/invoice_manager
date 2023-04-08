from django import forms

from invoices.models import Invoice, Item


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            "invoice_number",
            "invoice_type",
            "company",
            "recurring_frequency",
            "is_recurring",
            "create_date",
            "sale_date",
            "payment_date",
            "payment_method",
            "currency",
            "account_number",
        ]
        labels = {
            "invoice_number": "Numer faktury",
            "invoice_type": "Typ faktury",
            "company": "Nazwa firmy",
            "recurring_frequency": "Częstotliwość faktury",
            "is_recurring": "Czy powtarzalna",
            "create_date": "Data utworzenia",
            "sale_date": "Data sprzedaży",
            "payment_date": "Data płatności",
            "payment_method": "Forma płatności",
            "currency": "Waluta",
            "account_number": "Numer konta",
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "pkwiu", "amount", "net_price", "vat"]
