from django.shortcuts import render
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeListSerializer, EmployeeDetailSerializer
from apps.users.permissions import IsAdminRHManager

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer
    permission_classes = [IsAdminRHManager]

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeDetailSerializer
    permission_classes = [IsAdminRHManager]
