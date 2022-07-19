from rest_framework import viewsets, mixins, filters
from src.provider.models import Provider, ProviderDiscount
from src.provider.serializers import ProviderSerializer, ProviderDiscountSerializer
from django_filters.rest_framework import DjangoFilterBackend
from src.provider.services import ProviderFilter
from rest_framework import permissions
from src.core.permissions import IsOwnerOrReadOnly


class ProviderViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProviderFilter
    search_fields = ("cars",)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ProviderDiscountViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ProviderDiscount.objects.all()
    serializer_class = ProviderDiscountSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly,)
