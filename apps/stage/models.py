# stage/models.py

from django.db import models
from apps.employees.models import Employe # Importe le modèle Employe
from apps.postes.models import Poste # Importe le modèle Poste
from django.utils.text import slugify # Utilisé pour générer le username unique
import uuid # Utilisé pour générer un matricule unique

class Stagiaire(models.Model):
    """
    Modèle représentant un stagiaire au sein de l'entreprise.
    """
    CONTRAT_CHOICES = (
        ("Stage Académique", "Stage Académique"),
        ("Stage Professionnel", "Stage Professionnel"),
        ("Stage Réemployé", "Stage Réemployé"),
    )
    STATUT_CHOICES = (
        ("actif", "Actif"),
        ("inactif", "Inactif"),
    )

    first_name = models.CharField(max_length=100, verbose_name="Prénom")
    last_name = models.CharField(max_length=100, verbose_name="Nom")
    # Le champ 'username' est généré automatiquement et est unique pour chaque stagiaire
    username = models.CharField(max_length=100, unique=True, blank=True, verbose_name="Nom d'utilisateur unique")
    matricule = models.CharField(
        max_length=6,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Matricule",
        help_text="Matricule de l'utilisateur (généré automatiquement)"
    )
   
    poste = models.ForeignKey(Poste, on_delete=models.PROTECT, verbose_name="Poste")
    encadreur = models.ForeignKey(
        Employe,
        on_delete=models.PROTECT, # Empêche la suppression d'un employé s'il encadre encore des stagiaires
        related_name="stagiaires_encadres", # Permet d'accéder aux stagiaires encadrés par un employé (ex: employe.stagiaires_encadres.all())
        verbose_name="Encadreur",
    )
    type_contrat = models.CharField(max_length=30, choices=CONTRAT_CHOICES, verbose_name="Type de contrat")
    date_debut_stage = models.DateField(verbose_name="Date de début de stage")
    adresse_personnelle = models.TextField(blank=True, null=True, verbose_name="Adresse personnelle")
    tel_personnelle = models.CharField(max_length=12, blank=True, null=True, verbose_name="Téléphone personnel")
    niveau_scolaire = models.CharField(max_length=100, blank=True, null=True, verbose_name="Niveau scolaire")
    champ_etude = models.CharField(max_length=100, blank=True, null=True, verbose_name="Champ d'étude")
    etablissement = models.CharField(max_length=150, blank=True, null=True, verbose_name="Établissement")
    tel_professionnel = models.CharField(max_length=150, blank=True, null=True, verbose_name="Téléphone professionnel")
    email_professionnel = models.EmailField(blank=True, null=True, verbose_name="Email professionnel")
    email_personnel = models.EmailField(blank=True, null=True, verbose_name="Email personnel")
    # linkedin = models.URLField(blank=True, null=True, verbose_name="Profil LinkedIn")
    salaire_base = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Allocation de stage")
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default="actif", verbose_name="Statut")
    date_fin_stage = models.DateField(blank=True, null=True, verbose_name="Date de fin de stage")

    created_at = models.DateTimeField(auto_now_add=True) # Date de création automatique
    updated_at = models.DateTimeField(auto_now=True)     # Date de dernière mise à jour automatique

    class Meta:
        ordering = ["last_name", "first_name"] # Ordonne les stagiaires par nom de famille, puis prénom
        verbose_name = "Stagiaire"
        verbose_name_plural = "Stagiaires"

    def __str__(self):
        """Retourne une représentation en chaîne de caractères du stagiaire."""
        return f"{self.first_name} {self.last_name} ({self.matricule})"

    def save(self, *args, **kwargs):
        """
        Surcharge de la méthode save pour générer un 'username' unique si non fourni.
        Le 'username' est basé sur le prénom et le nom, avec un suffixe numérique si nécessaire pour l'unicité.
        """
        if not self.username:
            # Crée un 'username' de base à partir du prénom et du nom (en minuscules et slugifié)
            base_username = slugify(f"{self.first_name} {self.last_name}")
            username = base_username
            num = 1
            # Boucle tant que le 'username' généré existe déjà
            while Stagiaire.objects.filter(username=username).exists():
                username = f"{base_username}-{num}" # Ajoute un suffixe numérique
                num += 1
            self.username = username # Assigne le 'username' unique
        super().save(*args, **kwargs) # Appelle la méthode save originale du modèle
    
    def generate_matricule(self):
        # Génère un UUID4, prend les 6 premiers caractères hexadécimaux
        return uuid.uuid4().hex[:6].upper()

    def save(self, *args, **kwargs):
        if not self.matricule:
            self.matricule = self.generate_matricule()
        super().save(*args, **kwargs)


class PeriodeStage(models.Model):
    """
    Modèle pour enregistrer les périodes de stage d'un stagiaire.
    """
    stagiaire = models.ForeignKey("Stagiaire", on_delete=models.PROTECT, verbose_name="Stagiaire")
    poste = models.ForeignKey(Poste, on_delete=models.PROTECT, verbose_name="Poste")
    date_debut = models.DateField(verbose_name="Date de Début")
    date_fin = models.DateField(verbose_name="Date de Fin")
    
    created_at = models.DateTimeField(auto_now_add=True) # Date de création automatique
    updated_at = models.DateTimeField(auto_now=True)     # Date de dernière mise à jour automatique

    class Meta:
        verbose_name = "Période de Stage"
        verbose_name_plural = "Périodes de Stage"
        ordering = ["-date_debut"] # Ordonne les périodes de stage par date de début décroissante

    def __str__(self):
        """Retourne une représentation en chaîne de caractères de la période de stage."""
        # Affiche le nom du stagiaire et le poste associé pour une meilleure lisibilité
        return f"Période pour {self.stagiaire.first_name} {self.stagiaire.last_name} ({self.poste.nom})"

    def clean(self):
        """
        Validation personnalisée au niveau du modèle pour s'assurer que la date de fin est après la date de début.
        Cette validation est appelée par form.is_valid() ou model.full_clean().
        """
        from django.core.exceptions import ValidationError
        if self.date_debut and self.date_fin and self.date_fin < self.date_debut:
            raise ValidationError("La date de fin doit être postérieure à la date de début.")