from django.shortcuts import render
from rest_framework import generics, permissions
from .models import OffreEmploi, Candidat
from .serializers import (
    OffreEmploiListSerializer, OffreEmploiDetailSerializer,
    CandidatListSerializer, CandidatDetailSerializer
)
from apps.users.permissions import IsAdminRHManager

# Tout le monde peut voir la liste des offres et postuler
class OffreEmploiListView(generics.ListAPIView):
    queryset = OffreEmploi.objects.all()
    serializer_class = OffreEmploiListSerializer
    permission_classes = [permissions.AllowAny]

class OffreEmploiDetailView(generics.RetrieveAPIView):
    queryset = OffreEmploi.objects.all()
    serializer_class = OffreEmploiDetailSerializer
    permission_classes = [permissions.AllowAny]

# Postuler à une offre (création de candidature)
class CandidatCreateView(generics.CreateAPIView):
    queryset = Candidat.objects.all()
    serializer_class = CandidatDetailSerializer
    permission_classes = [permissions.AllowAny]

# Seuls admin, RH, manager peuvent voir la liste des candidats et gérer les candidatures
class CandidatListView(generics.ListAPIView):
    queryset = Candidat.objects.all()
    serializer_class = CandidatListSerializer
    permission_classes = [IsAdminRHManager]

class CandidatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidat.objects.all()
    serializer_class = CandidatDetailSerializer
    permission_classes = [IsAdminRHManager]