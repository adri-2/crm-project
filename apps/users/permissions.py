from rest_framework import permissions

class IsAdminRHManager(permissions.BasePermission):
    """
    Autorise uniquement les admin, RH et managers à faire du CRUD.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['admin', 'rh', 'manager']

class IsSelfOrAdminRHManager(permissions.BasePermission):
    """
    Les stagiaires/employés ne voient que leur propre fiche.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.role in ['admin', 'rh', 'manager']:
            return True
        return obj == request.user