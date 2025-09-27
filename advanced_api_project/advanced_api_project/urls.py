# advanced_api_project/advanced_api_project/urls.py

from django.contrib import admin
from django.urls import path, include # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # Include URLs from your 'api' app
]