from django_filters import rest_framework as filters
from .models import *



class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class CarFilter(filters.FilterSet):
    manufacturer = CharFilterInFilter(field_name='manufacturer__name', lookup_expr='in')
    car_type = filters.CharFilter(lookup_expr='iexact')


    class Meta:
        model = Car
        fields = ['manufacturer', 'car_type','year']


class ShowroomFilter(filters.FilterSet):
    class Meta:
        model = Showroom
        fields = ['name','location','cars']


class ProviderFilter(filters.FilterSet):
    class Meta:
        model = Provider
        fields = ['name','cars','year_of_foundation']




