from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Permission to only allow owners of an object to change it."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user