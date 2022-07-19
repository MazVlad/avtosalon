from rest_framework import serializers
from src.customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ("balance",)
