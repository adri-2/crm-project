# users/serializers.py

from rest_framework import serializers
from .models import User

class UserListSerializer(serializers.ModelSerializer):
    """
    Serializer pour la liste des utilisateurs (lecture simple).
    Affiche les informations de base de l'utilisateur.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']
        read_only_fields = fields # Tous les champs sont en lecture seule pour la liste

class UserCRUDSerializer(serializers.ModelSerializer):
    """
    Serializer pour le CRUD des utilisateurs.
    Permet de créer, lire, mettre à jour et supprimer des utilisateurs.
    Gère la validation du mot de passe lors de la création et la mise à jour.
    """
    # Le champ 'password' est en écriture seule et non requis pour les mises à jour partielles
    password = serializers.CharField(write_only=True, required=False) 

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'is_active', 'password']
        read_only_fields = ['id'] # L'ID est toujours en lecture seule

    def create(self, validated_data):
        """
        Crée un nouvel utilisateur avec un mot de passe haché.
        """
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        """
        Met à jour un utilisateur existant.
        Gère la mise à jour du mot de passe si fourni.
        """
        password = validated_data.pop('password', None)
        # Met à jour les autres champs
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Met à jour le mot de passe si un nouveau est fourni
        if password:
            instance.set_password(password)
        
        instance.save()
        return instance

    def validate_email(self, value):
        """
        Valide l'unicité de l'email.
        """
        # Si l'instance existe et que l'email n'a pas changé, pas de validation d'unicité
        if self.instance and self.instance.email == value:
            return value 
        # Vérifie si un autre utilisateur avec cet email existe déjà
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Cet email est déjà utilisé par un autre utilisateur.")
        return value