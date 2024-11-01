from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from items.admin import ItemInline

from .models import CorrectionInvoiceRelation, Invoice, Year


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        "invoice_number",
        "company",
        "client",
        "person",
        "payment_date",
        "net_amount",
        "currency",
        "is_recurring",
        "is_settled",
        "is_paid",
    )
    list_filter = (
        "is_recurring",
        "is_settled",
        "company__name",
        "invoice_type",
        "payment_date",
        "is_paid",
    )
    search_fields = ("invoice_number", "company__name")
    inlines = [ItemInline]
    fieldsets = (
        (
            _("Basic information"),
            {
                "fields": (
                    ("invoice_number", "invoice_type"),
                    ("company", "client", "person"),
                    ("create_date", "sale_date", "payment_date"),
                )
            },
        ),
        (
            _("Advanced options"),
            {
                "fields": (
                    ("payment_method", "currency"),
                    ("account_number", "is_paid"),
                )
            },
        ),
        (
            _("Additional options"),
            {
                "fields": (
                    ("is_recurring", "is_last_day"),
                    ("settlement_date", "is_settled"),
                    ("invoice_file",),
                )
            },
        ),
    )


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = (
        "year",
        "user",
    )


@admin.register(CorrectionInvoiceRelation)
class CorrectionInvoiceRelationAdmin(admin.ModelAdmin):
    list_display = (
        "invoice",
        "correction_invoice",
    )
