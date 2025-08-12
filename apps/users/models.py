# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

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
    email = models.EmailField(max_length=100,unique=True)
    def generate_matricule(self):
        # Génère un UUID4, prend les 6 premiers caractères hexadécimaux
        return uuid.uuid4().hex[:6].upper()

    matricule = models.CharField(
        max_length=6,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Matricule",
        help_text="Matricule de l'utilisateur (généré automatiquement)"
    )

    def save(self, *args, **kwargs):
        if not self.matricule:
            self.matricule = self.generate_matricule()
        super().save(*args, **kwargs)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        """Retourne une représentation en chaîne de caractères de l'utilisateur."""
        # Utilise le nom complet si disponible, sinon le nom d'utilisateur
        return self.get_full_name() or self.username