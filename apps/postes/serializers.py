# postes/serializers.py

from rest_framework import serializers
from .models import Departement, Competence, Poste

# Serializers pour Departement (maintenant dans l'app postes)
class DepartementListSerializer(serializers.ModelSerializer):
    """
    Serializer pour la liste des départements (lecture simple).
    """
    class Meta:
        model = Departement
        fields = ['id', 'nom', 'code_id', 'responsable'] # Champs spécifiés dans votre code fourni

class DepartementCRUDSerializer(serializers.ModelSerializer):
    """
    Serializer pour le CRUD des départements.
    """
    class Meta:
        model = Departement
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


# Serializers pour Competence
class CompetenceListSerializer(serializers.ModelSerializer):
    """
    Serializer pour la liste des compétences (lecture simple).
    """
    class Meta:
        model = Competence
        fields = ['id', 'nom']

class CompetenceCRUDSerializer(serializers.ModelSerializer):
    """
    Serializer pour le CRUD des compétences.
    """
    class Meta:
        model = Competence
        fields = '__all__'


# Serializers pour Poste
class PosteListSerializer(serializers.ModelSerializer):
    """
    Serializer pour la liste des postes (lecture simple).
    Affiche les détails du département et les noms des compétences.
    """
    departement = DepartementListSerializer(read_only=True) # Affiche les détails du département
    competences = CompetenceListSerializer(many=True, read_only=True) # Affiche les noms des compétences

    class Meta:
        model = Poste
        fields = [
            'id', 'nom', 'departement', 'salaire_mensuel', 
            'niveau_experience', 'statut', 'lieu_travail', 'type_contrat',
            'competences'
        ]

class PosteCRUDSerializer(serializers.ModelSerializer):
    """
    Serializer pour le CRUD des postes.
    Gère la validation du nom du poste et les relations.
    """
    # Pour la création/mise à jour, on attend l'ID du département
    departement = serializers.PrimaryKeyRelatedField(queryset=Departement.objects.all())
    # Pour la création/mise à jour des compétences, on attend les IDs des compétences
    competences = serializers.PrimaryKeyRelatedField(queryset=Competence.objects.all(), many=True, required=False)

    class Meta:
        model = Poste
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at'] # Ces champs sont en lecture seule

    def validate_nom(self, value):
        """
        Valide l'unicité du nom du poste.
        """
        if self.instance and self.instance.nom == value:
            return value
        if Poste.objects.filter(nom=value).exists():
            raise serializers.ValidationError("Un poste avec ce nom existe déjà.")
        return value