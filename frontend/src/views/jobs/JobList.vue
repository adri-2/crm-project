<template>
  <div
    class="flex flex-col p-6 bg-white rounded-lg shadow-xl drop-shadow min-h-[500px]"
    :class="{ 'w-full': !isMobile, 'min-w-[800px]': !isMobile }"
  >
    <div
      class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6 gap-4 sm:gap-0"
    >
      <div>
        <h2 class="text-2xl font-bold text-gray-800 mb-1">Postes</h2>
        <!-- <p class="text-sm text-gray-600 max-w-lg">
          Liste complète des postes avec leurs titres, ntreprises,
          localisations et types de contrat.
        </p> -->
      </div>

      <RouterLink
        to="/job/new"
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
        Nouveau Poste
      </RouterLink>
    </div>

    <div class="mb-4 flex flex-col sm:flex-row gap-4">
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Rechercher par titre, entreprise, lieu..."
        class="flex-1 px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-sm"
      />
      <select
        v-model="filterType"
        class="px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-sm"
      >
        <option value="">Tous les types</option>
        <option v-for="type in availableTypes" :key="type" :value="type">
          {{ type }}
        </option>
      </select>
      <select
        v-model="filterLocation"
        class="px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-sm"
      >
        <option value="">Toutes les localisations</option>
        <option
          v-for="location in availableLocations"
          :key="location"
          :value="location"
        >
          {{ location }}
        </option>
      </select>
    </div>

    <!-- <div v-if="loading" class="h-full w-full flex items-center justify-center">
      <p class="text-gray-500">Chargement des offres d'emploi...</p>
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
      v-else-if="filteredJobs.length === 0"
      class="h-full w-full flex items-center justify-center"
    >
      <p class="text-gray-500">
        Aucune offre d'emploi trouvée pour les critères sélectionnés.
      </p>
    </div> -->
    <div
      class="overflow-x-auto overflow-y-auto bg-white flex flex-col grow border border-gray-200 rounded-lg"
    >
      <table
        class="min-w-full text-sm text-left text-gray-700 divide-y divide-gray-200"
      >
        <thead
          class="bg-gray-50 text-xs uppercase text-gray-500 sticky top-0 z-10"
        >
          <tr>
            <th class="px-6 py-3 font-medium tracking-wider">Titre</th>
            <th class="px-6 py-3 font-medium tracking-wider">Entreprise</th>
            <th class="px-6 py-3 font-medium tracking-wider">Localisation</th>
            <th class="px-6 py-3 font-medium tracking-wider">Type</th>
            <th class="px-6 py-3 font-medium tracking-wider">
              Date de Publication
            </th>
            <th class="px-6 py-3 font-medium tracking-wider">Statut</th>
            <th class="px-6 py-3 font-medium tracking-wider text-right">
              Actions
            </th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200">
          <tr v-if="loading" class="text-center text-gray-500 py-4">
            <td colspan="6" class="px-6 py-4">Chargement des postes...</td>
          </tr>
          <tr
            v-else-if="filteredJobs.length === 0  && !loading"
            class="text-center text-gray-500 py-4"
          >
            <td colspan="6" class="px-6 py-4">
              Aucune poste trouvée pour les critères sélectionnés.
            </td>
          </tr>
          <tr
            v-else
            v-for="job in paginatedJobs"
            :key="job.id"
            class="hover:bg-gray-50 transition-colors duration-150 ease-in-out"
          >
            <td class="px-6 py-4 font-medium text-gray-900">{{ job.title }}</td>
            <td class="px-6 py-4 text-indigo-700 font-semibold">
              {{ job.company }}
            </td>
            <td class="px-6 py-4">{{ job.location }}</td>
            <td class="px-6 py-4">
              <span :class="typeBadgeClass(job.type)">
                {{ job.type }}
              </span>
            </td>
            <td class="px-6 py-4">{{ formatDate(job.published_at) }}</td>
            <td class="px-6 py-4">
              <span :class="statusBadgeClass(job.status)">
                {{ job.status }}
              </span>
            </td>
            <td class="px-6 py-4 text-right">
              <!-- <button
                @click="viewJob(job.id)"
                class="text-indigo-600 hover:text-indigo-800 font-medium cursor-pointer hover:underline text-sm"
              >
                Voir
              </button>
              <button
                @click="editJob(job.id)"
                class="ml-4 text-gray-600 hover:text-gray-800 font-medium cursor-pointer hover:underline text-sm"
              >
                Éditer
              </button> -->
              <button
                @click="confirmDeleteJob(job.id)"
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
        <span class="font-medium">{{ filteredJobs.length }}</span>
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
const perPage = 10; // Nombre d'offres par page
const currentPage = ref(1); // Page actuelle de la pagination
const searchQuery = ref(''); // Terme de recherche
const filterType = ref(''); // Filtre par type de contrat
const filterLocation = ref(''); // Filtre par localisation
const loading = ref(true); // État de chargement des données
const error = ref(null); // Message d'erreur
const isMobile = ref(false); // Pour adapter le min-width sur mobile

