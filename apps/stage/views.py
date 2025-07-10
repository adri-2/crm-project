# stage/views.py

from rest_framework import generics, filters, permissions
from .models import Stagiaire, PeriodeStage
from .serializers import (
    StagiaireListSerializer, StagiaireCRUDSerializer,
    PeriodeStageListSerializer, PeriodeStageCRUDSerializer
)
from apps.users.permissions import IsAdminOrRH, IsEncadreurOrAdminOrRH # Importe les permissions personnalisées


# --- Vues pour Stagiaire ---

class StagiaireListCreateAPIView(generics.ListCreateAPIView):
    """
    Vue pour lister et créer des stagiaires.
    - Les admins/RH peuvent lister et créer.
    - Les encadreurs (employés) peuvent lister les stagiaires qu'ils encadrent.
    """
    permission_classes = [permissions.IsAuthenticated] # Base: authentifié

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'first_name', 'last_name', 'matricule', 'poste__nom', 
        'encadreur__user__first_name', 'encadreur__user__last_name', 'statut'
    ]
    ordering_fields = ['last_name', 'first_name', 'matricule', 'date_debut_stage', 'statut', 'created_at']

    def get_queryset(self):
        """
        Restreint le queryset en fonction des permissions de l'utilisateur authentifié.
        - Les admins/RH voient tous les stagiaires.
        - Les employés (encadreurs) ne voient que les stagiaires qu'ils encadrent.
        """
        user = self.request.user
        if user.is_authenticated:
            if user.is_staff or user.role in ["admin", "rh"]:
                return Stagiaire.objects.all().order_by('last_name', 'first_name')
            elif hasattr(user, 'employe'):
                return Stagiaire.objects.filter(encadreur=user.employe).order_by('last_name', 'first_name')
        return Stagiaire.objects.none()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return StagiaireCRUDSerializer # Pour la création
        return StagiaireListSerializer # Pour la liste

    def get_permissions(self):
        # Pour la création, seuls les admins/RH sont autorisés
        if self.request.method == 'POST':
            return [IsAdminOrRH()]
        # Pour la liste, la permission est gérée par get_queryset et IsAuthenticated
        return [permissions.IsAuthenticated()]


class StagiaireRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vue pour récupérer, mettre à jour et supprimer un stagiaire spécifique.
    - Les admins/RH ont un accès complet.
    - Les encadreurs peuvent voir et modifier les stagiaires qu'ils encadrent.
    """
    queryset = Stagiaire.objects.all()
    serializer_class = StagiaireCRUDSerializer
    permission_classes = [IsEncadreurOrAdminOrRH] # Permission au niveau de l'objet

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return StagiaireListSerializer # Pour la lecture, utilisez le List serializer
        return StagiaireCRUDSerializer # Pour la mise à jour/suppression

    def get_queryset(self):
        """
        Assure que l'utilisateur ne peut accéder qu'aux stagiaires qu'il encadre s'il n'est pas admin/RH.
        """
        user = self.request.user
        if user.is_authenticated and (user.is_staff or user.role in ["admin", "rh"]):
            return Stagiaire.objects.all()
        elif user.is_authenticated and hasattr(user, 'employe'):
            return Stagiaire.objects.filter(encadreur=user.employe)
        return Stagiaire.objects.none()


# --- Vues pour PeriodeStage ---

class PeriodeStageListCreateAPIView(generics.ListCreateAPIView):
    """
    Vue pour lister et créer des périodes de stage.
    Accessible uniquement par les admins et les RH.
    """
    queryset = PeriodeStage.objects.all().order_by('-date_debut')
    permission_classes = [IsAdminOrRH]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['stagiaire__first_name', 'stagiaire__last_name', 'poste__nom']
    ordering_fields = ['date_debut', 'date_fin', 'created_at']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PeriodeStageCRUDSerializer
        return PeriodeStageListSerializer

class PeriodeStageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vue pour récupérer, mettre à jour et supprimer une période de stage spécifique.
    Accessible uniquement par les admins et les RH.
    """
    queryset = PeriodeStage.objects.all()
    serializer_class = PeriodeStageCRUDSerializer
    permission_classes = [IsAdminOrRH]
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