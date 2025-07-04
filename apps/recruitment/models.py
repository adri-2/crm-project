from django.db import models
from django.urls import reverse

class OffreEmploi(models.Model):
    """
    Modèle représentant une offre d'emploi.
    """
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
    date_limite = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='brouillon')
    generee_par_ia = models.BooleanField(default=False)
    departement = models.CharField(max_length=100)
    nbre_voulue = models.PositiveIntegerField()
    type_emploi = models.CharField(max_length=20, choices=TYPE_EMPLOI_CHOICES)
    periode = models.CharField(max_length=100, help_text="Ex: 6 mois, 1 an, Indéterminée")
    competences = models.TextField(help_text="Liste des compétences attendues")
    remuneration = models.CharField(max_length=100)
    publiée = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Offre d'emploi"
        verbose_name_plural = "Offres d'emploi"
        ordering = ['-date_creation']

    def save(self, *args, **kwargs):
        self.change_status()
        super().save(*args, **kwargs)

    def change_status(self):
        """
        Met à jour le statut de l'offre selon sa publication et sa date limite.
        """
        from django.utils import timezone
        now = timezone.now()
        if self.publiée:
            self.status = 'publiée'
        elif self.date_limite < now:
            self.status = 'expirée'
        else:
            self.status = 'brouillon'
        return self.status

    @property
    def offres(self):
        """
        Retourne toutes les offres (ici, placeholder, à adapter selon relations).
        """
        return self.candidats.all()

    def get_absolute_url(self):
        """
        Retourne l'URL de détail de l'offre.
        """
        return reverse('offre_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.titre
    
    
#---------------------------------------#
# Modèle représentant un candidat
#---------------------------------------#  
    
    
    

class Candidat(models.Model):
    """
    Modèle représentant un candidat.
    """
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
    offre = models.ForeignKey(OffreEmploi,    on_delete=models.CASCADE,    related_name="candidats",    verbose_name="Offre liée")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Candidat"
        verbose_name_plural = "Candidats"
        ordering = ['-created_at', 'nom_complet']
        
        
    @property
    def myoffres(self):
        """
        Retourne toutes les offres (ici, placeholder, à adapter selon relations).
        """
        return self.offre.all()


    def __str__(self):
        return self.nom_complet

