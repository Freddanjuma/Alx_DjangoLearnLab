from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

def list_books(request):
    """
    This view retrieves all Book objects from the database and
    passes them to the namespaced template.
    """
    books = Book.objects.all().order_by('title')
    context = {'books': books}
    # This path is now correct
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    """
    This view uses DetailView to display a single Library object.
    """
    model = Library
    # This path is also now correct
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'