# employees/views.py

from rest_framework import generics, filters, permissions
from .models import Employe
from .serializers import EmployeListSerializer, EmployeCRUDSerializer
from apps.users.permissions import IsAdminOrRH, IsEmployeeOwnerOrAdminOrRH # Importe les permissions personnalisées

from apps.users.models import User
class EmployeListCreateAPIView(generics.ListCreateAPIView):
    """
    Vue pour lister et créer des employés.
    - Les admins/RH peuvent lister et créer.
    - Les employés peuvent lister leur propre profil.
    """
    permission_classes = [permissions.IsAuthenticated] # Base: authentifié

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'user__first_name', 'user__last_name', 'matricule', 
        'poste__nom', 'statut', 'email_professionnel'
    ]
    ordering_fields = ['user__last_name', 'user__first_name', 'matricule', 'date_embauche', 'statut', 'created_at']

    def get_queryset(self):
        """
        Restreint le queryset en fonction des permissions de l'utilisateur authentifié.
        - Les admins/RH voient tous les employés.
        - Les employés (rôle 'user' sans être admin/rh) ne voient que leur propre profil d'employé.
        """
        user = self.request.user
        if user.is_authenticated:
            if user.is_staff or user.role in ["admin", "rh"]:
                return Employe.objects.all().order_by('user__last_name', 'user__first_name')
            elif hasattr(user, 'employe'):
                return Employe.objects.filter(user=user).order_by('user__last_name', 'user__first_name')
        return Employe.objects.none()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EmployeCRUDSerializer # Pour la création
        return EmployeListSerializer # Pour la liste

    def get_permissions(self):
        # Pour la création, seuls les admins/RH sont autorisés
        if self.request.method == 'POST':
            return [IsAdminOrRH()]
        # Pour la liste, la permission est gérée par get_queryset et IsAuthenticated
        return [permissions.IsAuthenticated()]


class EmployeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vue pour récupérer, mettre à jour et supprimer un employé spécifique.
    - Les admins/RH ont un accès complet.
    - Un employé peut voir et modifier son propre profil.
    """
    queryset = Employe.objects.all()
    serializer_class = EmployeCRUDSerializer
    permission_classes = [IsEmployeeOwnerOrAdminOrRH] # Permission au niveau de l'objet

    def get_queryset(self):
        """
        Assure que l'utilisateur ne peut accéder qu'à son propre profil s'il n'est pas admin/RH.
        """
        user = self.request.user
        if user.is_authenticated and (user.is_staff or user.role in ["admin", "rh"]):
            return Employe.objects.all()
        elif user.is_authenticated and hasattr(user, 'employe'):
            return Employe.objects.filter(user=user)
        return Employe.objects.none()
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
            pass
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            # Pour les détails, mise à jour et suppression :
            # Admin/RH ou le propriétaire de l'objet Employe
            self.permission_classes = [IsEmployeeOwnerOrAdminOrRH]
            pass
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