# employees/models.py

from django.conf import settings
from django.db import models
import uuid
from apps.postes.models import Poste # Importe le modèle Poste

class Employe(models.Model):
    """
    Modèle représentant un employé au sein de l'entreprise.
    Chaque employé est lié à un utilisateur du système.
    """
    CONTRAT_CHOICES = (
        ("CDI", "CDI"),
        ("CDD", "CDD"),
        ("Stage", "Stage"),
    )
    STATUT_CHOICES = (
        ("actif", "Actif"),
        ("inactif", "Inactif"),
    )

    # L'employé est lié à un utilisateur unique du système d'authentification
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Utilisateur",
        related_name="employe" # Permet d'accéder à l'Employe depuis un objet User (ex: user.employe)
    )
    def generate_matricule():
        # Génère un UUID4, prend les 6 premiers caractères hexadécimaux
        return uuid.uuid4().hex[:6].upper()

    matricule = models.CharField(
        max_length=6,
        unique=True,
        verbose_name="Matricule",
        default=generate_matricule,
        editable=False
    )
    poste = models.ForeignKey(Poste, on_delete=models.PROTECT, verbose_name="Poste")
    
    # Relation récursive pour le supérieur hiérarchique
    chef = models.ForeignKey(
        "self", # Référence au modèle lui-même
        null=True,
        blank=True,
        on_delete=models.SET_NULL, # Si le chef est supprimé, le champ devient NULL
        related_name="subordonnes", # Permet d'accéder aux subordonnés d'un chef (ex: chef.subordonnes.all())
        verbose_name="Supérieur hiérarchique",
    )
    type_contrat = models.CharField(max_length=20, choices=CONTRAT_CHOICES, verbose_name="Type de contrat")
    date_embauche = models.DateField(verbose_name="Date d'embauche")
    adresse_personnelle = models.TextField(blank=True, null=True, verbose_name="Adresse personnelle")
    tel_personnelle = models.CharField(max_length=12, blank=True, null=True, verbose_name="Téléphone personnel")
    niveau_scolaire = models.CharField(max_length=100, blank=True, null=True, verbose_name="Niveau scolaire")
    champ_etude = models.CharField(max_length=100, blank=True, null=True, verbose_name="Champ d'étude")
    etablissement = models.CharField(max_length=150, blank=True, null=True, verbose_name="Établissement")
    tel_professionnel = models.CharField(max_length=150, blank=True, null=True, verbose_name="Téléphone professionnel")
    email_professionnel = models.EmailField(blank=True, null=True, verbose_name="Email professionnel")
    email_personnel = models.EmailField(blank=True, null=True, verbose_name="Email personnel")
    linkedin = models.URLField(blank=True, null=True, verbose_name="Profil LinkedIn")
    salaire_base = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salaire de base")
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default="actif", verbose_name="Statut")
    # competences = models.ManyToManyField('Competence', blank=True, verbose_name="Compétences requises")
    date_sortie = models.DateField(blank=True, null=True, verbose_name="Date de sortie")

    created_at = models.DateTimeField(auto_now_add=True) # Date de création automatique
    updated_at = models.DateTimeField(auto_now=True)     # Date de dernière mise à jour automatique

    class Meta:
        # Ordonne les employés par nom de famille, puis prénom de l'utilisateur lié
        ordering = ["user__last_name", "user__first_name"]
        verbose_name = "Employé"
        verbose_name_plural = "Employés"

    def __str__(self):
        """Retourne une représentation en chaîne de caractères de l'employé."""
        # Affiche le nom complet de l'utilisateur lié et le matricule de l'employé
        return f"{self.user.get_full_name()} ({self.matricule})"

    @property
    def get_stagiaires_encadres(self):
        """
        Propriété qui retourne la liste des stagiaires encadrés par cet employé.
        Utilise le related_name 'stagiaires_encadres' défini dans le modèle Stagiaire.
        """
        return self.stagiaires_encadres.all()