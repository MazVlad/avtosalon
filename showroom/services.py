from django_filters import rest_framework as filters
from showroom.models import Showroom


class ShowroomFilter(filters.FilterSet):
    class Meta:
        model = Showroom
        fields = ['name','location','cars']







