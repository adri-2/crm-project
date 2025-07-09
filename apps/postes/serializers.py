# departement/serializers.py

from rest_framework import serializers
from .models import Departement, Poste

class DepartementListSerializer(serializers.ModelSerializer):
    """
    Serializer pour la liste des départements (lecture simple).
    """
    class Meta:
        model = Departement
        fields = ['id', 'nom','code_id','responsable','description'] # N'affiche que l'ID et le nom pour la liste

class DepartementCRUDSerializer(serializers.ModelSerializer):
    """
    Serializer pour le CRUD des départements.
    Permet de créer, lire, mettre à jour et supprimer des départements.
    """
    class Meta:
        model = Departement
        fields = '__all__' # Inclut tous les champs du modèle
        read_only_fields = ['created_at', 'updated_at'] # Ces champs sont gérés automatiquement par Django
        
        
        
# postes/serializers.py


"""
    Serializer pour les détails d'un poste.
    Inclut tous les champs du modèle Poste et affiche le département avec ses détails.          
"""

class PosteListSerializer(serializers.ModelSerializer):
    """
    Serializer pour la liste des postes (lecture simple).
    Affiche le nom du département en utilisant un serializer imbriqué.
    """
    departement = DepartementListSerializer(read_only=True) # Affiche les détails du département

    class Meta:
        model = Poste
        fields = [
            'id', 'nom', 'departement', 'salaire_mensuel', 
            'niveau_experience', 'statut', 'lieu_travail', 'type_contrat'
        ]




class PosteCRUDSerializer(serializers.ModelSerializer):
    """
    Serializer pour le CRUD des postes.
    Gère la validation des dates et l'unicité du nom du poste.
    """
    class Meta:
        model = Poste
        fields = '__all__' # Inclut tous les champs pour le CRUD
        read_only_fields = ['created_at', 'updated_at'] # Ces champs sont en lecture seule

    def validate(self, data):
        """
        Valide que la date de fin est après la date de début si les deux sont présentes.
        """
        date_debut = data.get('date_debut')
        date_fin = data.get('date_fin')

        if date_debut and date_fin and date_fin < date_debut:
            raise serializers.ValidationError(
                {"date_fin": "La date de fin ne peut pas être antérieure à la date de début."}
            )
        return data

    def validate_nom(self, value):
        """
        Valide l'unicité du nom du poste.
        """
        # Lors d'une mise à jour, si le nom n'a pas changé, pas besoin de vérifier l'unicité
        if self.instance and self.instance.nom == value:
            return value
        # Vérifie si un poste avec ce nom existe déjà
        if Poste.objects.filter(nom=value).exists():
            raise serializers.ValidationError("Un poste avec ce nom existe déjà.")
        return value       