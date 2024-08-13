from rest_framework import serializers
from .models import Currency

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class RateRequestSerializer(serializers.Serializer):
    from_currency = serializers.CharField(max_length=3)
    to_currency = serializers.CharField(max_length=3)
