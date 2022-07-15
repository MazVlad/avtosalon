from rest_framework import viewsets, mixins, filters
from car.models import Car
from car.serializers import CarSerializer
from django_filters.rest_framework import DjangoFilterBackend
from car.services import CarFilter
from rest_framework import permissions


class CarViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filterset_class = CarFilter
    search_fields = ["car_type"]
    ordering_fields = ["car_type", "manufacturer"]
    permission_classes = (permissions.IsAuthenticated,)
