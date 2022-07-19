from django_filters import rest_framework as filters
from src.provider.models import Provider


class ProviderFilter(filters.FilterSet):
    class Meta:
        model = Provider
        fields = ["name", "cars", "year_of_foundation"]
