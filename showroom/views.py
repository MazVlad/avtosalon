from rest_framework import viewsets,mixins
from showroom.models import Showroom,ShowroomDiscount
from showroom.serializers import ShowroomSerializer,ShowroomDiscountSerializer


class ShowroomViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomSerializer


class ShowroomDiscountViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = ShowroomDiscount.objects.all()
    serializer_class = ShowroomDiscountSerializer

