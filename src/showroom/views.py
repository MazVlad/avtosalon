from rest_framework import viewsets, mixins, filters
from src.showroom.models import Showroom, ShowroomDiscount
from src.showroom.serializers import ShowroomSerializer, ShowroomDiscountSerializer
from django_filters.rest_framework import DjangoFilterBackend
from src.showroom.services import ShowroomFilter
from rest_framework import permissions
from src.core.permissions import IsOwnerOrReadOnly


class ShowroomViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filterset_class = ShowroomFilter
    search_fields = ("cars",)
    ordering_fields = (
        "name",
        "cars",
        "location",
    )
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ShowroomDiscountViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ShowroomDiscount.objects.all()
    serializer_class = ShowroomDiscountSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly,
    )
