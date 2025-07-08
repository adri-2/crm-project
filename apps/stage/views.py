from django.shortcuts import render
from rest_framework import generics
from .models import Stage
from .serializers import StageListSerializer, StageDetailSerializer
from apps.users.permissions import IsAdminRHManager

class StageListView(generics.ListAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageListSerializer
    permission_classes = [IsAdminRHManager]

class StageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageDetailSerializer
    permission_classes = [IsAdminRHManager]
