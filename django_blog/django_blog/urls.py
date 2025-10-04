# django_blog/django_blog/urls.py

from django.contrib import admin
from django.urls import path, include # <--- 'include' must be imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # <--- This points to the app's new urls.py
]