from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='relationship_app:login'), name='logout'),
    path('profile/', views.profile, name='profile'),
    
    # Add your other app URLs here (books, etc.)
    # path('books/', include('relationship_app.book_urls')),
]
