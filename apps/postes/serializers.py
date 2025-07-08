from rest_framework import serializers
from .models import Poste

class PosteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poste
        fields = ['id', 'titre', 'departement']

class PosteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poste
        fields = '__all__'

    def validate_titre(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Le titre ne peut pas être vide.")
        if len(value) < 3:
            raise serializers.ValidationError("Le titre doit contenir au moins 3 caractères.")
        return value

    def validate_departement(self, value):
        if not value:
            raise serializers.ValidationError("Le département doit être spécifié.")
        return value