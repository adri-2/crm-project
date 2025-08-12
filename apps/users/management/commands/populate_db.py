# users/management/commands/populate_db.py

import random
import datetime
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone
from faker import Faker

# Importez tous vos modèles. Notez le changement pour Departement et Competence
from apps.users.models import User
from apps.postes.models import Departement, Competence, Poste # Departement et Competence sont maintenant ici
from apps.employees.models import Employe
from apps.stage.models import Stagiaire, PeriodeStage
from apps.recruitment.models import OffreEmploi, Candidat

class Command(BaseCommand):
    """
    Commande Django pour peupler la base de données avec des données fictives.
    Utilise la bibliothèque Faker pour générer des informations réalistes.
    """
    help = 'Popule la base de données avec des données de test fictives.'

    def add_arguments(self, parser):
        """
        Ajoute des arguments optionnels à la commande.
        - --num_users: Nombre d'utilisateurs à créer (par défaut: 10)
        - --num_departements: Nombre de départements à créer (par défaut: 5)
        - --num_competences: Nombre de compétences à créer (par défaut: 10)
        - --num_postes: Nombre de postes à créer (par défaut: 15)
        - --num_employees: Nombre d'employés à créer (par défaut: 20)
        - --num_stagiaires: Nombre de stagiaires à créer (par défaut: 10)
        - --num_offres: Nombre d'offres d'emploi à créer (par défaut: 10)
        - --num_candidatures: Nombre de candidatures à créer (par défaut: 30)
        - --clear: Vide toutes les données existantes avant de populer
        """
        parser.add_argument(
            '--num_users',
            type=int,
            default=10,
            help='Nombre d\'utilisateurs à créer.',
        )
        parser.add_argument(
            '--num_departements',
            type=int,
            default=5,
            help='Nombre de départements à créer.',
        )
        parser.add_argument(
            '--num_competences',
            type=int,
            default=10,
            help='Nombre de compétences à créer.',
        )
        parser.add_argument(
            '--num_postes',
            type=int,
            default=15,
            help='Nombre de postes à créer.',
        )
        parser.add_argument(
            '--num_employees',
            type=int,
            default=20,
            help='Nombre d\'employés à créer.',
        )
        parser.add_argument(
            '--num_stagiaires',
            type=int,
            default=10,
            help='Nombre de stagiaires à créer.',
        )
        parser.add_argument(
            '--num_offres',
            type=int,
            default=10,
            help='Nombre d\'offres d\'emploi à créer.',
        )
        parser.add_argument(
            '--num_candidatures',
            type=int,
            default=30,
            help='Nombre de candidatures à créer.',
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Vide toutes les données existantes avant de populer.',
        )

    def handle(self, *args, **options):
        """
        Logique principale de la commande pour populer la base de données.
        """
        fake = Faker('fr_FR') # Utilise le locale français pour des données plus pertinentes

        num_users = options['num_users']
        num_departements = options['num_departements']
        num_competences = options['num_competences']
        num_postes = options['num_postes']
        num_employees = options['num_employees']
        num_stagiaires = options['num_stagiaires']
        num_offres = options['num_offres']
        num_candidatures = options['num_candidatures']
        clear_data = options['clear']

        self.stdout.write(self.style.SUCCESS('Démarrage du peuplement de la base de données...'))

        if clear_data:
            self.stdout.write(self.style.WARNING('Vidage des données existantes...'))
            self._clear_data()
            self.stdout.write(self.style.SUCCESS('Données existantes vidées avec succès.'))

        with transaction.atomic():
            self.stdout.write(self.style.MIGRATE_HEADING('Création des utilisateurs...'))
            users = self._create_users(fake, num_users)
            self.stdout.write(self.style.SUCCESS(f'{len(users)} utilisateurs créés.'))

            self.stdout.write(self.style.MIGRATE_HEADING('Création des départements...'))
            departements = self._create_departements(fake, num_departements)
            self.stdout.write(self.style.SUCCESS(f'{len(departements)} départements créés.'))

            self.stdout.write(self.style.MIGRATE_HEADING('Création des compétences...'))
            competences = self._create_competences(fake, num_competences)
            self.stdout.write(self.style.SUCCESS(f'{len(competences)} compétences créées.'))

            self.stdout.write(self.style.MIGRATE_HEADING('Création des postes...'))
            postes = self._create_postes(fake, num_postes, departements, competences)
            self.stdout.write(self.style.SUCCESS(f'{len(postes)} postes créés.'))

            self.stdout.write(self.style.MIGRATE_HEADING('Création des employés...'))
            employees = self._create_employees(fake, num_employees, users, postes)
            self.stdout.write(self.style.SUCCESS(f'{len(employees)} employés créés.'))

            self.stdout.write(self.style.MIGRATE_HEADING('Création des stagiaires...'))
            stagiaires = self._create_stagiaires(fake, num_stagiaires, postes, employees)
            self.stdout.write(self.style.SUCCESS(f'{len(stagiaires)} stagiaires créés.'))

            self.stdout.write(self.style.MIGRATE_HEADING('Création des périodes de stage...'))
            self._create_periodes_stage(fake, stagiaires, postes)
            self.stdout.write(self.style.SUCCESS('Périodes de stage créées.'))

            self.stdout.write(self.style.MIGRATE_HEADING('Création des offres d\'emploi...'))
            offres_emploi = self._create_offres_emploi(fake, num_offres, departements)
            self.stdout.write(self.style.SUCCESS(f'{len(offres_emploi)} offres d\'emploi créées.'))

            self.stdout.write(self.style.MIGRATE_HEADING('Création des candidatures...'))
            self._create_candidatures(fake, num_candidatures, offres_emploi)
            self.stdout.write(self.style.SUCCESS('Candidatures créées.'))

        self.stdout.write(self.style.SUCCESS('Peuplement de la base de données terminé avec succès !'))

    def _clear_data(self):
        """
        Vide toutes les tables des modèles que nous allons populer.
        L'ordre de suppression est important pour les clés étrangères.
        """
        Candidat.objects.all().delete()
        OffreEmploi.objects.all().delete()
        PeriodeStage.objects.all().delete()
        Stagiaire.objects.all().delete()
        Employe.objects.all().delete()
        # Supprime les postes, qui gèrent les ManyToMany avec Competence
        Poste.objects.all().delete() 
        Competence.objects.all().delete() # Supprime les compétences
        Departement.objects.all().delete() # Supprime les départements
        User.objects.filter(is_superuser=False).delete() # Ne supprime pas le superutilisateur créé manuellement

    def _create_users(self, fake, num_users):
        """Crée des utilisateurs avec différents rôles."""
        users = []
        roles = ['user', 'user', 'user', 'manager', 'rh', 'admin'] # Plus de users standards
        for i in range(num_users):
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = f"{first_name.lower()}{last_name.lower()}{i}"
            email = f"{username}@example.com"
            role = random.choice(roles)
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password='password123', # Mot de passe par défaut pour les tests
                    first_name=first_name,
                    last_name=last_name,
                    role=role
                )
                users.append(user)
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Erreur lors de la création de l'utilisateur {username}: {e}"))
        return users

    def _create_departements(self, fake, num_departements):
        """Crée des départements."""
        departements = []
        for _ in range(num_departements):
            try:
                departement = Departement.objects.create(
                    nom=fake.unique.job() + " Dept", # Utilise job() pour des noms de département variés
                    code_id=fake.unique.bothify(text='DPT###'),
                    responsable=fake.name(),
                    location=fake.address(),
                    phone=fake.phone_number(),
                    email=fake.email(),
                    description=fake.paragraph(nb_sentences=3)
                )
                departements.append(departement)
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Erreur lors de la création du département: {e}"))
        return departements

    def _create_competences(self, fake, num_competences):
        """Crée des compétences."""
        competences = []
        for _ in range(num_competences):
            try:
                competence = Competence.objects.create(
                    nom=fake.unique.word().capitalize() + " Skill",
                    description=fake.paragraph(nb_sentences=2)
                )
                competences.append(competence)
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Erreur lors de la création de la compétence: {e}"))
        return competences

    def _create_postes(self, fake, num_postes, departements, all_competences):
        """Crée des postes."""
        postes = []
        if not departements:
            self.stdout.write(self.style.ERROR("Aucun département disponible pour créer des postes."))
            return []

        for _ in range(num_postes):
            try:
                poste = Poste.objects.create(
                    nom=fake.unique.job(),
                    description=fake.paragraph(nb_sentences=4),
                    responsable=fake.name(),
                    departement=random.choice(departements),
                    salaire_mensuel=random.uniform(2000, 8000),
                    niveau_experience=random.choice([choice[0] for choice in Poste.NIVEAU_EXPERIENCE_CHOICES]),
                    # date_debut et date_fin sont commentés dans le modèle, donc ne les crée pas ici
                    lieu_travail=random.choice([choice[0] for choice in Poste.LIEU_CHOICES]),
                    type_contrat=random.choice([choice[0] for choice in Poste.CONTRAT_CHOICES])
                )
                # Ajoute des compétences aléatoires au poste
                if all_competences:
                    num_competences_for_poste = random.randint(1, min(5, len(all_competences)))
                    selected_competences = random.sample(all_competences, num_competences_for_poste)
                    poste.competences.set(selected_competences) # Utilise .set() pour ajouter les compétences
                
                postes.append(poste)
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Erreur lors de la création du poste: {e}"))
        return postes

    def _create_employees(self, fake, num_employees, users, postes):
        """Crée des employés."""
        employees = []
        if not users or not postes:
            self.stdout.write(self.style.ERROR("Utilisateurs ou postes manquants pour créer des employés."))
            return []

        available_users = list(User.objects.filter(employe__isnull=True)) # Utilisateurs non encore liés à un employé
        if len(available_users) < num_employees:
            self.stdout.write(self.style.WARNING(f"Seulement {len(available_users)} utilisateurs disponibles pour {num_employees} employés demandés. Création de moins d'employés."))
            num_employees = len(available_users)

        for i in range(num_employees):
            try:
                user = random.choice(available_users)
                available_users.remove(user) # Retire l'utilisateur pour éviter la duplication OneToOne

                employe = Employe.objects.create(
                    user=user,
                    matricule=fake.unique.bothify(text='EMP###??'),
                    poste=random.choice(postes),
                    type_contrat=random.choice([choice[0] for choice in Employe.CONTRAT_CHOICES]),
                    date_embauche=fake.date_between(start_date='-5y', end_date='today'),
                    adresse_personnelle=fake.address(),
                    tel_personnelle=fake.phone_number(),
                    niveau_scolaire=random.choice(['Baccalauréat', 'Licence', 'Master', 'Doctorat']),
                    champ_etude=fake.catch_phrase(),
                    etablissement=fake.company(),
                    tel_professionnel=fake.phone_number(),
                    email_professionnel=f"{user.username}@company.com",
                    email_personnel=user.email,
                    linkedin=fake.url(),
                    salaire_base=random.uniform(2500, 10000),
                    statut=random.choice([choice[0] for choice in Employe.STATUT_CHOICES]),
                    date_sortie=fake.date_between(start_date='today', end_date='+1y') if random.random() < 0.2 else None # 20% de chance d'avoir une date de sortie future
                )
                employees.append(employe)
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Erreur lors de la création de l'employé pour {user.username}: {e}"))
        
        # Assignation des chefs après la création de tous les employés
        for employe in employees:
            if random.random() < 0.5 and len(employees) > 1: # 50% de chance d'avoir un chef
                potential_chefs = [e for e in employees if e != employe]
                if potential_chefs:
                    employe.chef = random.choice(potential_chefs)
                    employe.save()
        return employees

    def _create_stagiaires(self, fake, num_stagiaires, postes, employees):
        """Crée des stagiaires."""
        stagiaires = []
        if not postes or not employees:
            self.stdout.write(self.style.ERROR("Postes ou employés manquants pour créer des stagiaires."))
            return []

        for _ in range(num_stagiaires):
            try:
                first_name = fake.first_name()
                last_name = fake.last_name()
                stagiaire = Stagiaire.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    matricule=fake.unique.bothify(text='STG###??'),
                    poste=random.choice(postes),
                    encadreur=random.choice(employees),
                    type_contrat=random.choice([choice[0] for choice in Stagiaire.CONTRAT_CHOICES]),
                    date_debut_stage=fake.date_between(start_date='-1y', end_date='today'),
                    adresse_personnelle=fake.address(),
                    tel_personnelle=fake.phone_number(),
                    niveau_scolaire=random.choice(['Bac', 'BTS', 'Licence', 'Master']),
                    champ_etude=fake.catch_phrase(),
                    etablissement=fake.university(),
                    tel_professionnel=fake.phone_number(),
                    email_professionnel=f"{first_name.lower()}.{last_name.lower()}@intern.com",
                    email_personnel=fake.email(),
                    linkedin=fake.url(),
                    salaire_base=random.uniform(500, 1500),
                    statut=random.choice([choice[0] for choice in Stagiaire.STATUT_CHOICES]),
                    date_fin_stage=fake.date_between(start_date='today', end_date='+6m')
                )
                stagiaires.append(stagiaire)
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Erreur lors de la création du stagiaire: {e}"))
        return stagiaires

    def _create_periodes_stage(self, fake, stagiaires, postes):
        """Crée des périodes de stage pour les stagiaires existants."""
        if not stagiaires or not postes:
            self.stdout.write(self.style.ERROR("Stagiaires ou postes manquants pour créer des périodes de stage."))
            return

        for stagiaire in stagiaires:
            # Crée 1 à 3 périodes de stage par stagiaire
            for _ in range(random.randint(1, 3)):
                try:
                    date_debut = fake.date_between(start_date='-1y', end_date='today')
                    date_fin = fake.date_between_dates(date_start=date_debut, date_end=date_debut + datetime.timedelta(days=random.randint(30, 365)))
                    PeriodeStage.objects.create(
                        stagiaire=stagiaire,
                        poste=random.choice(postes),
                        date_debut=date_debut,
                        date_fin=date_fin
                    )
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f"Erreur lors de la création d'une période de stage pour {stagiaire.first_name}: {e}"))

    def _create_offres_emploi(self, fake, num_offres, departements):
        """Crée des offres d'emploi."""
        offres = []
        if not departements:
            self.stdout.write(self.style.ERROR("Départements manquants pour créer des offres d'emploi."))
            return []

        for _ in range(num_offres):
            try:
                is_published = random.choice([True, False, False]) # Plus de chances d'être brouillon
                date_limit = fake.date_time_between(start_date='now', end_date='+6m', tzinfo=timezone.get_current_timezone())
                
                offre = OffreEmploi.objects.create(
                    titre=fake.job(),
                    description=fake.text(max_nb_chars=500),
                    date_limite=date_limit,
                    generee_par_ia=fake.boolean(chance_of_getting_true=20),
                    departement=random.choice(departements),
                    nombre_postes_voulus=random.randint(1, 5),
                    type_emploi=random.choice([choice[0] for choice in OffreEmploi.TYPE_EMPLOI_CHOICES]),
                    periode=f"{random.randint(3, 24)} mois" if random.random() < 0.7 else "Indéterminée",
                    competences=fake.text(max_nb_chars=200), # Ce champ est un TextField dans OffreEmploi, pas ManyToMany
                    remuneration=f"{random.randint(2000, 10000)} EUR/mois",
                    est_publiee=is_published
                )
                offres.append(offre)
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Erreur lors de la création de l'offre d'emploi: {e}"))
        return offres

    def _create_candidatures(self, fake, num_candidatures, offres_emploi):
        """Crée des candidatures."""
        if not offres_emploi:
            self.stdout.write(self.style.ERROR("Aucune offre d'emploi disponible pour créer des candidatures."))
            return

        for _ in range(num_candidatures):
            try:
                offre = random.choice(offres_emploi)
                nom_complet = fake.name()
                email = fake.email()
                
                # Vérifier l'unicité (email, offre) avant de créer
                # Tenter avec un autre email si le premier est déjà pris pour cette offre
                attempts = 0
                while Candidat.objects.filter(email=email, offre=offre).exists() and attempts < 5:
                    email = fake.unique.email()
                    attempts += 1
                
                if Candidat.objects.filter(email=email, offre=offre).exists():
                    self.stdout.write(self.style.WARNING(f"Impossible de créer une candidature unique pour {nom_complet} sur l'offre {offre.titre} après plusieurs tentatives. Skipping."))
                    continue # Passe à la prochaine itération si l'email alternatif est aussi pris

                Candidat.objects.create(
                    nom_complet=nom_complet,
                    email=email,
                    telephone=fake.phone_number(),
                    cv='cvs/dummy_cv.pdf', # Chemin de fichier factice
                    medium=random.choice(['LinkedIn', 'Indeed', 'Recommandation', 'Site Web Entreprise']),
                    score_cv_ia=random.uniform(0.1, 0.9) if fake.boolean(chance_of_getting_true=50) else None,
                    poste_vise=fake.job(),
                    statut=random.choice([choice[0] for choice in Candidat.STATUT_CHOICES]),
                    offre=offre
                )
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Erreur lors de la création de la candidature: {e}"))