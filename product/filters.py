import django_filters
from django_filters import rest_framework

from .models import Product

class ProductFilter(django_filters.FilterSet):
    price_from = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_to = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    title = rest_framework.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ('title', 'categories', 'price_from', 'price_to')