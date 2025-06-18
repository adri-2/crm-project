from django.db import models

# Create your models here.
# --------------------
# Candidat
# --------------------
class Candidat(models.Model):
    STATUT_CHOICES = (
        ('nouveau', 'Nouveau'),
        ('entretien', 'Entretien'),
        ('accepté', 'Accepté'),
        ('rejeté', 'Rejeté'),
    )
    nom_complet = models.CharField(max_length=150)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    cv = models.FileField(upload_to='cvs/')
    medium = models.CharField(max_length=100, help_text="Ex: LinkedIn, Indeed, Recommandation, etc.")
    score_cv_ia = models.FloatField(null=True, blank=True)
    poste_vise = models.CharField(max_length=100)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='nouveau')

    def __str__(self):
        return self.nom_complet
