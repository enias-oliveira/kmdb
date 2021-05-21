from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    message = "you do not have permission to perform this action."

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        return False
