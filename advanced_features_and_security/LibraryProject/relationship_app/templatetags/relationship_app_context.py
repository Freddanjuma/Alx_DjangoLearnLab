# relationship_app/templatetags/relationship_app_context.py
from django.contrib.auth.models import Group

def user_groups_processor(request):
    """
    Adds user group booleans (is_librarian, is_member) to the template context.
    """
    is_librarian = False
    is_member = False

    if request.user.is_authenticated:
        # Check for superuser first to short-circuit if applicable, as superusers often have all access
        if request.user.is_superuser:
            is_librarian = True # A superuser might be considered a 'librarian' for access purposes
            is_member = True    # A superuser might be considered a 'member' for access purposes
        else:
            # Optimized query: get group IDs once if groups are frequently checked
            user_group_names = request.user.groups.values_list('name', flat=True)

            if 'Librarians' in user_group_names:
                is_librarian = True
            if 'Members' in user_group_names:
                is_member = True

    return {
        'is_librarian': is_librarian,
        'is_member': is_member,
    }