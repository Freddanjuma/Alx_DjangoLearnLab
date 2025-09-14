from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser # Import CustomUser from accounts.models

class CustomUserAdmin(UserAdmin):
    # Correctly links this admin to your CustomUser model
    # This line can be explicit, or UserAdmin infers it if you override get_user_model()
    # model = CustomUser # (Optional, UserAdmin usually infers this)

    # Fields shown in the list view of the admin
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")

    # Fields shown when adding/changing a user - this merges with default UserAdmin fieldsets
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Fields", {"fields": ("date_of_birth", "profile_photo")}),
    )
    # Fields shown when adding a *new* user - this merges with default UserAdmin add_fieldsets
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Custom Fields", {"fields": ("date_of_birth", "profile_photo")}),
    )

# Register your CustomUser model with your CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)