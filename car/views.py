from django.shortcuts import render
from rest_framework import viewsets,mixins

from car.models import Car,CarManufacturer
from car.serializers import CarManufacturerSerializer,CarSerializer



class CarManufacturerViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = CarManufacturer.objects.all()
    serializer_class = CarManufacturerSerializer



class CarViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
