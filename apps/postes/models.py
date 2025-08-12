# postes/models.py

from django.db import models
from django.utils import timezone # Importation nécessaire pour les validations de date si réactivées

class Competence(models.Model):
    """
    Modèle représentant une compétence pouvant être requise pour un poste.
    """
    nom = models.CharField(max_length=100, unique=True, verbose_name="Nom de la compétence")
    description = models.TextField(blank=True, null=True, verbose_name="Description de la compétence")

    class Meta:
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"
        ordering = ['nom']

    def __str__(self):
        return self.nom

class Departement(models.Model):
    """
    Modèle représentant un département au sein de l'entreprise.
    """
    nom = models.CharField(max_length=100, unique=True, verbose_name="Nom du département")
    code_id = models.CharField(max_length=10, unique=True, verbose_name="Code du département")
    responsable = models.CharField(max_length=100, blank=True, null=True, verbose_name="Responsable du département")
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name="Emplacement du département")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Téléphone du département")
    email = models.EmailField(blank=True, null=True, verbose_name="Email du département")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    
    created_at = models.DateTimeField(auto_now_add=True) # Date de création automatique
    updated_at = models.DateTimeField(auto_now=True)     # Date de dernière mise à jour automatique

    class Meta:
        verbose_name = "Département"
        verbose_name_plural = "Départements"
        ordering = ['nom'] # Ordonne les départements par nom alphabétique

    def __str__(self):
        """Retourne une représentation en chaîne de caractères du département."""
        return self.nom


class Poste(models.Model):
    """
    Modèle représentant un poste au sein de l'entreprise.
    Ce modèle est lié au modèle Departement pour normaliser les départements.
    Il inclut des informations sur le poste, telles que le nom, la description, le responsable,
    le département, le salaire, le niveau d'expérience, les compétences requises, le statut,
    le lieu de travail et le type de contrat.
    """
    NIVEAU_EXPERIENCE_CHOICES = [
        ("junior", "Junior"),
        ("intermediaire", "Intermédiaire"),
        ("senior", "Senior"),
        ("expert", "Expert"),
    ]
    STATUT_CHOICES = [
        ("actif", "Actif"),
        ("inactif", "Inactif"),
    ]
    LIEU_CHOICES = [
        ("bureau", "Bureau"),
        ("teletravail", "Télétravail"),
        ("hybride", "Hybride"),
    ]
    CONTRAT_CHOICES = [
        ("CDI", "CDI"),
        ("CDD", "CDD"),
        ("Stage", "Stage"),
    ]

    nom = models.CharField(max_length=100, unique=True, verbose_name="Nom du poste")
    description = models.TextField(blank=True, null=True, verbose_name="Description du poste")
    responsable = models.CharField(max_length=100, blank=True, null=True, verbose_name="Responsable du poste")
    # Utilise une clé étrangère vers le modèle Departement pour normaliser les départements
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT, verbose_name="Département")
    salaire_mensuel = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salaire mensuel")
    niveau_experience = models.CharField(
        max_length=50,
        choices=NIVEAU_EXPERIENCE_CHOICES,
        default="junior",
        verbose_name="Niveau d'expérience",
    )
    # Utilise ManyToManyField pour les compétences
    competences = models.ManyToManyField(Competence, blank=True, verbose_name="Compétences requises")
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default="actif",
        verbose_name="Statut du poste",
    )
    # date_debut et date_fin sont commentés comme dans votre code fourni
    # date_debut = models.DateField(blank=True, null=True, verbose_name="Date de début")
    # date_fin = models.DateField(blank=True, null=True, verbose_name="Date de fin")
    lieu_travail = models.CharField(
        max_length=20,
        choices=LIEU_CHOICES,
        verbose_name="Lieu de travail",
    )
    type_contrat = models.CharField( # Renommé pour cohérence PEP8 et clarté
        max_length=20,
        choices=CONTRAT_CHOICES,
        verbose_name="Type de contrat",
    )

    created_at = models.DateTimeField(auto_now_add=True) # Date de création automatique
    updated_at = models.DateTimeField(auto_now=True)     # Date de dernière mise à jour automatique

    class Meta:
        verbose_name = "Poste"
        verbose_name_plural = "Postes"
        ordering = ["nom"] # Ordonne les postes par nom alphabétique

    def __str__(self):
        """Retourne une représentation en chaîne de caractères du poste."""
        # Affiche le nom du poste et le nom du département lié
        return f"{self.nom} ({self.departement.nom})"

    @property
    def get_employes(self):
        """
        Propriété qui retourne la liste des employés associés à ce poste.
        Utilise le related_name par défaut 'employe_set'.
        """
        return self.employe_set.all()