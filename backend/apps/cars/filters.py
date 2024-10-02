from django_filters import rest_framework as filters

from apps.cars.choices import BodyTypeChoice


#examples
class CarFilter(filters.FilterSet):
    year_lt = filters.NumberFilter('year', 'lt')
    year_range = filters.RangeFilter('year')
    year_in = filters.BaseInFilter('year')
    body_type = filters.ChoiceFilter('body_type', choices=BodyTypeChoice.choices)
    model_endswith = filters.CharFilter('model', 'endswith')
    order = filters.OrderingFilter(fields=(
        'id',
        'model',
        'price'
    ))