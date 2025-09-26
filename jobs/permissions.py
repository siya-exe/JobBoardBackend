# jobs/permissions.py
from rest_framework.permissions import BasePermission

class IsAdminUserRole(BasePermission):
    """
    Allows access only to authenticated users with role='admin'.
    """

    def has_permission(self, request, view):
        # Ensure user is authenticated first
        if not request.user or not request.user.is_authenticated:
            return False
        # Check role safely
        return getattr(request.user, "role", None) == "admin"
