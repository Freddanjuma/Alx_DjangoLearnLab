# relationship_app/admin.py (Only UserProfile admin)
from django.contrib import admin
from .models import UserProfile # Import ONLY models from this app

admin.site.register(UserProfile)
# If you have other models in relationship_app, register them here:
# from .models import Librarian, Library
# admin.site.register(Librarian)
# admin.site.register(Library)