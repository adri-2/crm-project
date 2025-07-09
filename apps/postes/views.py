# departement/views.py

from rest_framework import viewsets, filters
from .models import Departement, Poste
from .serializers import (DepartementListSerializer, DepartementCRUDSerializer,PosteListSerializer, PosteCRUDSerializer)
from apps.users.permissions import IsAdminOrRH # Importe la permission personnalisée


class DepartementViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les départements.
    Seuls les administrateurs et les RH peuvent gérer les départements.
    """
    queryset = Departement.objects.all()
    permission_classes = [IsAdminOrRH] # Seuls les admins et RH peuvent accéder à ce ViewSet

    def get_serializer_class(self):
        """
        Retourne le serializer approprié en fonction de l'action de la vue.
        - Pour la liste, utilise DepartementListSerializer.
        - Pour les autres actions, utilise DepartementCRUDSerializer.
        """
        if self.action == 'list':
            return DepartementListSerializer
        return DepartementCRUDSerializer
    
# postes/views.py

class PosteViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les postes.
    Seuls les administrateurs et les RH peuvent gérer les postes.
    """
    queryset = Poste.objects.all()
    permission_classes = [IsAdminOrRH] # Seuls les admins et RH peuvent accéder à ce ViewSet
    filter_backends = [filters.SearchFilter, filters.OrderingFilter] # Active la recherche et le tri
    search_fields = ['nom', 'description', 'departement__nom'] # Champs sur lesquels la recherche est possible
    ordering_fields = ['nom', 'salaire_mensuel', 'departement__nom'] # Champs sur lesquels le tri est possible

    def get_serializer_class(self):
        """
        Retourne le serializer approprié en fonction de l'action de la vue.
        - Pour la liste, utilise PosteListSerializer.
        - Pour les autres actions, utilise PosteCRUDSerializer.
        """
        if self.action == 'list':
            return PosteListSerializer
        return PosteCRUDSerializer    