// Données des offres d'emploi (simulées - à remplacer par un appel API)
const jobs = ref([]); // Initialement vide, sera rempli par fetchData

// --- Détection Mobile (pour ajuster le style si besoin) ---
onMounted(() => {
  checkIfMobile();
  window.addEventListener('resize', checkIfMobile);
  fetchJobs(); // Récupère les offres au montage du composant
});

const checkIfMobile = () => {
  isMobile.value = window.innerWidth < 768; // Exemple pour les écrans < md
};

// --- Logique de Récupération des Offres d'Emploi ---
const fetchJobs = async () => {
  loading.value = true;
  error.value = null;
  try {
    // --- SIMULATION D'APPEL API ---
    // En production, vous feriez un appel à votre API Django ici
    // Exemple avec fetch :
    // const response = await fetch('/api/jobs/');
    // if (!response.ok) throw new Error('Échec de la récupération des offres d\'emploi.');
    // const data = await response.json();
    // jobs.value = data;

    // Données fictives pour la démo
    await new Promise(resolve => setTimeout(resolve, 800)); // Simule un délai réseau
    jobs.value = [
      {
        id: 1,
        title: "Frontend Developer",
        company: "TechCorp",
        location: "Remote",
        type: "Full-time",
        published_at: "2024-06-20",
        status: "Active",
      },
      {
        id: 2,
        title: "UI/UX Designer",
        company: "Creative Inc.",
        location: "Paris, France",
        type: "Part-time",
        published_at: "2024-06-15",
        status: "Active",
      },
      {
        id: 3,
        title: "Backend Engineer",
        company: "DevSolutions",
        location: "Berlin, Germany",
        type: "Full-time",
        published_at: "2024-06-10",
        status: "Active",
      },
      {
        id: 4,
        title: "Marketing Specialist",
        company: "MarketSmart",
        location: "Remote",
        type: "Freelance",
        published_at: "2024-06-01",
        status: "Active",
      },
      {
        id: 5,
        title: "Data Analyst",
        company: "Insights Co.",
        location: "Dakar, Senegal",
        type: "Full-time",
        published_at: "2024-05-25",
        status: "Active",
      },
      {
        id: 6,
        title: "Cloud Architect",
        company: "CloudWare",
        location: "London, UK",
        type: "Full-time",
        published_at: "2024-06-22",
        status: "Active",
      },
      {
        id: 7,
        title: "Product Manager",
        company: "Innovate Solutions",
        location: "New York, USA",
        type: "Full-time",
        published_at: "2024-06-18",
        status: "Active",
      },
      {
        id: 8,
        title: "Sales Representative",
        company: "Global Sales",
        location: "Casablanca, Morocco",
        type: "Contract",
        published_at: "2024-06-12",
        status: "Active",
      },
      {
        id: 9,
        title: "HR Manager",
        company: "PeopleFirst",
        location: "Lyon, France",
        type: "Full-time",
        published_at: "2024-06-05",
        status: "Active",
      },
      {
        id: 10,
        title: "DevOps Engineer",
        company: "DevOps Pro",
        location: "Remote",
        type: "Full-time",
        published_at: "2024-05-30",
        status: "Active",
      },
      {
        id: 11,
        title: "Cybersecurity Analyst",
        company: "SecureNet",
        location: "Abidjan, Côte d'Ivoire",
        type: "Full-time",
        published_at: "2024-06-25",
        status: "Active",
      },
      {
        id: 12,
        title: "Copywriter",
        company: "WordGenius",
        location: "Remote",
        type: "Freelance",
        published_at: "2024-06-21",
        status: "Archived", // Example of inactive status
      },
      {
        id: 13,
        title: "Network Administrator",
        company: "ConnectIT",
        location: "Brussels, Belgium",
        type: "Full-time",
        published_at: "2024-06-19",
        status: "Active",
      },
      {
        id: 14,
        title: "Legal Advisor",
        company: "LawFirm Inc.",
        location: "Geneva, Switzerland",
        type: "Part-time",
        published_at: "2024-06-14",
        status: "Active",
      },
      {
        id: 15,
        title: "Mobile App Developer",
        company: "AppCreators",
        location: "Barcelona, Spain",
        type: "Full-time",
        published_at: "2024-06-07",
        status: "Active",
      },
      {
        id: 16,
        title: "Content Creator",
        company: "Digital Spark",
        location: "Remote",
        type: "Freelance",
        published_at: "2024-06-03",
        status: "Active",
      },
      {
        id: 17,
        title: "Business Analyst",
        company: "Strategy Corp.",
        location: "Dubai, UAE",
        type: "Full-time",
        published_at: "2024-05-28",
        status: "Active",
      },
      {
        id: 18,
        title: "Research Scientist",
        company: "BioLabs",
        location: "Cambridge, USA",
        type: "Full-time",
        published_at: "2024-05-20",
        status: "Active",
      },
      {
        id: 19,
        title: "Customer Support Specialist",
        company: "ServicePro",
        location: "Berlin, Germany",
        type: "Part-time",
        published_at: "2024-05-15",
        status: "Closed", // Another example of inactive status
      },
      {
        id: 20,
        title: "Financial Controller",
        company: "FinanceHub",
        location: "Paris, France",
        type: "Full-time",
        published_at: "2024-05-10",
        status: "Active",
      },
    ];
  } catch (e) {
    error.value = `Impossible de charger les offres d'emploi : ${e.message}`;
    console.error(e);
  } finally {
    loading.value = false;
  }
};

