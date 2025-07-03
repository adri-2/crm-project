<template>
  <div
    class="flex flex-col p-6 bg-white rounded-lg shadow-xl drop-shadow min-h-[500px]"
    :class="{ 'w-full': !isMobile, 'min-w-[800px]': !isMobile }"
  >
    <div
      class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6 gap-4 sm:gap-0"
    >
      <div>
        <h2 class="text-2xl font-bold text-gray-800 mb-1">Candidatures</h2>
        <p class="text-sm text-gray-600 max-w-lg">
          Liste complète des candidatures avec les informations détaillées du
          candidat et leur statut actuel.
        </p>
      </div>

      <RouterLink
        to="/recruitment/candidates/new"
        class="inline-flex items-center px-5 py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white font-medium rounded-md text-sm transition-colors duration-200 ease-in-out shadow-md hover:shadow-lg"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-4 w-4 mr-2"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          stroke-width="2"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M12 4v16m8-8H4"
          />
        </svg>
        Nouvelle Candidature
      </RouterLink>
    </div>

    <div class="mb-4 flex flex-col sm:flex-row gap-4">
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Rechercher par nom, poste, email..."
        class="flex-1 px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-sm"
      />
      <select
        v-model="filterStatus"
        class="px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-sm"
      >
        <option value="">Tous les statuts</option>
        <option
          v-for="status in availableStatuses"
          :key="status"
          :value="status"
        >
          {{ status }}
        </option>
      </select>
      <select
        v-model="filterPosition"
        class="px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-sm"
      >
        <option value="">Tous les postes</option>
        <option
          v-for="position in availablePositions"
          :key="position"
          :value="position"
        >
          {{ position }}
        </option>
      </select>
    </div>

    <div v-if="loading" class="h-full w-full flex items-center justify-center">
      <p class="text-gray-500">Chargement des candidatures...</p>
    </div>
    <div
      v-else-if="error"
      class="h-full w-full flex items-center justify-center"
    >
      <p class="text-red-500">
        Erreur lors du chargement des données : {{ error }}
      </p>
    </div>
    <div
      v-else-if="filteredCandidats.length === 0"
      class="h-full w-full flex items-center justify-center"
    >
      <p class="text-gray-500">
        Aucune candidature trouvée pour les critères sélectionnés.
      </p>
    </div>
    <div
      v-else
      class="overflow-x-auto overflow-y-auto bg-white flex flex-col grow border border-gray-200 rounded-lg"
    >
      <table
        class="min-w-full text-sm text-left text-gray-700 divide-y divide-gray-200"
      >
        <thead
          class="bg-gray-50 text-xs uppercase text-gray-500 sticky top-0 z-10"
        >
          <tr>
            <th class="px-6 py-3 font-medium tracking-wider">
              Nom du Candidat
            </th>
            <th class="px-6 py-3 font-medium tracking-wider">Postulé le</th>
            <th class="px-6 py-3 font-medium tracking-wider">Poste</th>
            <th class="px-6 py-3 font-medium tracking-wider">Statut</th>
            <th class="px-6 py-3 font-medium tracking-wider">Raison refus</th>
            <th class="px-6 py-3 font-medium tracking-wider">Évaluation</th>
            <th class="px-6 py-3 font-medium tracking-wider">Email</th>
            <th class="px-6 py-3 font-medium tracking-wider">Téléphone</th>
            <th class="px-6 py-3 font-medium tracking-wider">Recruteur</th>
            <th class="px-6 py-3 font-medium tracking-wider">
              Source / Médium
            </th>
            <th class="px-6 py-3 font-medium tracking-wider">Étiquettes</th>
            <th class="px-6 py-3 font-medium tracking-wider text-right">
              Actions
            </th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200">
          <tr
            v-for="app in paginatedCandidat"
            :key="app.id"
            class="hover:bg-gray-50 transition-colors duration-150 ease-in-out"
          >
            <td class="px-6 py-4 font-medium text-gray-900 flex items-center">
              <img
                :src="app.avatar"
                alt="Avatar"
                class="h-8 w-8 rounded-full mr-3 object-cover"
                v-if="app.avatar"
              />
              {{ app.name }}
            </td>
            <td class="px-6 py-4">{{ formatDate(app.applied_at) }}</td>
            <td class="px-6 py-4">{{ app.position }}</td>
            <td class="px-6 py-4">
              <span :class="statusBadgeClass(app.status)">
                {{ app.status }}
              </span>
            </td>
            <td class="px-6 py-4 text-red-600">
              {{ app.rejection_reason || '-' }}
            </td>
            <td class="px-6 py-4">{{ app.evaluation || '-' }}</td>
            <td class="px-6 py-4">{{ app.email }}</td>
            <td class="px-6 py-4">{{ app.phone || '-' }}</td>
            <td class="px-6 py-4">{{ app.recruiter || '-' }}</td>
            <td class="px-6 py-4">
              {{ app.source || '-' }} / {{ app.medium || '-' }}
            </td>
            <td class="px-6 py-4">
              <div class="flex flex-wrap gap-1">
                <span
                  v-for="tag in app.tags"
                  :key="tag"
                  class="bg-gray-100 text-gray-700 px-2 py-0.5 rounded-full text-xs font-medium"
                >
                  {{ tag }}
                </span>
                <span v-if="app.tags.length === 0">-</span>
              </div>
            </td>
            <td class="px-6 py-4 text-right">
              <button
                @click="viewCandidature(app.id)"
                class="text-indigo-600 hover:text-indigo-800 font-medium cursor-pointer hover:underline text-sm"
              >
                Voir
              </button>
              <button
                @click="editCandidature(app.id)"
                class="ml-4 text-gray-600 hover:text-gray-800 font-medium cursor-pointer hover:underline text-sm"
              >
                Éditer
              </button>
              <button
                @click="confirmDeleteCandidature(app.id)"
                class="ml-4 text-red-600 hover:text-red-800 font-medium cursor-pointer hover:underline text-sm"
              >
                Supprimer
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div
      class="mt-6 flex flex-col sm:flex-row justify-between items-center shrink-0"
    >
      <p class="text-sm text-gray-700 mb-2 sm:mb-0">
        Affichage de
        <span class="font-medium">{{ startIndex + 1 }}</span>
        à
        <span class="font-medium">{{ endIndex }}</span>
        sur
        <span class="font-medium">{{ filteredCandidats.length }}</span>
        résultats
      </p>
      <div class="flex gap-2">
        <button
          @click="goToPage(currentPage - 1)"
          :disabled="currentPage === 1"
          class="px-4 py-2 text-sm rounded-md border border-gray-300 text-gray-700 hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-150 ease-in-out"
        >
          Précédent
        </button>
        <div class="flex gap-1">
          <button
            v-for="page in visiblePages"
            :key="page"
            @click="goToPage(page)"
            :class="[
              'px-4 py-2 text-sm rounded-md border',
              page === currentPage
                ? 'bg-indigo-600 text-white border-indigo-600 shadow-sm'
                : 'border-gray-300 text-gray-700 hover:bg-gray-100'
            ]"
          >
            {{ page }}
          </button>
        </div>
        <button
          @click="goToPage(currentPage + 1)"
          :disabled="currentPage === totalPages"
          class="px-4 py-2 text-sm rounded-md border border-gray-300 text-gray-700 hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-150 ease-in-out"
        >
          Suivant
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue';
import { RouterLink } from 'vue-router'; // Assurez-vous que vue-router est bien installé et configuré

