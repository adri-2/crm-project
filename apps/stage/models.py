from django.db import models
from django.conf import settings
from  apps.employees.models import Employe
from django.urls import reverse
from  apps.postes.models import Poste
from django.utils.text import slugify

class PeriodeStage(models.Model):
    date_start = models.DateField(verbose_name="Date de Debut")
    date_end = models.DateField(verbose_name="Date de Fin")
    stagiaire = models.ForeignKey('Stagiaire',on_delete=models.PROTECT)
    poste = models.ForeignKey(Poste,on_delete=models.PROTECT)
    nombre_stagiaire = models.DecimalField(max_digits=10, decimal_places=0,)
    def save(self,*args,**kwargs):
        
        self.nombre_stagiaire += 1
        super().save(*args,**kwargs)
    

class Stagiaire(models.Model):
    CONTRAT_CHOICES = (
        ('Stage Académique', 'Stage Académique'),
        ('Stage Professionnel', 'Stage Professionnel'),
        ('Stage Réemployé', 'Stage Réemployé'),
    )
    STATUT_CHOICES = (
        ('actif', 'Actif'),
        ('inactif', 'Inactif'),
    )

    # user = models.OneToOneField(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     verbose_name="Utilisateur"
    # )
    matricule = models.CharField(max_length=20, unique=True, verbose_name="Matricule")
    poste = models.CharField(max_length=100, verbose_name="Poste")
    # username = models.CharField(max_length=20, unique=True, verbose_name="Nom complet")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,unique=True,blank=True)
    
    encadreur = models.ForeignKey(
        Employe,
        on_delete=models.PROTECT,
        related_name="stagiaires_encadres",
        verbose_name="Encadreur"
    )
    contrat_type = models.CharField(max_length=30, choices=CONTRAT_CHOICES, verbose_name="Type de contrat")
    date_joined = models.DateField(verbose_name="Date d'embauche")
    matricule = models.CharField(max_length=20, unique=True, verbose_name="Matricule")
    poste = models.ForeignKey(Poste, on_delete=models.PROTECT, verbose_name="Poste")
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
    # last_login
    # is_active

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['user__last_name', 'user__first_name']
        verbose_name = "Stagiaire"
        verbose_name_plural = "Stagiaires"
        
        
      
    def save(self,*args,**kwargs):
        
        if not self.username:
            username = slugify(f"{self.first_name} {self.last_name}")
            ex = __class__.objects.filter(username=username).exists()
            
            while ex:
                i = len(__class__.objects.filter(first_name=self.first_name,last_name=self.last_name))
                username = slugify(f'{self.first_name} {self.last_name} copie {i+1}')
                ex = __class__.objects.filter(username=username).exists()
            self.username = username
        super().save(*args,**kwargs)
       

    def get_absolute_url(self):
        return reverse('stagiaire_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.matricule})"
