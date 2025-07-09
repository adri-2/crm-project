# employees/views.py

from rest_framework import viewsets, filters, permissions
from .models import Employe
from .serializers import EmployeListSerializer, EmployeCRUDSerializer
from apps.users.permissions import IsAdminOrRH, IsEmployeeOwnerOrAdminOrRH # Importe les permissions personnalisées

class EmployeViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les employés.
    - Les admins/RH ont un accès complet (CRUD).
    - Un employé peut voir et modifier son propre profil d'employé.
    - Les autres utilisateurs n'ont pas d'accès direct aux profils d'employés.
    """
    queryset = Employe.objects.all() # Queryset de base
    filter_backends = [filters.SearchFilter, filters.OrderingFilter] # Active la recherche et le tri
    search_fields = [
        'user__first_name', 'user__last_name', 'matricule', 
        'poste__nom', 'statut', 'email_professionnel'
    ] # Champs sur lesquels la recherche est possible
    ordering_fields = ['user__last_name', 'user__first_name', 'matricule', 'date_embauche', 'statut'] # Champs sur lesquels le tri est possible

    def get_permissions(self):
        """
        Retourne l'ensemble des permissions que cette vue requiert en fonction de l'action.
        """
        if self.action in ['list', 'create']:
            # Seuls les admins et RH peuvent lister et créer des employés
            self.permission_classes = [IsAdminOrRH]
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            # Pour les détails, mise à jour et suppression :
            # Admin/RH ou le propriétaire de l'objet Employe
            self.permission_classes = [IsEmployeeOwnerOrAdminOrRH]
        else:
            # Pour toute autre action non spécifiée, l'utilisateur doit être authentifié
            self.permission_classes = [permissions.IsAuthenticated] 

        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        """
        Retourne le serializer approprié en fonction de l'action de la vue.
        - Pour la liste, utilise EmployeListSerializer.
        - Pour les autres actions, utilise EmployeCRUDSerializer.
        """
        if self.action == 'list':
            return EmployeListSerializer
        return EmployeCRUDSerializer
    
    def get_queryset(self):
        """
        Restreint le queryset en fonction des permissions de l'utilisateur authentifié.
        - Les admins/RH voient tous les employés.
        - Les employés (rôle 'user' sans être admin/rh) ne voient que leur propre profil d'employé.
        - Les utilisateurs non authentifiés ou sans rôle spécifique ne voient rien.
        """
        user = self.request.user
        if user.is_authenticated:
            # Les superutilisateurs, admins et RH voient tous les employés
            if user.is_staff or user.role in ["admin", "rh"]:
                return Employe.objects.all()
            # Un utilisateur authentifié qui a un profil d'employé ne voit que son propre profil
            elif hasattr(user, 'employe'):
                return Employe.objects.filter(user=user)
        # Par défaut (utilisateur non authentifié ou sans accès), retourne un queryset vide
        return Employe.objects.none()