// --- Données et États ---
const perPage = 10; // Nombre de candidatures par page
const currentPage = ref(1); // Page actuelle de la pagination
const searchQuery = ref(''); // Terme de recherche
const filterStatus = ref(''); // Filtre par statut
const filterPosition = ref(''); // Filtre par poste
const loading = ref(true); // État de chargement des données
const error = ref(null); // Message d'erreur
const isMobile = ref(false); // Pour adapter le min-width sur mobile

// Données des candidatures (simulées - à remplacer par un appel API)
const candidats = ref([]); // Initialement vide, sera rempli par fetchData

// --- Détection Mobile (pour ajuster le style si besoin) ---
onMounted(() => {
  checkIfMobile();
  window.addEventListener('resize', checkIfMobile);
  fetchCandidatures(); // Récupère les candidatures au montage du composant
});

const checkIfMobile = () => {
  isMobile.value = window.innerWidth < 768; // Exemple pour les écrans < md
};

// --- Logique de Récupération des Candidatures ---
const fetchCandidatures = async () => {
  loading.value = true;
  error.value = null;
  try {
    // --- SIMULATION D'APPEL API ---
    // En production, vous feriez un appel à votre API Django ici
    // Exemple avec fetch :
    // const response = await fetch('/api/candidatures/');
    // if (!response.ok) throw new Error('Échec de la récupération des candidatures.');
    // const data = await response.json();
    // candidats.value = data;

    // Données fictives pour la démo
    await new Promise(resolve => setTimeout(resolve, 800)); // Simule un délai réseau
    candidats.value = [
      {
        id: 1,
        name: "Jean Dupont",
        applied_at: "2025-05-10",
        position: "Développeur Backend",
        status: "En cours",
        rejection_reason: "",
        evaluation: "4.5/5",
        email: "jean.dupont@example.com",
        tags: ["PHP", "Symfony", "Expérimenté"],
        recruiter: "Sophie Martin",
        phone: "+33 6 12 34 56 78",
        medium: "LinkedIn",
        source: "Annonce en ligne",
        avatar: 'https://randomuser.me/api/portraits/men/1.jpg'
      },
      {
        id: 2,
        name: "Fatou Ndiaye",
        applied_at: "2025-05-05",
        position: "Chargée RH",
        status: "Refusé",
        rejection_reason: "Manque d'expérience",
        evaluation: "3/5",
        email: "fatou.ndiaye@example.com",
        tags: ["Junior", "Motivée"],
        recruiter: "David Kamga",
        phone: "+221 77 123 45 67",
        medium: "Site entreprise",
        source: "Cooptation",
        avatar: 'https://randomuser.me/api/portraits/women/2.jpg'
      },
      {
        id: 3,
        name: "Ali Bongo",
        applied_at: "2025-04-28",
        position: "Designer UI",
        status: "Accepté",
        rejection_reason: "",
        evaluation: "5/5",
        email: "ali.bongo@example.com",
        tags: ["UI/UX", "React", "Disponible"],
        recruiter: "Léa Traoré",
        phone: "+241 06 00 00 00",
        medium: "Indeed",
        source: "Stage précédent",
        avatar: 'https://randomuser.me/api/portraits/men/3.jpg'
      },
      {
        id: 4,
        name: "Amélie Dubois",
        applied_at: "2025-06-01",
        position: "Chef de Projet IT",
        status: "Entretien",
        rejection_reason: "",
        evaluation: "4/5",
        email: "amelie.dubois@example.com",
        tags: ["Agile", "Scrum"],
        recruiter: "Sophie Martin",
        phone: "+33 7 98 76 54 32",
        medium: "Recommandation",
        source: "Bouche-à-oreille",
        avatar: 'https://randomuser.me/api/portraits/women/4.jpg'
      },
      {
        id: 5,
        name: "Marc Durand",
        applied_at: "2025-05-20",
        position: "Consultant SEO",
        status: "En attente",
        rejection_reason: "",
        evaluation: "",
        email: "marc.durand@example.com",
        tags: ["SEO", "Marketing"],
        recruiter: "David Kamga",
        phone: "+33 6 54 32 10 98",
        medium: "Indeed",
        source: "CVthèque",
        avatar: 'https://randomuser.me/api/portraits/men/5.jpg'
      },
      {
        id: 6,
        name: "Sarah Leclerc",
        applied_at: "2025-04-15",
        position: "Développeur Frontend",
        status: "Refusé",
        rejection_reason: "Profil pas adapté",
        evaluation: "2.5/5",
        email: "sarah.leclerc@example.com",
        tags: ["VueJS", "Junior"],
        recruiter: "Léa Traoré",
        phone: "+33 6 99 88 77 66",
        medium: "LinkedIn",
        source: "Annonce en ligne",
        avatar: 'https://randomuser.me/api/portraits/women/6.jpg'
      },
      {
        id: 7,
        name: "Kevin Dubois",
        applied_at: "2025-06-15",
        position: "Data Scientist",
        status: "Nouveau",
        rejection_reason: "",
        evaluation: "",
        email: "kevin.dubois@example.com",
        tags: ["Python", "Machine Learning"],
        recruiter: "Sophie Martin",
        phone: "+33 6 11 22 33 44",
        medium: "Plateforme recrutement",
        source: "Candidature spontanée",
        avatar: 'https://randomuser.me/api/portraits/men/7.jpg'
      },
      {
        id: 8,
        name: "Léa Morel",
        applied_at: "2025-06-10",
        position: "UX Designer",
        status: "En cours",
        rejection_reason: "",
        evaluation: "4/5",
        email: "lea.morel@example.com",
        tags: ["Figma", "Design System"],
        recruiter: "David Kamga",
        phone: "+33 6 77 66 55 44",
        medium: "Dribbble",
        source: "Portfolio",
        avatar: 'https://randomuser.me/api/portraits/women/8.jpg'
      },
      {
        id: 9,
        name: "Ahmed Khan",
        applied_at: "2025-05-25",
        position: "Ingénieur DevOps",
        status: "Entretien",
        rejection_reason: "",
        evaluation: "4.5/5",
        email: "ahmed.khan@example.com",
        tags: ["Docker", "Kubernetes"],
        recruiter: "Léa Traoré",
        phone: "+33 6 55 44 33 22",
        medium: "Jobboard",
        source: "Recherche proactive",
        avatar: 'https://randomuser.me/api/portraits/men/9.jpg'
      },
      {
        id: 10,
        name: "Chloé Lefevre",
        applied_at: "2025-05-18",
        position: "Responsable Commercial",
        status: "En attente",
        rejection_reason: "",
        evaluation: "",
        email: "chloe.lefevre@example.com",
        tags: ["Vente", "B2B"],
        recruiter: "Sophie Martin",
        phone: "+33 6 33 22 11 00",
        medium: "LinkedIn",
        source: "Annonce en ligne",
        avatar: 'https://randomuser.me/api/portraits/women/10.jpg'
      },
       {
        id: 11,
        name: "Louis Moreau",
        applied_at: "2025-05-12",
        position: "Développeur Fullstack",
        status: "En cours",
        rejection_reason: "",
        evaluation: "4/5",
        email: "louis.moreau@example.com",
        tags: ["NodeJS", "React", "Senior"],
        recruiter: "David Kamga",
        phone: "+33 6 45 67 89 01",
        medium: "GitHub",
        source: "Profil en ligne",
        avatar: 'https://randomuser.me/api/portraits/men/11.jpg'
      },
      {
        id: 12,
        name: "Manon Roussel",
        applied_at: "2025-06-03",
        position: "Chargée de Communication",
        status: "Nouveau",
        rejection_reason: "",
        evaluation: "",
        email: "manon.roussel@example.com",
        tags: ["Marketing Digital", "Réseaux Sociaux"],
        recruiter: "Léa Traoré",
        phone: "+33 6 23 45 67 89",
        medium: "Indeed",
        source: "Candidature spontanée",
        avatar: 'https://randomuser.me/api/portraits/women/12.jpg'
      },
       {
        id: 13,
        name: "Hugo Bernard",
        applied_at: "2025-05-29",
        position: "Comptable",
        status: "En cours",
        rejection_reason: "",
        evaluation: "3.5/5",
        email: "hugo.bernard@example.com",
        tags: ["Expert", "Sage"],
        recruiter: "Sophie Martin",
        phone: "+33 6 98 76 54 32",
        medium: "Recommandation",
        source: "Partenaire",
        avatar: 'https://randomuser.me/api/portraits/men/13.jpg'
      },
      {
        id: 14,
        name: "Emma Laurent",
        applied_at: "2025-05-01",
        position: "Assistant Administratif",
        status: "Refusé",
        rejection_reason: "Compétences linguistiques insuffisantes",
        evaluation: "2/5",
        email: "emma.laurent@example.com",
        tags: ["Bureautique"],
        recruiter: "David Kamga",
        phone: "+33 6 87 65 43 21",
        medium: "Pôle Emploi",
        source: "Annonce en ligne",
        avatar: 'https://randomuser.me/api/portraits/women/14.jpg'
      },
      {
        id: 15,
        name: "Lucas Garcia",
        applied_at: "2025-06-20",
        position: "Architecte Logiciel",
        status: "Nouveau",
        rejection_reason: "",
        evaluation: "",
        email: "lucas.garcia@example.com",
        tags: ["Cloud", "Microservices"],
        recruiter: "Léa Traoré",
        phone: "+33 6 76 54 32 10",
        medium: "LinkedIn",
        source: "Chasse",
        avatar: 'https://randomuser.me/api/portraits/men/15.jpg'
      },
      {
        id: 16,
        name: "Jade Petit",
        applied_at: "2025-06-18",
        position: "Chef de Produit",
        status: "Entretien",
        rejection_reason: "",
        evaluation: "4.8/5",
        email: "jade.petit@example.com",
        tags: ["Product Management", "SaaS"],
        recruiter: "Sophie Martin",
        phone: "+33 6 65 43 21 09",
        medium: "Referral",
        source: "Employé",
        avatar: 'https://randomuser.me/api/portraits/women/16.jpg'
      },
      {
        id: 17,
        name: "Gabriel Rousseau",
        applied_at: "2025-05-08",
        position: "Technicien Support",
        status: "En attente",
        rejection_reason: "",
        evaluation: "",
        email: "gabriel.rousseau@example.com",
        tags: ["Support IT", "Bilingue"],
        recruiter: "David Kamga",
        phone: "+33 6 54 32 10 98",
        medium: "Indeed",
        source: "Annonce en ligne",
        avatar: 'https://randomuser.me/api/portraits/men/17.jpg'
      },
      {
        id: 18,
        name: "Lina Martin",
        applied_at: "2025-06-05",
        position: "Graphiste",
        status: "Accepté",
        rejection_reason: "",
        evaluation: "4.7/5",
        email: "lina.martin@example.com",
        tags: ["Photoshop", "Illustrator"],
        recruiter: "Léa Traoré",
        phone: "+33 6 34 56 78 90",
        medium: "Behance",
        source: "Portfolio",
        avatar: 'https://randomuser.me/api/portraits/women/18.jpg'
      },
      {
        id: 19,
        name: "Noah Dubois",
        applied_at: "2025-05-16",
        position: "Développeur Mobile",
        status: "En cours",
        rejection_reason: "",
        evaluation: "4.2/5",
        email: "noah.dubois@example.com",
        tags: ["iOS", "Android", "Swift"],
        recruiter: "Sophie Martin",
        phone: "+33 6 21 09 87 65",
        medium: "LinkedIn",
        source: "Contact direct",
        avatar: 'https://randomuser.me/api/portraits/men/19.jpg'
      },
      {
        id: 20,
        name: "Clara Lambert",
        applied_at: "2025-06-08",
        position: "Analyste Financier",
        status: "Entretien",
        rejection_reason: "",
        evaluation: "4.1/5",
        email: "clara.lambert@example.com",
        tags: ["Excel", "Finance"],
        recruiter: "David Kamga",
        phone: "+33 6 90 87 65 43",
        medium: "Jobboard",
        source: "Annonce en ligne",
        avatar: 'https://randomuser.me/api/portraits/women/20.jpg'
      },
    ];
  } catch (e) {
    error.value = `Impossible de charger les candidatures: ${e.message}`;
    console.error(e);
  } finally {
    loading.value = false;
  }
};

