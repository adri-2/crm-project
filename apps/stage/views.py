# stage/views.py

from rest_framework import viewsets, filters, permissions
from .models import Stagiaire, PeriodeStage
from .serializers import (
    StagiaireListSerializer, StagiaireCRUDSerializer,
    PeriodeStageListSerializer, PeriodeStageCRUDSerializer
)
from apps.users.permissions import IsAdminOrRH, IsEncadreurOrAdminOrRH # Importe les permissions personnalisées

class StagiaireViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les stagiaires.
    - Les admins/RH ont un accès complet (CRUD).
    - Les encadreurs (employés) ne peuvent voir que les stagiaires qu'ils encadrent et les modifier.
    """
    queryset = Stagiaire.objects.all() # Queryset de base
    filter_backends = [filters.SearchFilter, filters.OrderingFilter] # Active la recherche et le tri
    search_fields = [
        'first_name', 'last_name', 'matricule', 'poste__nom', 
        'encadreur__user__first_name', 'encadreur__user__last_name', 'statut'
    ] # Champs sur lesquels la recherche est possible
    ordering_fields = ['last_name', 'first_name', 'matricule', 'date_debut_stage', 'statut'] # Champs sur lesquels le tri est possible

    def get_permissions(self):
        """
        Retourne l'ensemble des permissions que cette vue requiert en fonction de l'action.
        """
        if self.action in ['list', 'create']:
            # Seuls les admins et RH peuvent lister et créer des stagiaires
            self.permission_classes = [IsAdminOrRH]
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            # Pour les détails, mise à jour et suppression :
            # Admin/RH ou l'encadreur du stagiaire
            self.permission_classes = [IsEncadreurOrAdminOrRH]
        else:
            # Pour toute autre action non spécifiée, l'utilisateur doit être authentifié
            self.permission_classes = [permissions.IsAuthenticated] 

        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        """
        Retourne le serializer approprié en fonction de l'action de la vue.
        - Pour la liste, utilise StagiaireListSerializer.
        - Pour les autres actions, utilise StagiaireCRUDSerializer.
        """
        if self.action == 'list':
            return StagiaireListSerializer
        return StagiaireCRUDSerializer
    
    def get_queryset(self):
        """
        Restreint le queryset en fonction des permissions de l'utilisateur authentifié.
        - Les admins/RH voient tous les stagiaires.
        - Les employés (encadreurs) ne voient que les stagiaires qu'ils encadrent.
        - Les utilisateurs non authentifiés ou sans rôle spécifique ne voient rien.
        """
        user = self.request.user
        if user.is_authenticated:
            # Les superutilisateurs, admins et RH voient tous les stagiaires
            if user.is_staff or user.role in ["admin", "rh"]:
                return Stagiaire.objects.all()
            # Un utilisateur authentifié qui est un employé peut voir les stagiaires qu'il encadre
            elif hasattr(user, 'employe'):
                return Stagiaire.objects.filter(encadreur=user.employe)
        # Par défaut (utilisateur non authentifié ou sans accès), retourne un queryset vide
        return Stagiaire.objects.none() 


class PeriodeStageViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les périodes de stage.
    Seuls les administrateurs et les RH peuvent gérer les périodes de stage.
    """
    queryset = PeriodeStage.objects.all() # Queryset de base
    permission_classes = [IsAdminOrRH] # Seuls les admins et RH peuvent accéder à ce ViewSet
    filter_backends = [filters.SearchFilter, filters.OrderingFilter] # Active la recherche et le tri
    search_fields = ['stagiaire__first_name', 'stagiaire__last_name', 'poste__nom'] # Champs sur lesquels la recherche est possible
    ordering_fields = ['date_debut', 'date_fin'] # Champs sur lesquels le tri est possible

    def get_serializer_class(self):
        """
        Retourne le serializer approprié en fonction de l'action de la vue.
        - Pour la liste, utilise PeriodeStageListSerializer.
        - Pour les autres actions, utilise PeriodeStageCRUDSerializer.
        """
        if self.action == 'list':
            return PeriodeStageListSerializer
        return PeriodeStageCRUDSerializer