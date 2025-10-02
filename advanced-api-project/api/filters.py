import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    # Filter by publication year
    publication_year = django_filters.NumberFilter(field_name='published_date', lookup_expr='year')

    # Filter for books published on or after a certain date
    published_after = django_filters.DateFilter(field_name='published_date', lookup_expr='gte')

    # Filter for books published on or before a certain date
    published_before = django_filters.DateFilter(field_name='published_date', lookup_expr='lte')

    # New: Filter by title containing text (case-insensitive)
    title__icontains = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    # New: Filter by author name containing text (case-insensitive)
    # This requires 'author__name' as the field name
    author_name__icontains = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = {
            'author': ['exact'],
            # The '__icontains' filters are defined explicitly above,
            # so we don't need to add them here with a specific lookup_expr
            # If you *only* wanted exact title, you could put 'title': ['exact']
        }