// --- Logique de Filtrage et Recherche ---
const filteredCandidats = computed(() => {
  let filtered = candidats.value;

  // Appliquer le filtre de recherche
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase();
    filtered = filtered.filter(app =>
      app.name.toLowerCase().includes(query) ||
      app.position.toLowerCase().includes(query) ||
      app.email.toLowerCase().includes(query) ||
      app.recruiter.toLowerCase().includes(query) ||
      app.tags.some(tag => tag.toLowerCase().includes(query)) // Recherche dans les tags
    );
  }

  // Appliquer le filtre de statut
  if (filterStatus.value) {
    filtered = filtered.filter(app => app.status === filterStatus.value);
  }

  // Appliquer le filtre de poste
  if (filterPosition.value) {
    filtered = filtered.filter(app => app.position === filterPosition.value);
  }

  return filtered;
});

// Récupérer tous les statuts uniques pour le filtre
const availableStatuses = computed(() => {
  const statuses = new Set(candidats.value.map(app => app.status));
  return Array.from(statuses).sort();
});

// Récupérer tous les postes uniques pour le filtre
const availablePositions = computed(() => {
  const positions = new Set(candidats.value.map(app => app.position));
  return Array.from(positions).sort();
});

// --- Logique de Pagination ---
const totalPages = computed(() => Math.ceil(filteredCandidats.value.length / perPage));

