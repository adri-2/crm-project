from django.db import models
from django.conf import settings
from django.urls import reverse
from postes.models import Postes

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

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Utilisateur"
    )
    matricule = models.CharField(max_length=20, unique=True, verbose_name="Matricule")
    poste = models.ForeignKey(Postes, on_delete=models.PROTECT, verbose_name="Poste")
    chef = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='subordonnes',
        verbose_name="Supérieur hiérarchique"
    )
    contrat_type = models.CharField(max_length=20, choices=CONTRAT_CHOICES, verbose_name="Type de contrat")
    date_embauche = models.DateField(verbose_name="Date d'embauche")
    # departement = models.CharField(max_length=100, verbose_name="Département")
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
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='actif', verbose_name="Statut")
    date_sortie = models.DateField(blank=True, null=True, verbose_name="Date de sortie")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['user__last_name', 'user__first_name']
        verbose_name = "Employé"
        verbose_name_plural = "Employés"

    def get_absolute_url(self):
        return reverse('employe_detail', kwargs={'pk': self.pk})
    
    @property
    def get_my_stagiaires(self):
        return self.stagiaires_encadres.all()

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.matricule})"
