from django.shortcuts import render
from rest_framework import viewsets, mixins
from provider.models import Provider,ProviderDiscount
from provider.serializers import ProviderSerializer,ProviderDiscountSerializer


class ProviderViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderDiscountViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = ProviderDiscount.objects.all()
    serializer_class = ProviderDiscountSerializer
