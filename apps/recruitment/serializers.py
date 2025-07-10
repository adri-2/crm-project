# recruitment/serializers.py

from rest_framework import serializers
from django.utils import timezone # Pour gérer les dates et heures avec les fuseaux horaires
from .models import OffreEmploi, Candidat
from apps.postes.models import Departement,Poste, Competence # Importe le modèle Departement
from apps.postes.serializers import DepartementListSerializer # Importe son serializer

class OffreEmploiListSerializer(serializers.ModelSerializer):
    """
    Serializer pour la liste des offres d'emploi (lecture simple).
    Affiche le nom du département lié.
    """
    departement = DepartementListSerializer(read_only=True) # Affiche les détails du département
    poste = serializers.CharField(source='poste.titre', read_only=True) # Affiche le titre du poste
    competences = serializers.StringRelatedField(many=True, read_only=True) # Affiche les compétences requises

    class Meta:
        model = OffreEmploi
        fields = [
            'id', 'titre', 'description', 'date_limite', 'statut', 
            'departement', 'nombre_postes_voulus', 'type_emploi', 'remuneration','poste', 'competences',
            'est_publiee', 'date_creation'
        ]

class OffreEmploiCRUDSerializer(serializers.ModelSerializer):
    """
    Serializer pour le CRUD des offres d'emploi.
    Gère la validation des dates et le statut.
    """
    class Meta:
        model = OffreEmploi
        fields = '__all__' # Inclut tous les champs pour le CRUD
        # 'date_creation' est auto_now_add, 'statut' est géré par la méthode save du modèle
        read_only_fields = ['date_creation', 'statut'] 

    def validate_date_limite(self, value):
        """
        Valide que la date limite est dans le futur si l'offre est marquée comme publiée.
        """
        # Si c'est une mise à jour et que la date limite n'a pas changé, pas de validation supplémentaire
        if self.instance and self.instance.date_limite == value:
            return value

        # Si l'offre est ou sera publiée et que la date limite est passée, lève une erreur
        if self.initial_data.get('est_publiee', False) and value < timezone.now():
            raise serializers.ValidationError("La date limite doit être future si l'offre est publiée.")
        return value

class CandidatListSerializer(serializers.ModelSerializer):
    """
    Serializer pour la liste des candidats (lecture simple).
    Affiche le titre de l'offre d'emploi liée.
    """
    offre_titre = serializers.CharField(source='offre.titre', read_only=True) # Affiche le titre de l'offre

    class Meta:
        model = Candidat
        fields = [
            'id', 'nom_complet', 'email', 'telephone', 'offre', 'offre_titre', 
            'poste_vise', 'statut', 'created_at'
        ]

class CandidatCRUDSerializer(serializers.ModelSerializer):
    """
    Serializer pour le CRUD des candidats.
    Gère la validation de l'unicité de la candidature (email + offre).
    """
    class Meta:
        model = Candidat
        fields = '__all__' # Inclut tous les champs pour le CRUD
        read_only_fields = ['created_at', 'updated_at', 'score_cv_ia'] # Ces champs sont en lecture seule

    def validate(self, data):
        """
        Valide l'unicité de la candidature (email + offre).
        Empêche une même personne de postuler plusieurs fois à la même offre.
        """
        email = data.get('email')
        offre = data.get('offre')

        if email and offre:
            # Vérifie si une candidature existe déjà pour cet email et cette offre
            # Exclut l'instance actuelle lors d'une mise à jour pour ne pas déclencher une erreur sur soi-même
            if Candidat.objects.filter(email=email, offre=offre).exclude(pk=self.instance.pk if self.instance else None).exists():
                raise serializers.ValidationError(
                    {"non_field_errors": "Cet email a déjà postulé à cette offre d'emploi."}
                )
        return data