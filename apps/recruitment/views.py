# recruitment/views.py

from rest_framework import viewsets, filters, permissions, status
from rest_framework.decorators import action # Pour ajouter des actions personnalisées aux ViewSets
from rest_framework.response import Response
from django.utils import timezone # Pour gérer les dates et heures avec les fuseaux horaires

from .models import OffreEmploi, Candidat
from .serializers import (
    OffreEmploiListSerializer, OffreEmploiCRUDSerializer,
    CandidatListSerializer, CandidatCRUDSerializer
)
from apps.users.permissions import IsAdminOrRH, IsAdminOrManagerOrRH, IsCandidatOwnerOrAdminOrManagerOrRH # Importe les permissions personnalisées

class OffreEmploiViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les offres d'emploi.
    - Tout le monde (authentifié ou anonyme) peut consulter la liste des offres publiées et leurs détails.
    - Seuls les admins et les RH peuvent créer, modifier et supprimer des offres.
    """
    queryset = OffreEmploi.objects.all() # Queryset de base
    filter_backends = [filters.SearchFilter, filters.OrderingFilter] # Active la recherche et le tri
    search_fields = ['titre', 'description', 'departement__nom', 'statut', 'type_emploi'] # Champs sur lesquels la recherche est possible
    ordering_fields = ['titre', 'date_creation', 'date_limite', 'statut'] # Champs sur lesquels le tri est possible

    def get_permissions(self):
        """
        Retourne l'ensemble des permissions que cette vue requiert en fonction de l'action.
        """
        if self.action == 'list' or self.action == 'retrieve':
            # Tout le monde (y compris les utilisateurs non authentifiés) peut lister et voir les détails des offres
            self.permission_classes = [permissions.AllowAny]
        else:
            # Seuls les admins et RH peuvent créer, mettre à jour, supprimer des offres
            self.permission_classes = [IsAdminOrRH]
        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        """
        Retourne le serializer approprié en fonction de l'action de la vue.
        - Pour la liste et le détail, utilise OffreEmploiListSerializer.
        - Pour les autres actions (création, mise à jour, suppression), utilise OffreEmploiCRUDSerializer.
        """
        if self.action == 'list' or self.action == 'retrieve':
            return OffreEmploiListSerializer
        return OffreEmploiCRUDSerializer
    
    def get_queryset(self):
        """
        Restreint le queryset en fonction des permissions de l'utilisateur authentifié.
        - Les admins et RH voient toutes les offres (brouillons, publiées, expirées).
        - Les autres utilisateurs (y compris les anonymes) ne voient que les offres publiées et non expirées.
        """
        user = self.request.user
        if user.is_authenticated and (user.is_staff or user.role in ["admin", "rh"]):
            return OffreEmploi.objects.all() # Admins/RH voient toutes les offres
        # Les utilisateurs publics ne voient que les offres dont le statut est 'publiee' et la date limite n'est pas dépassée
        return OffreEmploi.objects.filter(statut='publiee', date_limite__gte=timezone.now())


class CandidatViewSet(viewsets.ModelViewSet):
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