const paginatedCandidat = computed(() => {
  const start = (currentPage.value - 1) * perPage;
  return filteredCandidats.value.slice(start, start + perPage);
});

const startIndex = computed(() => (currentPage.value - 1) * perPage);
const endIndex = computed(() =>
  Math.min(currentPage.value * perPage, filteredCandidats.value.length)
);

// Pages visibles dans la pagination (ex: 1 2 3 4 5)
const visiblePages = computed(() => {
  const pages = [];
  const maxVisible = 5; // Nombre max de boutons de page à afficher
  let start = Math.max(1, currentPage.value - Math.floor(maxVisible / 2));
  let end = Math.min(totalPages.value, start + maxVisible - 1);

  // Ajustement si on est proche des limites
  if (end - start + 1 < maxVisible) {
    start = Math.max(1, end - maxVisible + 1);
  }

  for (let i = start; i <= end; i++) {
    pages.push(i);
  }
  return pages;
});

// Naviguer vers une page spécifique
function goToPage(page) {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
}

// Réinitialiser la page courante si les filtres réduisent le nombre total de pages
watch([filteredCandidats, perPage], () => {
  if (currentPage.value > totalPages.value) {
    currentPage.value = 1;
  }
}, { immediate: true }); // immediate: true pour s'assurer que cela s'exécute au premier chargement si filteredCandidats est vide au début


