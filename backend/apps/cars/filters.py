import django_filters as filters

from .models import CarModel


class CarFilter(filters.FilterSet):
    year_gte = filters.NumberFilter('year', 'gte')
    park_name = filters.CharFilter('autopark', 'name__istartswith')

    class Meta:
        model = CarModel
        fields = ('year_gte', 'park_name', 'year', 'model')