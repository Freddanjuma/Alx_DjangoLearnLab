import django_filters
from .models import Book, Author

class BookFilter(django_filters.FilterSet):
    """
    A filterset for the Book model, providing filtering capabilities.
    All filterable fields are explicitly defined here to avoid Meta.fields conflicts.
    """
    # Char filters
    title = django_filters.CharFilter(lookup_expr='icontains', field_name='title')
    isbn = django_filters.CharFilter(lookup_expr='icontains', field_name='isbn') # Explicit filter for ISBN

    # Foreign Key filter
    author = django_filters.ModelChoiceFilter(queryset=Author.objects.all()) # Filter by Author object
    author_name = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains') # Filter by Author name

    # Date filters for range
    published_after = django_filters.DateFilter(field_name='published_date', lookup_expr='gte')
    published_before = django_filters.DateFilter(field_name='published_date', lookup_expr='lte')
    # Exact date filter (if desired for ?published_date=YYYY-MM-DD)
    published_date = django_filters.DateFilter(field_name='published_date', lookup_expr='exact')


    class Meta:
        model = Book
        # With all fields explicitly defined above, Meta.fields can be empty or omitted.
        # This prevents django-filter from trying to auto-generate filters for these fields
        # and conflicting with our explicit definitions.
        fields = [] # <-- Make this an empty list
        # OR you can just remove the 'fields' attribute completely from Meta

class AuthorFilter(django_filters.FilterSet):
    """
    A filterset for the Author model.
    """
    name = django_filters.CharFilter(lookup_expr='icontains', field_name='name')

    class Meta:
        model = Author
        # Similarly, for AuthorFilter, since 'name' is explicitly defined:
        fields = [] # <-- Make this an empty list or omit