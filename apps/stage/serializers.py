from rest_framework import serializers
from .models import Stage, Stagiaire

class StageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ['id', 'titre', 'departement']

class StageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'

class StagiaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stagiaire
        fields = [
            'id', 'matricule', 'poste', 'first_name', 'last_name', 'username',
            'encadreur', 'contrat_type', 'date_joined', 'adresse_personnelle',
            'tel_personnelle', 'niveau_scolaire', 'champ_etude', 'etablissement',
            'tel_professionnel', 'email_professionnel', 'email_personnel',
            'linkedin', 'salaire_base', 'statut', 'date_sortie',
            'created_at', 'updated_at'
        ]

    def validate_matricule(self, value):
        if Stagiaire.objects.filter(matricule=value).exclude(pk=self.instance.pk if self.instance else None).exists():
            raise serializers.ValidationError("Ce matricule existe déjà.")
        return value

    def validate_email_professionnel(self, value):
        if value and Stagiaire.objects.filter(email_professionnel=value).exclude(pk=self.instance.pk if self.instance else None).exists():
            raise serializers.ValidationError("Cet email professionnel existe déjà.")
        return value

    def validate_email_personnel(self, value):
        if value and Stagiaire.objects.filter(email_personnel=value).exclude(pk=self.instance.pk if self.instance else None).exists():
            raise serializers.ValidationError("Cet email personnel existe déjà.")
        return value

    def validate_tel_personnelle(self, value):
        if value and not value.isdigit():
            raise serializers.ValidationError("Le téléphone personnel doit contenir uniquement des chiffres.")
        return value

    def validate_tel_professionnel(self, value):
        if value and not value.isdigit():
            raise serializers.ValidationError("Le téléphone professionnel doit contenir uniquement des chiffres.")
        return value

    def validate(self, attrs):
        # Exemple de vérification personnalisée
        if attrs.get('date_sortie') and attrs['date_sortie'] < attrs['date_joined']:
            raise serializers.ValidationError("La date de sortie ne peut pas être antérieure à la date d'embauche.")
        return attrs