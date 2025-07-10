# recruitment/views.py

from rest_framework import generics, filters, permissions, status
from rest_framework.decorators import action # Pour ajouter des actions personnalisées aux ViewSets
from rest_framework.response import Response
from django.utils import timezone # Pour gérer les dates et heures avec les fuseaux horaires

from .models import OffreEmploi, Candidat
from .serializers import (
    OffreEmploiListSerializer, OffreEmploiCRUDSerializer,
    CandidatListSerializer, CandidatCRUDSerializer
)
from apps.users.permissions import IsAdminOrRH, IsAdminOrManagerOrRH, IsCandidatOwnerOrAdminOrManagerOrRH # Importe les permissions personnalisées


# --- Vues pour OffreEmploi ---

class OffreEmploiListCreateAPIView(generics.ListCreateAPIView):
    """
    Vue pour lister et créer des offres d'emploi.
    - Tout le monde peut lister les offres publiées.
    - Seuls les admins et les RH peuvent créer des offres.
    """
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titre', 'description', 'departement__nom', 'statut', 'type_emploi']
    ordering_fields = ['titre', 'date_creation', 'date_limite', 'statut', 'created_at']

    def get_queryset(self):
        """
        Restreint le queryset pour n'afficher que les offres publiées aux utilisateurs non-RH/Admin.
        """
        user = self.request.user
        if user.is_authenticated and (user.is_staff or user.role in ["admin", "rh"]):
            return OffreEmploi.objects.all().order_by('-date_creation') # Admins/RH voient toutes les offres
        # Public ne voit que les publiées et non expirées
        return OffreEmploi.objects.filter(statut='publiee', date_limite__gte=timezone.now()).order_by('-date_creation')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OffreEmploiCRUDSerializer # Pour la création
        return OffreEmploiListSerializer # Pour la liste

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminOrRH()] # Seuls les admins/RH peuvent créer
        return [permissions.AllowAny()] # Tout le monde peut lister


class OffreEmploiRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vue pour récupérer, mettre à jour et supprimer une offre d'emploi spécifique.
    - Tout le monde peut récupérer les détails des offres publiées.
    - Seuls les admins et les RH peuvent mettre à jour et supprimer.
    """
    queryset = OffreEmploi.objects.all()
    serializer_class = OffreEmploiCRUDSerializer # Pour la mise à jour/suppression, utilisez le CRUD serializer

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return OffreEmploiListSerializer # Pour la lecture, utilisez le List serializer
        return OffreEmploiCRUDSerializer # Pour la mise à jour/suppression

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()] # Tout le monde peut lire
        return [IsAdminOrRH()] # Seuls les admins/RH peuvent modifier/supprimer

    def get_queryset(self):
        """
        Restreint le queryset pour n'afficher que les offres publiées aux utilisateurs non-RH/Admin lors de la lecture.
        """
        user = self.request.user
        if user.is_authenticated and (user.is_staff or user.role in ["admin", "rh"]):
            return OffreEmploi.objects.all() # Admins/RH voient toutes les offres
        # Public ne voit que les publiées et non expirées
        return OffreEmploi.objects.filter(statut='publiee', date_limite__gte=timezone.now())


# --- Vues pour Candidat ---

class CandidatListCreateAPIView(generics.ListCreateAPIView):
    """
    Vue pour lister et créer des candidatures.
    - Tout le monde peut créer une candidature (postuler).
    - Les admins/RH/managers peuvent lister toutes les candidatures.
    - Les employés ne peuvent lister que leurs propres candidatures.
    """
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nom_complet', 'email', 'poste_vise', 'statut', 'offre__titre']
    ordering_fields = ['created_at', 'statut', 'nom_complet']

    def get_queryset(self):
        """
        Restreint le queryset en fonction des permissions de l'utilisateur authentifié.
        - Les admins/RH/managers voient toutes les candidatures.
        - Les employés authentifiés ne voient que leurs propres candidatures (basé sur l'email personnel).
        - Les utilisateurs non authentifiés ne voient rien après la création.
        """
        user = self.request.user
        if user.is_authenticated:
            if user.is_staff or user.role in ["admin", "rh", "manager"]:
                return Candidat.objects.all().order_by('-created_at')
            elif hasattr(user, 'employe') and user.employe.email_personnel:
                return Candidat.objects.filter(email=user.employe.email_personnel).order_by('-created_at')
        return Candidat.objects.none()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CandidatCRUDSerializer # Pour la création
        return CandidatListSerializer # Pour la liste

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()] # Tout le monde peut créer (postuler)
        # Pour la liste, la permission est gérée par get_queryset et IsAuthenticated
        return [permissions.IsAuthenticated()]


class CandidatRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vue pour récupérer, mettre à jour et supprimer une candidature spécifique.
    - Les admins/RH/managers ont un accès complet.
    - Un employé peut récupérer ses propres candidatures.
    """
    queryset = Candidat.objects.all()
    serializer_class = CandidatCRUDSerializer
    permission_classes = [IsCandidatOwnerOrAdminOrManagerOrRH] # Permission au niveau de l'objet

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return CandidatListSerializer # Pour la lecture, utilisez le List serializer
        return CandidatCRUDSerializer # Pour la mise à jour/suppression

    def get_queryset(self):
        """
        Assure que l'utilisateur ne peut accéder qu'à ses propres candidatures s'il n'est pas admin/RH/manager.
        """
        user = self.request.user
        if user.is_authenticated and (user.is_staff or user.role in ["admin", "rh", "manager"]):
            return Candidat.objects.all()
        elif user.is_authenticated and hasattr(user, 'employe') and user.employe.email_personnel:
            return Candidat.objects.filter(email=user.employe.email_personnel)
        return Candidat.objects.none()


class CandidatAcceptAPIView(generics.UpdateAPIView):
    """
    Vue pour accepter une candidature.
    Accessible uniquement par les admins, RH et managers.
    """
    queryset = Candidat.objects.all()
    serializer_class = CandidatListSerializer # Retourne le format liste après l'action
    permission_classes = [IsAdminOrManagerOrRH]

    def patch(self, request, *args, **kwargs):
        candidat = self.get_object()
        if candidat.statut == 'accepte':
            return Response({'detail': 'La candidature est déjà acceptée.'}, status=status.HTTP_400_BAD_REQUEST)
        
        candidat.statut = 'accepte'
        candidat.save()
        serializer = self.get_serializer(candidat)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CandidatRejectAPIView(generics.UpdateAPIView):
    """
    Vue pour rejeter une candidature.
    Accessible uniquement par les admins, RH et managers.
    """
    queryset = Candidat.objects.all()
    serializer_class = CandidatListSerializer # Retourne le format liste après l'action
    permission_classes = [IsAdminOrManagerOrRH]

    def patch(self, request, *args, **kwargs):
        candidat = self.get_object()
        if candidat.statut == 'rejete':
            return Response({'detail': 'La candidature est déjà rejetée.'}, status=status.HTTP_400_BAD_REQUEST)

        candidat.statut = 'rejete'
        candidat.save()
        serializer = self.get_serializer(candidat)
        return Response(serializer.data, status=status.HTTP_200_OK)
    """
    ViewSet pour gérer les candidatures.
    - Tout le monde peut postuler (créer une candidature).
    - Les admins/RH/managers peuvent voir toutes les candidatures et les gérer (accepter/rejeter).
    - Les employés ne peuvent voir que leurs propres candidatures.
    """
    queryset = Candidat.objects.all() # Queryset de base
    filter_backends = [filters.SearchFilter, filters.OrderingFilter] # Active la recherche et le tri
    search_fields = ['nom_complet', 'email', 'poste_vise', 'statut', 'offre__titre'] # Champs sur lesquels la recherche est possible
    ordering_fields = ['created_at', 'statut', 'nom_complet'] # Champs sur lesquels le tri est possible

    def get_permissions(self):
        """
        Retourne l'ensemble des permissions que cette vue requiert en fonction de l'action.
        """
        if self.action == 'create':
            # Tout le monde (authentifié ou anonyme) peut créer une candidature (postuler)
            self.permission_classes = [permissions.AllowAny]
        elif self.action == 'list':
            # Les admins/RH/managers voient toutes les candidatures.
            # Les employés authentifiés peuvent lister leurs propres candidatures (géré par get_queryset).
            self.permission_classes = [IsAdminOrManagerOrRH | permissions.IsAuthenticated] 
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy', 'accept', 'reject']:
            # Pour les détails, mise à jour, suppression, accept/reject :
            # Admin/RH/Manager ou le propriétaire de la candidature (pour retrieve/update/delete)
            self.permission_classes = [IsCandidatOwnerOrAdminOrManagerOrRH]
        else:
            # Pour toute autre action non spécifiée, l'utilisateur doit être authentifié
            self.permission_classes = [permissions.IsAuthenticated] 

        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        """
        Retourne le serializer approprié en fonction de l'action de la vue.
        - Pour la liste, utilise CandidatListSerializer.
        - Pour les autres actions, utilise CandidatCRUDSerializer.
        """
        if self.action == 'list':
            return CandidatListSerializer
        return CandidatCRUDSerializer
    
    def get_queryset(self):
        """
        Restreint le queryset en fonction des permissions de l'utilisateur authentifié.
        - Les admins/RH/managers voient toutes les candidatures.
        - Les employés authentifiés ne voient que leurs propres candidatures (basé sur l'email personnel).
        - Les utilisateurs non authentifiés ne voient rien après la création.
        """
        user = self.request.user
        if user.is_authenticated:
            # Les superutilisateurs, admins, RH et managers voient toutes les candidatures
            if user.is_staff or user.role in ["admin", "rh", "manager"]:
                return Candidat.objects.all()
            # Un utilisateur authentifié qui a un profil d'employé peut voir les candidatures où l'email correspond à son email personnel
            elif hasattr(user, 'employe') and user.employe.email_personnel:
                return Candidat.objects.filter(email=user.employe.email_personnel)
        # Par défaut (utilisateur non authentifié ou sans accès), retourne un queryset vide
        return Candidat.objects.none() 

    @action(detail=True, methods=['post'], permission_classes=[IsAdminOrManagerOrRH])
    def accept(self, request, pk=None):
        """
        Action personnalisée pour accepter une candidature.
        Accessible uniquement par les admins, RH et managers.
        """
        candidat = self.get_object() # Récupère l'objet Candidat
        if candidat.statut == 'accepte':
            return Response({'detail': 'La candidature est déjà acceptée.'}, status=status.HTTP_400_BAD_REQUEST)
        
        candidat.statut = 'accepte' # Met à jour le statut
        candidat.save() # Sauvegarde l'objet
        serializer = self.get_serializer(candidat) # Sérialise l'objet mis à jour
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[IsAdminOrManagerOrRH])
    def reject(self, request, pk=None):
        """
        Action personnalisée pour rejeter une candidature.
        Accessible uniquement par les admins, RH et managers.
        """
        candidat = self.get_object() # Récupère l'objet Candidat
        if candidat.statut == 'rejete':
            return Response({'detail': 'La candidature est déjà rejetée.'}, status=status.HTTP_400_BAD_REQUEST)

        candidat.statut = 'rejete' # Met à jour le statut
        candidat.save() # Sauvegarde l'objet
        serializer = self.get_serializer(candidat) # Sérialise l'objet mis à jour
        return Response(serializer.data, status=status.HTTP_200_OK)