// --- Logique de Filtrage et Recherche ---
const filteredJobs = computed(() => {
  let filtered = jobs.value;

  // Appliquer le filtre de recherche
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase();
    filtered = filtered.filter(job =>
      job.title.toLowerCase().includes(query) ||
      job.company.toLowerCase().includes(query) ||
      job.location.toLowerCase().includes(query) ||
      job.type.toLowerCase().includes(query)
    );
  }

  // Appliquer le filtre par type
  if (filterType.value) {
    filtered = filtered.filter(job => job.type === filterType.value);
  }

  // Appliquer le filtre par localisation
  if (filterLocation.value) {
    filtered = filtered.filter(job => job.location === filterLocation.value);
  }

  return filtered;
});

// Récupérer tous les types uniques pour le filtre
const availableTypes = computed(() => {
  const types = new Set(jobs.value.map(job => job.type));
  return Array.from(types).sort();
});

// Récupérer toutes les localisations uniques pour le filtre
const availableLocations = computed(() => {
  const locations = new Set(jobs.value.map(job => job.location));
  return Array.from(locations).sort();
});

// --- Logique de Pagination ---
const totalPages = computed(() => Math.ceil(filteredJobs.value.length / perPage));

const paginatedJobs = computed(() => {
  const start = (currentPage.value - 1) * perPage;
  return filteredJobs.value.slice(start, start + perPage);
});

const startIndex = computed(() => (currentPage.value - 1) * perPage);
const endIndex = computed(() =>
  Math.min(currentPage.value * perPage, filteredJobs.value.length)
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
watch([filteredJobs, perPage], () => {
  if (currentPage.value > totalPages.value) {
    currentPage.value = 1;
  }
}, { immediate: true });

// --- Logique des Actions sur Offre d'Emploi ---
const viewJob = (jobId) => {
  console.log(`Voir les détails de l'offre d'emploi ID : ${jobId}`);
  // Exemple: router.push({ name: 'JobDetails', params: { id: jobId } });
};

const editJob = (jobId) => {
  console.log(`Éditer l'offre d'emploi ID : ${jobId}`);
  // Exemple: router.push({ name: 'JobEdit', params: { id: jobId } });
};

const confirmDeleteJob = (jobId) => {
  if (confirm(`Êtes-vous sûr de vouloir supprimer l'offre d'emploi ID ${jobId} ?`)) {
    deleteJob(jobId);
  }
};

const deleteJob = async (jobId) => {
  console.log(`Suppression de l'offre d'emploi ID : ${jobId}`);
  // Exemple :
  // try {
  //   const response = await fetch(`/api/jobs/${jobId}/`, { method: 'DELETE' });
  //   if (!response.ok) throw new Error('Échec de la suppression.');
  //   jobs.value = jobs.value.filter(job => job.id !== jobId); // Met à jour la liste localement
  //   alert('Offre d\'emploi supprimée avec succès !');
  // } catch (e) {
  //   alert(`Erreur lors de la suppression: ${e.message}`);
  // }
};

// --- Fonctions d'aide pour le style (badges de type et statut) ---
const typeBadgeClass = (type) => {
  switch (type) {
    case 'Full-time':
      return 'bg-green-100 text-green-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
    case 'Part-time':
      return 'bg-yellow-100 text-yellow-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
    case 'Freelance':
      return 'bg-purple-100 text-purple-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
    case 'Contract':
      return 'bg-blue-100 text-blue-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
    default:
      return 'bg-gray-100 text-gray-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
  }
};

const statusBadgeClass = (status) => {
  switch (status) {
    case 'Active':
      return 'bg-green-100 text-green-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
    case 'Archived':
      return 'bg-orange-100 text-orange-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
    case 'Closed':
      return 'bg-red-100 text-red-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
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
</style>
