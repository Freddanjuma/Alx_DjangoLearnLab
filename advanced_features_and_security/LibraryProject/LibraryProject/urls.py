# LibraryProject/LibraryProject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # Your existing include for relationship_app
    path('books/', include('bookshelf.urls')),   # <-- ADD THIS NEW LINE at the bottom of urlpatterns
]