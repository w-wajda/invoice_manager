from rest_framework import serializers

from currencies.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("id", "code", "user")
        extra_kwargs = {
            "code": {"validators": []},
        }
