from rest_framework import serializers
from src.provider.models import Provider, ProviderDiscount


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"


class ProviderDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderDiscount
        fields = "__all__"
