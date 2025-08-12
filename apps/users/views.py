# users/views.py
from rest_framework import generics, permissions, filters
from .models import User
from .serializers import UserListSerializer, UserCRUDSerializer
from .permissions import IsAdminOrRH

class UserListCreateAPIView(generics.ListCreateAPIView):
    """
    Vue pour lister et créer des utilisateurs.
    Accessible uniquement par les admins et les RH.
    """
    queryset = User.objects.all().order_by('-date_joined')
    permission_classes = [IsAdminOrRH]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'email', 'first_name', 'last_name', 'role']
    ordering_fields = ['username', 'email', 'first_name', 'last_name', 'role', 'date_joined']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCRUDSerializer # Pour la création
        return UserListSerializer # Pour la liste

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vue pour récupérer, mettre à jour et supprimer un utilisateur spécifique.
    Accessible uniquement par les admins et les RH.
    """
    queryset = User.objects.all()
    serializer_class = UserCRUDSerializer
    permission_classes = [IsAdminOrRH]