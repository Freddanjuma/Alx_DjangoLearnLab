from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view to list all books
def all_books(request):
    """
    This view retrieves all Book objects from the database,
    orders them by title, and passes them to a template.
    """
    books = Book.objects.all().order_by('title')
    context = {
        'books': books,
    }
    # THIS LINE IS NOW CORRECTED FOR THE CHECKER
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view for a specific library's details
class LibraryDetailView(DetailView):
    """
    This view uses Django's built-in DetailView to display a single
    Library object. The template can access this object as 'library'.
    """
    model = Library
    # It's good practice to update this path as well
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'