// --- Logique des Actions sur Candidature ---
const viewCandidature = (candidatId) => {
  console.log(`Voir les détails de la candidature ID : ${candidatId}`);
  // Exemple: router.push({ name: 'CandidatDetails', params: { id: candidatId } });
};

const editCandidature = (candidatId) => {
  console.log(`Éditer la candidature ID : ${candidatId}`);
  // Exemple: router.push({ name: 'CandidatEdit', params: { id: candidatId } });
};

const confirmDeleteCandidature = (candidatId) => {
  if (confirm(`Êtes-vous sûr de vouloir supprimer la candidature ID ${candidatId} ?`)) {
    deleteCandidature(candidatId);
  }
};

const deleteCandidature = async (candidatId) => {
  console.log(`Suppression de la candidature ID : ${candidatId}`);
  // Exemple :
  // try {
  //   const response = await fetch(`/api/candidatures/${candidatId}/`, { method: 'DELETE' });
  //   if (!response.ok) throw new Error('Échec de la suppression.');
  //   candidats.value = candidats.value.filter(app => app.id !== candidatId); // Met à jour la liste localement
  //   alert('Candidature supprimée avec succès !');
  // } catch (e) {
  //   alert(`Erreur lors de la suppression: ${e.message}`);
  // }
};

// --- Fonctions d'aide pour le style (badges de statut) ---
const statusBadgeClass = (status) => {
  switch (status) {
    case 'Nouveau':
      return 'bg-blue-100 text-blue-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
    case 'En cours':
      return 'bg-yellow-100 text-yellow-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
    case 'Entretien':
      return 'bg-purple-100 text-purple-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
    case 'Accepté':
      return 'bg-green-100 text-green-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
    case 'Refusé':
      return 'bg-red-100 text-red-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
    case 'En attente':
      return 'bg-gray-100 text-gray-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
    default:
      return 'bg-gray-100 text-gray-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
  }
};

// Formateur de date
const formatDate = (dateStr) => {
  if (!dateStr) return '-';
  const options = { year: 'numeric', month: 'short', day: 'numeric' };
  return new Date(dateStr).toLocaleDateString('fr-FR', options);
};
</script>

<style scoped>
/* Aucun style spécifique n'est nécessaire ici car Tailwind CSS gère la plupart du design. */
/* Si vous aviez des styles très spécifiques qui ne sont pas gérés par Tailwind, vous les mettriez ici. */
</style>
