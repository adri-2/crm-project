# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Modèle d'utilisateur personnalisé étendant AbstractUser.
    Ajoute un champ de rôle pour la gestion des permissions.
    """
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('rh', 'Ressources Humaines'),
        ('manager', 'Manager'),
        ('user', 'Utilisateur'), # Rôle par défaut pour les utilisateurs standards (inclut les employés sans rôle spécifique RH/Manager)
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='user', # Le rôle par défaut est 'user'
        verbose_name="Rôle",
        help_text="Rôle de l'utilisateur dans l'application"
    )

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        """Retourne une représentation en chaîne de caractères de l'utilisateur."""
        # Utilise le nom complet si disponible, sinon le nom d'utilisateur
        return self.get_full_name() or self.username