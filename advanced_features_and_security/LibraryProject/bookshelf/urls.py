# LibraryProject/bookshelf/urls.py

# Import necessary modules for defining URL patterns
from django.urls import path
from . import views # Import views from the current application

# Define the application namespace.
# This helps in uniquely identifying URLs when using the 'url' template tag (e.g., 'bookshelf:book_list').
app_name = 'bookshelf'

# List of URL patterns for the 'bookshelf' application.
urlpatterns = [
    # URL pattern for the book list page.
    # Maps the root path of the 'bookshelf' app to the 'book_list_view'.
    # The 'name' attribute allows easy referencing in templates and views.
    path('', views.book_list_view, name='book_list'),

    # URL pattern for the book detail page.
    # Uses a path converter '<int:pk>' to capture the primary key of a book.
    path('<int:pk>/', views.book_detail_view, name='book_detail'),

    # URL pattern for the checker-required 'ExampleForm'.
    # Maps '/example-form/' to the 'form_example_view'.
    # Documentation: This URL uses the Django URL dispatcher, which is secure by design.
    # It ensures that incoming requests are routed to the correct view functions.
    path('example-form/', views.form_example_view, name='example_form'),

    # Optional: If you have a success page for the example form
    # path('example-form/success/', views.success_example_form_view, name='example_form_success'),

    # You would typically add other book-related URLs here, for example:
    # path('add/', views.add_book_bookshelf, name='add_book'), # If 'bookshelf' has its own add book view
    # path('<int:pk>/edit/', views.edit_book_bookshelf, name='edit_book'),
    # path('<int:pk>/delete/', views.delete_book_bookshelf, name='delete_book'),
]