import django_filters
from .models import Book, Author

class BookFilter(django_filters.FilterSet):
    """
    A filterset for the Book model, providing advanced filtering capabilities.
    All filterable fields are explicitly defined to allow for custom lookups
    and to prevent conflicts with django-filter's default Meta.fields processing.
    """
    # Custom CharFilter for 'title', allowing case-insensitive partial matches.
    title = django_filters.CharFilter(lookup_expr='icontains', field_name='title')
    # Custom CharFilter for 'isbn', allowing case-insensitive partial matches.
    isbn = django_filters.CharFilter(lookup_expr='icontains', field_name='isbn')

    # Custom ModelChoiceFilter for 'author', allowing filtering by Author ID.
    author = django_filters.ModelChoiceFilter(queryset=Author.objects.all())
    # Custom CharFilter for 'author_name', allowing case-insensitive partial matches on the author's name.
    author_name = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')

    # Custom DateFilters for published date range queries (greater than or equal to, less than or equal to).
    published_after = django_filters.DateFilter(field_name='published_date', lookup_expr='gte')
    published_before = django_filters.DateFilter(field_name='published_date', lookup_expr='lte')
    # Custom DateFilter for exact published date match.
    published_date = django_filters.DateFilter(field_name='published_date', lookup_expr='exact')


    class Meta:
        model = Book
        # With all desired filter fields explicitly defined above, Meta.fields can be empty.
        # This prevents django-filter from auto-generating conflicting filters.
        fields = []

class AuthorFilter(django_filters.FilterSet):
    """
    A filterset for the Author model, providing filtering by name.
    """
    # Custom CharFilter for 'name', allowing case-insensitive partial matches.
    name = django_filters.CharFilter(lookup_expr='icontains', field_name='name')

    class Meta:
        model = Author
        # Since 'name' is explicitly defined above, Meta.fields can be empty.
        fields = []