import django_filters
from .models import Book, Author

class BookFilter(django_filters.FilterSet):
    """
    A filterset for the Book model, providing advanced filtering capabilities.
    Configured with specific filters for exact matches, partial matches, and date ranges.
    """
    title = django_filters.CharFilter(lookup_expr='icontains', field_name='title', help_text="Case-insensitive partial match on book title.")
    isbn = django_filters.CharFilter(lookup_expr='icontains', field_name='isbn', help_text="Case-insensitive partial match on ISBN.")

    # Filter by Author ID
    author = django_filters.ModelChoiceFilter(queryset=Author.objects.all(), help_text="Filter by Author ID.")
    # Filter by Author's Name (case-insensitive partial match)
    author_name = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains', help_text="Case-insensitive partial match on author's name.")

    # Date range filters for published_date
    published_after = django_filters.DateFilter(field_name='published_date', lookup_expr='gte', help_text="Filter books published on or after a specific date (YYYY-MM-DD).")
    published_before = django_filters.DateFilter(field_name='published_date', lookup_expr='lte', help_text="Filter books published on or before a specific date (YYYY-MM-DD).")
    published_date = django_filters.DateFilter(field_name='published_date', lookup_expr='exact', help_text="Filter books published on an exact date (YYYY-MM-DD).")

    # Explicit filter for publication_year 
    publication_year = django_filters.NumberFilter(field_name='published_date__year', lookup_expr='exact', help_text="Filter books published in a specific year (YYYY).")

    class Meta:
        model = Book
        # All filterable fields are defined explicitly above to leverage custom lookups and help_text.
        fields = []

class AuthorFilter(django_filters.FilterSet):
    """
    A filterset for the Author model, providing filtering by name.
    """
    name = django_filters.CharFilter(lookup_expr='icontains', field_name='name', help_text="Case-insensitive partial match on author's name.")

    class Meta:
        model = Author
        fields = []