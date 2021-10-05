import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Title')
    author = django_filters.CharFilter(field_name='author__full_name', lookup_expr='icontains', label='Author')
    order = django_filters.ChoiceFilter(method='by_ascending_order_release', label='Order',
     choices=(
         ('ASC', 'by ascending'),
         ('DESC', 'by descending'))
        )

    class Meta:
        model = Book
        fields = ['title', 'author', 'order']

    def by_ascending_order_release(self, queryset, name, value):
        query = {
            'ASC': 'date_of_release',
            'DESC': '-date_of_release'
        }
        return queryset.order_by(query[value])