from django.db import models

# Create your models here.

# --------------------
# Offre d'emploi
# --------------------
class OffreEmploi(models.Model):
    STATUS_CHOICES = (
        ('brouillon', 'Brouillon'),
        ('publiée', 'Publiée'),
        ('expirée', 'Expirée'),
    )
    TYPE_EMPLOI_CHOICES = (
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('Stage', 'Stage'),
        ('Freelance', 'Freelance'),
    )

    titre = models.CharField(max_length=150)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='brouillon')
    generee_par_ia = models.BooleanField(default=False)
    departement = models.CharField(max_length=100)
    nbre_voulue = models.PositiveIntegerField()
    type_emploi = models.CharField(max_length=20, choices=TYPE_EMPLOI_CHOICES)
    periode = models.CharField(max_length=100, help_text="Ex: 6 mois, 1 an, Indéterminée")
    competences = models.TextField(help_text="Liste des compétences attendues")
    remuneration = models.CharField(max_length=100)

    def __str__(self):
        return self.titre
