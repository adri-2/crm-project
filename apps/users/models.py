from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('rh', 'Ressources Humaines'),
        ('manager', 'Manager'),
        ('user', 'Utilisateur'),
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='rh',
        verbose_name="Rôle",
        help_text="Rôle de l'utilisateur dans l'application"
    )

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
