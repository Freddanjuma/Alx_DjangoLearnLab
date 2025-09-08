from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', __import__('relationship_app.views').views.register, name='register'),
    path('login/', __import__('relationship_app.views').views.login_view, name='login'),
    path('logout/', __import__('relationship_app.views').views.logout_view, name='logout'),
    path('profile/', __import__('relationship_app.views').views.profile, name='profile'),

    # redirect root ("/") to login
    path('', lambda request: redirect('login')),
]
from django.urls import path
from . import views

app_name = "relationship_app"

urlpatterns = [
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("relationship_app.urls")),  # <-- include our app routes
]
urlpatterns = [
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
    path("redirect-after-login/", views.redirect_after_login, name="redirect_after_login"),
]

