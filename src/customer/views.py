from rest_framework import viewsets, mixins
from src.customer.models import Customer
from src.customer.serializers import CustomerSerializer
from rest_framework import permissions
from src.core.permissions import IsOwnerOrReadOnly


class CustomerViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly,
    )
