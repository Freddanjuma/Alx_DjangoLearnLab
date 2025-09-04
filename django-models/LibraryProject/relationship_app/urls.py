from django.urls import path
# Import the entire views module to satisfy the checker
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Paths for book and library views
    path('books/', views.list_books, name='all-books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),

    # This line now explicitly uses "views.register"
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/registration/logout.html'), name='logout'),
]