# employees/serializers.py

from rest_framework import serializers
from .models import Employe
from apps.users.models import User # Importe le modèle User
from apps.users.serializers import UserListSerializer # Importe le serializer User
from apps.postes.models import Poste # Importe le modèle Poste
from apps.postes.serializers import PosteListSerializer # Importe son serializer

class EmployeListSerializer(serializers.ModelSerializer):
    """
    Serializer pour la liste des employés (lecture simple).
    Affiche les informations de l'utilisateur lié, du poste et le nom complet du chef.
    """
    user = UserListSerializer(read_only=True) # Affiche les détails de l'utilisateur lié
    poste = PosteListSerializer(read_only=True) # Affiche les détails du poste lié
    chef_nom_complet = serializers.SerializerMethodField() # Champ calculé pour le nom du chef

    class Meta:
        model = Employe
        fields = [
            'id', 'matricule', 'user', 'poste', 'chef_nom_complet',
            'type_contrat', 'date_embauche', 'statut'
        ]

    def get_chef_nom_complet(self, obj):
        """
        Méthode pour obtenir le nom complet du chef.
        Retourne None si le chef n'existe pas.
        """
        if obj.chef and obj.chef.user:
            return obj.chef.user.get_full_name()
        return None

class EmployeCRUDSerializer(serializers.ModelSerializer):
    """
    Serializer pour le CRUD des employés.
    Permet de lier un utilisateur existant et gère les validations.
    """
    # Le champ 'user' est une clé étrangère qui attend l'ID d'un utilisateur existant
    # Le queryset est défini dynamiquement dans __init__ pour éviter les problèmes de dépendance circulaire
    user = serializers.PrimaryKeyRelatedField(queryset=Employe.objects.all(), required=True) 

    class Meta:
        model = Employe
        fields = '__all__' # Inclut tous les champs pour le CRUD
        read_only_fields = ['created_at', 'updated_at'] # Ces champs sont en lecture seule

    def __init__(self, *args, **kwargs):
        """
        Initialise le serializer et définit dynamiquement le queryset pour le champ 'user'.
        """
        super().__init__(*args, **kwargs)
        # Importe le modèle User ici pour éviter les problèmes d'importation circulaire au niveau global
        from users.models import User
        self.fields['user'].queryset = User.objects.all() # Permet de sélectionner n'importe quel utilisateur existant

    def validate(self, data):
        """
        Valide les règles métier pour l'employé.
        - S'assure que la date de sortie est après la date d'embauche.
        - Vérifie qu'un utilisateur n'est pas déjà associé à un autre employé.
        """
        date_embauche = data.get('date_embauche')
        date_sortie = data.get('date_sortie')

        if date_embauche and date_sortie and date_sortie < date_embauche:
            raise serializers.ValidationError(
                {"date_sortie": "La date de sortie ne peut pas être antérieure à la date d'embauche."}
            )
        
        # Vérifie si l'utilisateur est déjà associé à un employé existant
        user = data.get('user')
        if user:
            # Exclut l'instance actuelle lors d'une mise à jour pour ne pas déclencher une erreur sur soi-même
            existing_employe = Employe.objects.filter(user=user)
            if self.instance: # Si c'est une mise à jour
                existing_employe = existing_employe.exclude(pk=self.instance.pk)
            
            if existing_employe.exists():
                raise serializers.ValidationError({"user": "Cet utilisateur est déjà associé à un autre employé."})

        return data

    def validate_matricule(self, value):
        """
        Valide l'unicité du matricule de l'employé.
        """
        # Lors d'une mise à jour, si le matricule n'a pas changé, pas besoin de vérifier l'unicité
        if self.instance and self.instance.matricule == value:
            return value
        # Vérifie si un employé avec ce matricule existe déjà
        if Employe.objects.filter(matricule=value).exists():
            raise serializers.ValidationError("Ce matricule existe déjà pour un autre employé.")
        return value