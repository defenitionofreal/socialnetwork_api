from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    # read-only permissons for any
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # write permissions allowed to author
        return obj.author == request.user

