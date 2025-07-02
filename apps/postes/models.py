from django.db import models

class Poste(models.Model):
    """
    Modèle représentant un poste au sein de l'entreprise.
    """
    NIVEAU_EXPERIENCE_CHOICES = [
        ('junior', 'Junior'),
        ('intermediaire', 'Intermédiaire'),
        ('senior', 'Senior'),
        ('expert', 'Expert'),
    ]
    STATUT_CHOICES = [
        ('actif', 'Actif'),
        ('inactif', 'Inactif'),
    ]
    LIEU_CHOICES = [
        ('bureau', 'Bureau'),
        ('teletravail', 'Télétravail'),
        ('hybride', 'Hybride'),
    ]
    CONTRAT_CHOICES = [
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('Stage', 'Stage'),
    ]

    nom = models.CharField(max_length=100, unique=True, verbose_name="Nom du poste")
    description = models.TextField(blank=True, null=True, verbose_name="Description du poste")
    responsable = models.CharField(max_length=100, blank=True, null=True, verbose_name="Responsable du poste")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    date_modification = models.DateTimeField(auto_now=True, verbose_name="Date de modification")
    departement = models.CharField(max_length=100, verbose_name="Département")
    salaire_mensuel = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salaire mensuel")
    niveau_experience = models.CharField(
        max_length=50,
        choices=NIVEAU_EXPERIENCE_CHOICES,
        default='junior',
        verbose_name="Niveau d'expérience"
    )
    competences_requises = models.TextField(blank=True, null=True, verbose_name="Compétences requises")
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='actif',
        verbose_name="Statut du poste"
    )
    date_debut = models.DateField(blank=True, null=True, verbose_name="Date de début")
    date_fin = models.DateField(blank=True, null=True, verbose_name="Date de fin")
    lieu_travail = models.CharField(
        max_length=20,
        choices=LIEU_CHOICES,
        verbose_name="Lieu de travail"
    )
    contrat_type = models.CharField(
        max_length=20,
        choices=CONTRAT_CHOICES,
        verbose_name="Type de contrat"
    )
    departement = models.CharField(max_length=100, verbose_name="Département")

    def get_employes(self):
        """
        Retourne la liste des employés associés à ce poste.
        """
        return self.employe_set.all()

    class Meta:
        verbose_name = "Poste"
        verbose_name_plural = "Postes"
        ordering = ['nom']

    def __str__(self):
        return f"{self.nom} ({self.departement})"