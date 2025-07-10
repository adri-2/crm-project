# postes/views.py

from rest_framework import generics, filters, permissions
from .models import Departement, Competence, Poste
from .serializers import (
    DepartementListSerializer, DepartementCRUDSerializer,
    CompetenceListSerializer, CompetenceCRUDSerializer,
    PosteListSerializer, PosteCRUDSerializer
)
from apps.users.permissions import IsAdminOrRH # Importe la permission personnalisée

# --- Vues pour Departement ---

class DepartementListCreateAPIView(generics.ListCreateAPIView):
    """
    Vue pour lister et créer des départements.
    Accessible uniquement par les admins et les RH.
    """
    queryset = Departement.objects.all().order_by('nom')
    permission_classes = [IsAdminOrRH]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nom', 'description', 'code_id', 'responsable', 'location', 'email']
    ordering_fields = ['nom', 'code_id', 'responsable', 'created_at']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DepartementCRUDSerializer
        return DepartementListSerializer

class DepartementRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vue pour récupérer, mettre à jour et supprimer un département spécifique.
    Accessible uniquement par les admins et les RH.
    """
    queryset = Departement.objects.all()
    serializer_class = DepartementCRUDSerializer
    permission_classes = [IsAdminOrRH]


# --- Vues pour Competence ---

class CompetenceListCreateAPIView(generics.ListCreateAPIView):
    """
    Vue pour lister et créer des compétences.
    Accessible uniquement par les admins et les RH.
    """
    queryset = Competence.objects.all().order_by('nom')
    permission_classes = [IsAdminOrRH]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nom', 'description']
    ordering_fields = ['nom']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CompetenceCRUDSerializer
        return CompetenceListSerializer

class CompetenceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vue pour récupérer, mettre à jour et supprimer une compétence spécifique.
    Accessible uniquement par les admins et les RH.
    """
    queryset = Competence.objects.all()
    serializer_class = CompetenceCRUDSerializer
    permission_classes = [IsAdminOrRH]


# --- Vues pour Poste ---

class PosteListCreateAPIView(generics.ListCreateAPIView):
    """
    Vue pour lister et créer des postes.
    Accessible uniquement par les admins et les RH.
    """
    queryset = Poste.objects.all().order_by('nom')
    permission_classes = [IsAdminOrRH]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nom', 'description', 'departement__nom', 'statut', 'type_contrat', 'competences__nom']
    ordering_fields = ['nom', 'salaire_mensuel', 'departement__nom', 'created_at']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PosteCRUDSerializer
        return PosteListSerializer

class PosteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vue pour récupérer, mettre à jour et supprimer un poste spécifique.
    Accessible uniquement par les admins et les RH.
    """
    queryset = Poste.objects.all()
    serializer_class = PosteCRUDSerializer
    permission_classes = [IsAdminOrRH]