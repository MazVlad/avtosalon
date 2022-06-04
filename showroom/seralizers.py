from rest_framework import serializers
from .models import *



class CarManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarManufacturer
        fields = ('name',)


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'



class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = '__all__'
        read_only_fields = ('balance',)


class ShowroomDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowroomDiscount
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ('balance',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ProviderDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderDiscount
        fields = '__all__'





