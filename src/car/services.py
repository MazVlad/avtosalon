from django_filters import rest_framework as filters
from src.car.models import Car


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class CarFilter(filters.FilterSet):
    manufacturer = CharFilterInFilter(field_name="manufacturer__name", lookup_expr="in")
    car_type = filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Car
        fields = ["manufacturer", "car_type", "year"]
