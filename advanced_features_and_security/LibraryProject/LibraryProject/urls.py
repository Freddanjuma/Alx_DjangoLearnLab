# LibraryProject/LibraryProject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView # <--- Make sure this is imported!

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add the root path redirect. This MUST come before any other empty path includes.
    path('', RedirectView.as_view(url='login/', permanent=False)), # Redirects root to login page

    # Include your application's URL configurations
    path('', include('relationship_app.urls')),
    path('books/', include('bookshelf.urls')), # This line is now correctly placed and uncommented
]