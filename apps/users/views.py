# users/views.py

from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserListSerializer, UserCRUDSerializer
from .permissions import IsAdminOrRH # Importe la permission personnalisée

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les utilisateurs.
    Seuls les administrateurs et les RH peuvent gérer les utilisateurs.
    """
    queryset = User.objects.all().order_by('-date_joined') # Ordonne par date d'inscription
    permission_classes = [IsAdminOrRH] # Seuls les admins et RH peuvent accéder à ce ViewSet

    def get_serializer_class(self):
        """
        Retourne le serializer approprié en fonction de l'action de la vue.
        - Pour la liste, utilise UserListSerializer (lecture simple).
        - Pour les autres actions (création, détail, mise à jour, suppression), utilise UserCRUDSerializer.
        """
        if self.action == 'list':
            return UserListSerializer
        return UserCRUDSerializer