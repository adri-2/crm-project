from django.shortcuts import render
from rest_framework import generics
from .models import Poste
from .serializers import PosteListSerializer, PosteDetailSerializer
from apps.users.permissions import IsAdminRHManager

class PosteListView(generics.ListAPIView):
    queryset = Poste.objects.all()
    serializer_class = PosteListSerializer
    permission_classes = [IsAdminRHManager]

class PosteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poste.objects.all()
    serializer_class = PosteDetailSerializer
    permission_classes = [IsAdminRHManager]

# Create your views here.
