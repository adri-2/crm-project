# users/permissions.py

from rest_framework import permissions

class IsAdminOrRH(permissions.BasePermission):
    """
    Permission personnalisée : Autorise l'accès uniquement aux utilisateurs avec le rôle 'admin' ou 'rh',
    ou aux superutilisateurs (is_staff).
    """
    def has_permission(self, request, view):
        # Un utilisateur doit être authentifié pour avoir un rôle
        if not request.user or not request.user.is_authenticated:
            return False
        # Autorise si l'utilisateur est un superutilisateur ou a le rôle admin/rh
        return request.user.is_staff or request.user.role in ["admin", "rh"]

class IsAdminOrManagerOrRH(permissions.BasePermission):
    """
    Permission personnalisée : Autorise l'accès aux utilisateurs avec le rôle 'admin', 'rh', ou 'manager',
    ou aux superutilisateurs (is_staff).
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        # Autorise si l'utilisateur est un superutilisateur ou a le rôle admin/rh/manager
        return request.user.is_staff or request.user.role in ["admin", "rh", "manager"]

class IsEmployeeOwnerOrAdminOrRH(permissions.BasePermission):
    """
    Permission au niveau de l'objet pour les profils Employe :
    - Les admins/RH ont un accès complet.
    - Un employé peut voir et modifier son propre profil Employe.
    """
    def has_object_permission(self, request, view, obj):
        # Les admins et les RH ont toujours un accès complet
        if request.user.is_staff or request.user.role in ["admin", "rh"]:
            return True
        
        # Si la requête est une lecture (GET, HEAD, OPTIONS), l'authentification est suffisante pour son propre profil
        if request.method in permissions.SAFE_METHODS:
            return obj.user == request.user
        
        # Pour les opérations de modification (PUT, PATCH, DELETE), seul le propriétaire peut modifier
        return obj.user == request.user

class IsEncadreurOrAdminOrRH(permissions.BasePermission):
    """
    Permission au niveau de l'objet pour les stagiaires :
    - Les admins/RH ont un accès complet.
    - Un encadreur peut voir et modifier les stagiaires qu'il encadre.
    """
    def has_object_permission(self, request, view, obj):
        # Les admins et les RH ont toujours un accès complet
        if request.user.is_staff or request.user.role in ["admin", "rh"]:
            return True
        
        # Si la requête est une lecture (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            # Vérifie si l'utilisateur authentifié est un employé et est l'encadreur du stagiaire
            return hasattr(request.user, 'employe') and obj.encadreur == request.user.employe
        
        # Pour les opérations de modification (PUT, PATCH, DELETE), seul l'encadreur peut modifier
        return hasattr(request.user, 'employe') and obj.encadreur == request.user.employe

class IsCandidatOwnerOrAdminOrManagerOrRH(permissions.BasePermission):
    """
    Permission au niveau de l'objet pour les candidatures :
    - Les admins/RH/managers ont un accès complet.
    - Un employé peut voir ses propres candidatures (basé sur l'email personnel).
    """
    def has_object_permission(self, request, view, obj):
        # Les admins/RH/managers ont toujours un accès complet
        if request.user.is_staff or request.user.role in ["admin", "rh", "manager"]:
            return True
        
        # Un employé authentifié peut voir sa propre candidature si l'email correspond
        # Note: Ceci est une simplification. Dans un système réel, un candidat pourrait être lié à un `User`.
        if request.user.is_authenticated and hasattr(request.user, 'employe'):
            return obj.email == request.user.employe.email_personnel
        
        return False



# from rest_framework import permissions

# class IsAdminRHManager(permissions.BasePermission):
#     """
#     Autorise uniquement les admin, RH et managers à faire du CRUD.
#     """
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role in ['admin', 'rh', 'manager']

# class IsSelfOrAdminRHManager(permissions.BasePermission):
#     """
#     Les stagiaires/employés ne voient que leur propre fiche.
#     """
#     def has_object_permission(self, request, view, obj):
#         if request.user.role in ['admin', 'rh', 'manager']:
#             return True
#         return obj == request.user