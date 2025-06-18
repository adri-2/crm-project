from django.db import models
from django.contrib.auth.models import AbstractUser

# --------------------
# Utilisateur de base
# --------------------
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('rh', 'Ressources Humaines'),
        ('manager', 'Manager'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='rh')

# --------------------
# Employé
# --------------------
class Employe(models.Model):
    CONTRAT_CHOICES = (
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('Stage', 'Stage'),
    )
    STATUT_CHOICES = (
        ('actif', 'Actif'),
        ('inactif', 'Inactif'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricule = models.CharField(max_length=20, unique=True)
    poste = models.CharField(max_length=100)
    contrat_type = models.CharField(max_length=20, choices=CONTRAT_CHOICES)
    date_embauche = models.DateField()
    departement = models.CharField(max_length=100)
    adresse_personnelle = models.TextField(blank=True, null=True)
    niveau_certificat = models.CharField(max_length=100, blank=True, null=True)
    champ_etude = models.CharField(max_length=100, blank=True, null=True)
    etablissement = models.CharField(max_length=150, blank=True, null=True)
    email_professionnel = models.EmailField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    salaire_base = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='actif')
    date_sortie = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.matricule})"

