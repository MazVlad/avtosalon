from django.shortcuts import render
from rest_framework import viewsets,mixins,filters

from car.models import Car,CarManufacturer
from car.serializers import CarManufacturerSerializer,CarSerializer
from django_filters.rest_framework import DjangoFilterBackend
from car.services import CarFilter



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
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = CarFilter
    search_fields = ['car_type']
    ordering_fields = ['car_type', 'manufacturer']
