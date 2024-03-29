from rest_framework import serializers

from invoices.models import CorrectionInvoiceRelation, Invoice
from items.models import Item
from items.serializers import ItemSerializer


class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Invoice
        fields = [
            "company",
            "invoice_type",
            "payment_method",
            "create_date",
            "sale_date",
            "payment_date",
            "account_number",
            "invoice_number",
            "currency",
            "items",
            "is_recurring",
            "is_last_day",
            "is_settled",
            "is_paid",
            "settlement_date",
            "client",
            "person",
            "invoice_file",
            "net_amount",
            "gross_amount",
        ]

    def create(self, validated_data):
        items = validated_data.pop("items")
        invoice = Invoice.objects.create(**validated_data)

        for item in items:
            name = item["name"]
            pkwiu = item["pkwiu"]
            amount = item["amount"]
            net_price = item["net_price"]
            vat = item["vat"]
            Item.objects.create(
                name=name,
                amount=amount,
                pkwiu=pkwiu,
                net_price=net_price,
                vat=vat,
                invoice=invoice,
            )

        return invoice

    def update(self, instance: Invoice, validated_data):
        items = validated_data.pop("items", [])

        for key, values in validated_data.items():
            setattr(instance, key, values)

        for item in items:
            item_id = item.pop("id")
            instance_item = Item.objects.get(pk=item_id)

            for key, values in item.items():
                setattr(instance_item, key, values)

            instance_item.save()

        instance.save()
        return instance


class CorrectionInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorrectionInvoiceRelation
        fields = [
            "invoice",
            "correction_invoice",
        ]
