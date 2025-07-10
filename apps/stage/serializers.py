# stage/serializers.py
from rest_framework import serializers
from .models import Stagiaire, PeriodeStage
from apps.postes.models import Poste # Importe le modèle Poste
from apps.postes.serializers import PosteListSerializer # Importe son serializer
from apps.employees.models import Employe # Importe le modèle Employe
from apps.employees.serializers import EmployeListSerializer # Importe son serializer

class StagiaireListSerializer(serializers.ModelSerializer):
    """
    Serializer pour la liste des stagiaires (lecture simple).
    Affiche les informations de l'encadreur et du poste.
    """
    encadreur = EmployeListSerializer(read_only=True) # Affiche les détails de l'encadreur
    poste = PosteListSerializer(read_only=True) # Affiche les détails du poste

    class Meta:
        model = Stagiaire
        fields = [
            'id', 'first_name', 'last_name', 'matricule', 'username',
            'poste', 'encadreur', 'type_contrat', 'date_debut_stage', 'statut'
        ]

class StagiaireCRUDSerializer(serializers.ModelSerializer):
    """
    Serializer pour le CRUD des stagiaires.
    Gère la validation des dates et l'unicité du matricule.
    """
    class Meta:
        model = Stagiaire
        fields = '__all__' # Inclut tous les champs pour le CRUD
        read_only_fields = ['username', 'created_at', 'updated_at'] # Ces champs sont en lecture seule

    def validate(self, data):
        """
        Valide les règles métier pour le stagiaire.
        - S'assure que la date de fin de stage est après la date de début de stage.
        """
        date_debut_stage = data.get('date_debut_stage')
        date_fin_stage = data.get('date_fin_stage')

        if date_debut_stage and date_fin_stage and date_fin_stage < date_debut_stage:
            raise serializers.ValidationError(
                {"date_fin_stage": "La date de fin de stage ne peut pas être antérieure à la date de début."}
            )
        return data

    def validate_matricule(self, value):
        """
        Valide l'unicité du matricule du stagiaire.
        """
        # Lors d'une mise à jour, si le matricule n'a pas changé, pas besoin de vérifier l'unicité
        if self.instance and self.instance.matricule == value:
            return value
        # Vérifie si un stagiaire avec ce matricule existe déjà
        if Stagiaire.objects.filter(matricule=value).exists():
            raise serializers.ValidationError("Ce matricule de stagiaire existe déjà.")
        return value

class PeriodeStageListSerializer(serializers.ModelSerializer):
    """
    Serializer pour la liste des périodes de stage (lecture simple).
    Affiche le nom du stagiaire et du poste associés.
    """
    stagiaire = StagiaireListSerializer(read_only=True) # Affiche les détails du stagiaire
    poste = PosteListSerializer(read_only=True) # Affiche les détails du poste

    class Meta:
        model = PeriodeStage
        fields = ['id', 'stagiaire', 'poste', 'date_debut', 'date_fin']

class PeriodeStageCRUDSerializer(serializers.ModelSerializer):
    """
    Serializer pour le CRUD des périodes de stage.
    Gère la validation des dates.
    """
    class Meta:
        model = PeriodeStage
        fields = '__all__' # Inclut tous les champs pour le CRUD
        read_only_fields = ['created_at', 'updated_at'] # Ces champs sont en lecture seule

    def validate(self, data):
        """
        Valide que la date de fin est après la date de début.
        """
        date_debut = data.get('date_debut')
        date_fin = data.get('date_fin')

        if date_debut and date_fin and date_fin < date_debut:
            raise serializers.ValidationError(
                {"date_fin": "La date de fin ne peut pas être antérieure à la date de début."}
            )
        return data