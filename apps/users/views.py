from django.shortcuts import render
from rest_framework import generics
from .models import User, Candidat
from .serializers import UserListSerializer, UserDetailSerializer, CandidatListSerializer, CandidatDetailSerializer
from .permissions import IsAdminRHManager, IsSelfOrAdminRHManager

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAdminRHManager]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsSelfOrAdminRHManager | IsAdminRHManager]

    def get_queryset(self):
        user = self.request.user
        if user.role in ['admin', 'rh', 'manager']:
            return User.objects.all()
        # Stagiaire/employé : ne peut voir que lui-même
        return User.objects.filter(pk=user.pk)

class CandidatListView(generics.ListAPIView):
    serializer_class = CandidatListSerializer
    permission_classes = [IsAdminRHManager]
    def get_queryset(self):
        user = self.request.user
        if user.role in ['admin', 'rh', 'manager']:
            return Candidat.objects.all()
        # Stagiaire/employé : ne voit que ses propres candidatures
        return Candidat.objects.filter(user=user)

class CandidatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidat.objects.all()
    serializer_class = CandidatDetailSerializer
    permission_classes = [IsAdminRHManager]

# Create your views here.
