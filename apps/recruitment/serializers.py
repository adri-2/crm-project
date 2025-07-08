from rest_framework import serializers
from .models import OffreEmploi, Candidat

class OffreEmploiListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffreEmploi
        fields = ['id', 'titre', 'date_limite', 'status']

class OffreEmploiDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffreEmploi
        fields = '__all__'

class CandidatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidat
        fields = ['id', 'nom_complet', 'email', 'poste_vise', 'statut']

class CandidatDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidat
        fields = '__all__'


from rest_framework import serializers
from .models import Departement

class DepartementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = ['id', 'nom']

class DepartementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'