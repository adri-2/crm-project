# recruitment/models.py

from django.db import models
from django.utils import timezone # Pour gérer les dates et heures avec les fuseaux horaires
from apps.postes.models import Departement, Poste, Competence # Importe le modèle Departement

class OffreEmploi(models.Model):
    """
    Modèle représentant une offre d'emploi.
    """
    STATUS_CHOICES = (
        ("brouillon", "Brouillon"), # Offre en cours de rédaction, non visible publiquement
        ("publiee", "Publiée"),     # Offre active, visible publiquement
        ("expiree", "Expirée"),     # Date limite dépassée ou offre retirée
    )
    TYPE_EMPLOI_CHOICES = (
        ("CDI", "CDI"),
        ("CDD", "CDD"),
        ("Stage", "Stage"),
        ("Freelance", "Freelance"),
    )

    titre = models.CharField(max_length=150, verbose_name="Titre de l'offre")
    description = models.TextField(verbose_name="Description de l'offre")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    date_limite = models.DateTimeField(verbose_name="Date limite de candidature")
    statut = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="brouillon", verbose_name="Statut de l'offre"
    )
    generee_par_ia = models.BooleanField(default=False, verbose_name="Générée par IA")
    # Utilise une clé étrangère vers le modèle Departement pour normaliser les départements
    # departement = models.ForeignKey(Departement, on_delete=models.PROTECT, verbose_name="Département")
    # Utilise une clé étrangère vers le modèle Poste pour normaliser les postes
    poste = models.ForeignKey(Poste, on_delete=models.PROTECT, verbose_name="Poste")
    # Utilise une relation ManyToMany pour les compétences, permettant de lier plusieurs compétences    
    # à une offre d'emploi. Le modèle Competence doit être défini dans l'application correspondante.
    competences = models.ManyToManyField(Competence, blank=True, verbose_name="Compétences requises")
    # Nombre de postes voulus pour cette offre
    nombre_postes_voulus = models.PositiveIntegerField(verbose_name="Nombre de postes voulus")
    type_emploi = models.CharField(max_length=20, choices=TYPE_EMPLOI_CHOICES, verbose_name="Type d'emploi")
    periode = models.CharField(max_length=100, help_text="Ex: 6 mois, 1 an, Indéterminée", verbose_name="Période")
    competences = models.TextField(help_text="Liste des compétences attendues", verbose_name="Compétences requises")
    remuneration = models.CharField(max_length=100, verbose_name="Rémunération")
    est_publiee = models.BooleanField(default=False, verbose_name="Est publiée")

    class Meta:
        verbose_name = "Offre d'emploi"
        verbose_name_plural = "Offres d'emploi"
        ordering = ["-date_creation"] # Ordonne les offres par date de création décroissante

    def __str__(self):
        """Retourne une représentation en chaîne de caractères de l'offre d'emploi."""
        return self.titre

    def clean(self):
        """
        Validation personnalisée au niveau du modèle.
        S'assure que la date limite est dans le futur si l'offre est marquée comme publiée.
        """
        from django.core.exceptions import ValidationError
        if self.est_publiee and self.date_limite and self.date_limite < timezone.now():
            raise ValidationError("La date limite doit être future si l'offre est publiée.")

    def save(self, *args, **kwargs):
        """
        Surcharge de la méthode save pour mettre à jour le statut de l'offre avant sauvegarde.
        """
        self._update_status() # Appelle la méthode interne pour mettre à jour le statut
        super().save(*args, **kwargs) # Appelle la méthode save originale du modèle

    def _update_status(self):
        """
        Méthode interne pour mettre à jour le statut de l'offre en fonction de sa publication et de sa date limite.
        """
        now = timezone.now() # Obtient la date et l'heure actuelles avec le fuseau horaire
        if self.est_publiee and self.date_limite and self.date_limite > now:
            self.statut = "publiee" # Si publiée et non expirée
        elif self.date_limite and self.date_limite < now:
            self.statut = "expiree" # Si la date limite est dépassée
        else:
            self.statut = "brouillon" # Par défaut, ou si non publiée et non expirée

    @property
    def get_candidats(self):
        """
        Propriété qui retourne tous les candidats associés à cette offre.
        Utilise le related_name 'candidats' défini dans le modèle Candidat.
        """
        return self.candidats.all()


class Candidat(models.Model):
    """
    Modèle représentant un candidat postulant à une offre d'emploi.
    """
    STATUT_CHOICES = (
        ("nouveau", "Nouveau"),     # Candidature soumise
        ("entretien", "Entretien"), # Candidat en phase d'entretien
        ("accepte", "Accepté"),     # Candidature acceptée
        ("rejete", "Rejeté"),       # Candidature rejetée
    )
    nom_complet = models.CharField(max_length=150, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Adresse email")
    telephone = models.CharField(max_length=20, verbose_name="Numéro de téléphone")
    cv = models.FileField(upload_to="cvs/", verbose_name="CV") # Les CVs seront stockés dans le dossier 'media/cvs/'
    medium = models.CharField(
        max_length=100, help_text="Ex: LinkedIn, Indeed, Recommandation, etc.", verbose_name="Source"
    )
    score_cv_ia = models.FloatField(null=True, blank=True, verbose_name="Score CV (IA)") # Champ pour un score généré par IA
    poste_vise = models.CharField(max_length=100, verbose_name="Poste visé")
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default="nouveau", verbose_name="Statut")
    offre = models.ForeignKey(
        OffreEmploi, on_delete=models.CASCADE, related_name="candidats", verbose_name="Offre liée"
    )
    # Utilise une relation ManyToMany pour les compétences, permettant de lier plusieurs compétences    
    # à une offre d'emploi. Le modèle Competence doit être défini dans l'application correspondante.
    # competences = models.ManyToManyField(Competence, blank=True, verbose_name="Compétences requises")

    created_at = models.DateTimeField(auto_now_add=True) # Date de création automatique
    updated_at = models.DateTimeField(auto_now=True)     # Date de dernière mise à jour automatique

    class Meta:
        verbose_name = "Candidat"
        verbose_name_plural = "Candidats"
        ordering = ["-created_at", "nom_complet"] # Ordonne les candidats par date de création (décroissante) et nom complet
        # Ajout d'une contrainte d'unicité pour éviter les candidatures multiples
        # pour la même offre par le même email (email + offre doivent être uniques ensemble)
        unique_together = ('email', 'offre') 

    def __str__(self):
        """Retourne une représentation en chaîne de caractères du candidat."""
        return f"{self.nom_complet} pour {self.offre.titre}"