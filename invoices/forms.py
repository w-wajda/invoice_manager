from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

from companies.models import Company
from currencies.models import Currency
from invoices.models import Invoice
from persons.models import Person

invoice_number_validator = RegexValidator(
    r"^[0-9]+/[0-9]{4}$",
    _("Enter invoice number in numbers only in format number/yyyy"),
)

account_number_validator = RegexValidator(
    r"^[0-9A-Z ]{15,32}$",
    _("Enter account number with minimum 15 character without special characters"),
)


class InvoiceSellForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            "invoice_number",
            "company",
            "client",
            "create_date",
            "sale_date",
            "payment_date",
            "payment_method",
            "currency",
            "account_number",
            "is_recurring",
        ]

    def __init__(self, *args, current_user, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_user = current_user
        self.fields["company"].queryset = Company.objects.filter(
            user=current_user, is_my_company=True
        ).order_by("name")
        self.fields["client"].queryset = Company.objects.filter(
            user=current_user, is_my_company=False
        ).order_by("name")
        self.fields["currency"].queryset = Currency.objects.filter(
            user=current_user
        ).order_by("code")
        invoice_number_field: forms.CharField = self.fields["invoice_number"]
        invoice_number_field.validators = [invoice_number_validator]

        account_number_field: forms.CharField = self.fields["account_number"]
        account_number_field.validators = [account_number_validator]

        for field in self.Meta.fields:
            if field == "is_recurring":
                continue
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].required = True

    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get("invoice_number")
        invoice = Invoice.objects.filter(
            invoice_number=invoice_number,
            company__user=self.current_user,
        )

        if self.instance.pk:
            invoice = invoice.exclude(pk=self.instance.pk)

        if invoice.exists():
            raise forms.ValidationError(_("Invoice number already exists"))

        return invoice_number


class InvoiceSellPersonForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            "invoice_number",
            "company",
            "person",
            "create_date",
            "sale_date",
            "payment_date",
            "payment_method",
            "currency",
            "account_number",
            "is_recurring",
        ]

    def __init__(self, current_user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_user = current_user

        self.fields["company"].queryset = Company.objects.filter(
            user=current_user, is_my_company=True
        ).order_by("name")
        self.fields["person"].queryset = Person.objects.filter(user=current_user)
        self.fields["currency"].queryset = Currency.objects.filter(
            user=current_user
        ).order_by("code")

        invoice_number_field: forms.CharField = self.fields["invoice_number"]
        invoice_number_field.validators = [invoice_number_validator]

        account_number_field: forms.CharField = self.fields["account_number"]
        account_number_field.validators = [account_number_validator]

        for field in self.Meta.fields:
            if field == "is_recurring":
                continue
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].required = True

    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get("invoice_number")
        invoice = Invoice.objects.filter(
            invoice_number=invoice_number,
            company__user=self.current_user,
        )

        if self.instance.pk:
            invoice = invoice.exclude(pk=self.instance.pk)

        if invoice.exists():
            raise forms.ValidationError(_("Invoice number already exists"))

        return invoice_number


class InvoiceBuyForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            "invoice_number",
            "company",
            "sale_date",
            "payment_date",
            "settlement_date",
            "invoice_file",
        ]

    def __init__(self, *args, current_user, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_user = current_user
        self.fields["company"].queryset = Company.objects.filter(
            user=current_user, is_my_company=True
        ).order_by("name")

        for field in self.Meta.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].required = True

    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get("invoice_number")
        invoice = Invoice.objects.filter(
            invoice_number=invoice_number,
            company__user=self.current_user,
        )
        if self.instance.pk:
            invoice = invoice.exclude(pk=self.instance.pk)

        if invoice.exists():
            raise forms.ValidationError(_("Invoice number already exists"))

        return invoice_number


class InvoiceFilterForm(forms.Form):
    invoice_number = forms.CharField(label=_("Invoice number"), required=False)
    invoice_type = forms.ChoiceField(
        label=_("Invoice type"), required=False, choices=Invoice.INVOICE_TYPES
    )
    client = forms.CharField(label=_("Client"), required=False)
    company = forms.CharField(label=_("Company"), required=False)

    invoice_number.widget.attrs.update({"class": "form-control"})
    invoice_type.widget.attrs.update({"class": "form-select"})
    client.widget.attrs.update({"class": "form-control"})
    company.widget.attrs.update({"class": "form-control"})

    def get_filtered_invoices(self, invoices_list):
        invoice_number = self.cleaned_data["invoice_number"]
        invoice_type = self.cleaned_data["invoice_type"]
        company = self.cleaned_data["company"]
        client = self.cleaned_data["client"]

        if invoice_number:
            invoices_list = invoices_list.filter(
                invoice_number__contains=invoice_number
            )
        if invoice_type:
            invoices_list = invoices_list.filter(invoice_type=invoice_type)
        if client:
            invoices_list = invoices_list.filter(client__name__icontains=client)
        if company:
            invoices_list = invoices_list.filter(company__name__icontains=company)

        return invoices_list
