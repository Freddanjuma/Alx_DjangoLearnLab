from django.contrib import admin
from django.urls import path, include  # Make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This is the new line that connects your app's URLs
    path('app/', include('relationship_app.urls')), 
]