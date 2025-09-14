from django.contrib import admin
from .models import UserProfile # Import UserProfile (and any other models like Librarian, Library)

# Register your models here.
admin.site.register(UserProfile)
# If you have other models in relationship_app/models.py, register them too:
# admin.site.register(Librarian)
# admin.site.register(Library)