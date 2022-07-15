from rest_framework import serializers
from showroom.models import Showroom, ShowroomDiscount


class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = "__all__"
        read_only_fields = ("balance",)


class ShowroomDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowroomDiscount
        fields = "__all__"
