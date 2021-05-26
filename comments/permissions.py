from rest_framework import permissions


class IsStandardUser(permissions.BasePermission):
    message = "you do not have permission to perform this action."

    def has_permission(self, request, view):
        if not request.user.is_staff and not request.user.is_superuser:
            return True

        return False
