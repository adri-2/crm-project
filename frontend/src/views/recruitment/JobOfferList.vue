<template>
  <div
    class="flex flex-col p-6 bg-white rounded-lg shadow-xl drop-shadow min-h-[500px]"
    :class="{ 'w-full': !isMobile, 'min-w-[800px]': !isMobile }"
  >
    <div
      class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6 gap-4 sm:gap-0"
    >
      <div>
        <h2 class="text-2xl font-bold text-gray-800 mb-1">Offres d'Emploi</h2>
      </div>

      <div class="flex items-center gap-4">
        <button
          v-if="selectedOffers.length > 0"
          @click="confirmDeleteSelectedOffers"
          class="inline-flex items-center px-5 py-2.5 bg-red-600 hover:bg-red-700 text-white font-medium rounded-md text-sm transition-colors duration-200 ease-in-out shadow-md hover:shadow-lg"
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
              d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
            />
          </svg>
          Supprimer la sélection ({{ selectedOffers.length }})
        </button>

        <RouterLink
          to="/recruitment/offers/new"
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
          Nouvelle Offre
        </RouterLink>
      </div>
    </div>

    <div class="mb-4 flex flex-col sm:flex-row gap-4">
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Rechercher par poste, département..."
        class="flex-1 px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-sm"
      />
      <select
        v-model="filterDepartment"
        class="px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-sm"
      >
        <option value="">Tous les départements</option>
        <option
          v-for="department in availableDepartments"
          :key="department"
          :value="department"
        >
          {{ department }}
        </option>
      </select>
      <select
        v-model="filterStatus"
        class="px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-sm"
      >
        <option value="">Tous les statuts</option>
        <option value="active">Actives</option>
        <option value="expired">Expirées</option>
      </select>
    </div>

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
            <th class="px-6 py-3 font-medium tracking-wider">
              <input
                type="checkbox"
                @change="toggleSelectAll"
                :checked="isAllSelected"
                :indeterminate="isIndeterminate"
                class="form-checkbox h-4 w-4 text-indigo-600 transition duration-150 ease-in-out"
              />
            </th>
            <th class="px-6 py-3 font-medium tracking-wider">Poste</th>
            <th class="px-6 py-3 font-medium tracking-wider">Département</th>
            <th class="px-6 py-3 font-medium tracking-wider">Créée le</th>
            <th class="px-6 py-3 font-medium tracking-wider">Date limite</th>
            <th class="px-6 py-3 font-medium tracking-wider text-center">
              Demandes
            </th>
            <th class="px-6 py-3 font-medium tracking-wider text-center">
              Candidatures
            </th>
            <th class="px-6 py-3 font-medium tracking-wider text-center">
              Statut
            </th>
            <th class="px-6 py-3 font-medium tracking-wider text-right">
              Actions
            </th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200">
          <tr v-if="loading" class="text-center text-gray-500 py-4">
            <td colspan="9" class="px-6 py-4">
              Chargement des offres d'emploi...
            </td>
          </tr>
          <tr
            v-else-if="filteredOffers.length === 0 && !loading"
            class="text-center text-gray-500 py-4"
          >
            <td colspan="9" class="px-6 py-4">
              Aucune offre de poste trouvée pour les critères sélectionnés.
            </td>
          </tr>
          <tr
            v-for="offer in paginatedOffers"
            :key="offer.id"
            class="hover:bg-gray-50 transition-colors duration-150 ease-in-out"
            :class="{ 'bg-blue-50': selectedOffers.includes(offer.id) }"
          >
            <td class="px-6 py-4">
              <input
                type="checkbox"
                :value="offer.id"
                v-model="selectedOffers"
                class="form-checkbox h-4 w-4 text-indigo-600 transition duration-150 ease-in-out"
              />
            </td>
            <td class="px-6 py-4 font-medium text-gray-900">
              {{ offer.title }}
            </td>
            <td class="px-6 py-4">{{ offer.department }}</td>
            <td class="px-6 py-4 whitespace-nowrap">
              {{ formatDate(offer.created_at) }}
            </td>
            <td class="px-6 py-4">
              <span :class="deadlineClass(offer.deadline)">
                {{ formatDate(offer.deadline) }}
              </span>
            </td>
            <td class="px-6 py-4 text-center">{{ offer.requests }}</td>
            <td class="px-6 py-4 text-center">{{ offer.applications }}</td>
            <td class="px-6 py-4 text-center">
              <span :class="statusBadgeClass(offer.deadline)">
                {{ getOfferStatus(offer.deadline) }}
              </span>
            </td>
            <td class="px-6 py-4 text-right">
              <button
                @click="confirmDeleteOffer(offer.id)"
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
      class="mt-6 mb-2 flex flex-col sm:flex-row justify-between items-center shrink-0"
    >
      <p class="text-sm text-gray-700 mb-2 sm:mb-0">
        Affichage de
        <span class="font-medium">{{ startIndex + 1 }}</span>
        à
        <span class="font-medium">{{ endIndex }}</span>
        sur
        <span class="font-medium">{{ filteredOffers.length }}</span>
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
                : 'border-gray-300 text-gray-700 hover:bg-gray-100',
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
import { RouterLink } from 'vue-router';

// --- Données et États ---
const perPage = 10;
const currentPage = ref(1);
const searchQuery = ref('');
const filterDepartment = ref('');
const filterStatus = ref('');
const loading = ref(true);
const error = ref(null);
const isMobile = ref(false);
const offers = ref([]);

// Nouvelle donnée pour la sélection multiple
const selectedOffers = ref([]);

// --- Détection Mobile (pour ajuster le style si besoin) ---
onMounted(() => {
  checkIfMobile();
  window.addEventListener('resize', checkIfMobile);
  fetchOffers();
});

const checkIfMobile = () => {
  isMobile.value = window.innerWidth < 768;
};

// --- Logique de Récupération des Offres de Poste ---
const fetchOffers = async () => {
  loading.value = true;
  error.value = null;
  try {
    await new Promise((resolve) => setTimeout(resolve, 800)); // Simule un délai réseau
    offers.value = [
      {
        id: 1,
        title: 'Développeur Frontend',
        department: 'Informatique',
        created_at: '2025-05-01',
        deadline: '2025-07-15', // Date future
        requests: 10,
        applications: 6,
      },
      {
        id: 2,
        title: 'Analyste RH',
        department: 'Ressources Humaines',
        created_at: '2025-04-20',
        deadline: '2025-06-01', // Date passée
        requests: 8,
        applications: 8,
      },
      {
        id: 3,
        title: 'Assistant Marketing',
        department: 'Marketing',
        created_at: '2025-05-10',
        deadline: '2025-07-30', // Date future
        requests: 15,
        applications: 11,
      },
      {
        id: 4,
        title: 'Chef de projet',
        department: 'Gestion de projet',
        created_at: '2025-04-05',
        deadline: '2025-06-10', // Date passée
        requests: 5,
        applications: 2,
      },
      {
        id: 5,
        title: 'Comptable',
        department: 'Finance',
        created_at: '2025-05-15',
        deadline: '2025-07-25', // Date future
        requests: 7,
        applications: 3,
      },
      {
        id: 6,
        title: 'Ingénieur DevOps',
        department: 'Informatique',
        created_at: '2025-06-01',
        deadline: '2025-08-01', // Date future
        requests: 12,
        applications: 5,
      },
      {
        id: 7,
        title: 'Graphiste Senior',
        department: 'Création',
        created_at: '2025-05-20',
        deadline: '2025-07-10', // Date future
        requests: 9,
        applications: 7,
      },
      {
        id: 8,
        title: 'Responsable Commercial',
        department: 'Commercial',
        created_at: '2025-04-10',
        deadline: '2025-05-30', // Date passée
        requests: 20,
        applications: 15,
      },
      {
        id: 9,
        title: 'Juriste d\'entreprise',
        department: 'Juridique',
        created_at: '2025-06-05',
        deadline: '2025-08-10', // Date future
        requests: 6,
        applications: 4,
      },
      {
        id: 10,
        title: 'Data Scientist',
        department: 'Informatique',
        created_at: '2025-05-25',
        deadline: '2025-07-20', // Date future
        requests: 18,
        applications: 9,
      },
      {
        id: 11,
        title: 'Responsable R&D',
        department: 'Recherche et Développement',
        created_at: '2025-06-10',
        deadline: '2025-08-25', // Date future
        requests: 7,
        applications: 3,
      },
      {
        id: 12,
        title: 'Chargé de clientèle',
        department: 'Service Client',
        created_at: '2025-05-01',
        deadline: '2025-06-01', // Date passée
        requests: 25,
        applications: 20,
      },
      {
        id: 13,
        title: 'Technicien de maintenance',
        department: 'Technique',
        created_at: '2025-06-15',
        deadline: '2025-08-05', // Date future
        requests: 11,
        applications: 6,
      },
      {
        id: 14,
        title: 'Auditeur interne',
        department: 'Audit',
        created_at: '2025-05-05',
        deadline: '2025-06-20', // Date future (moins d'une semaine)
        requests: 9,
        applications: 5,
      },
      {
        id: 15,
        title: 'Chef de produit IT',
        department: 'Produit',
        created_at: '2025-06-20',
        deadline: '2025-09-01', // Date future
        requests: 14,
        applications: 8,
      },
    ];
    // Réinitialiser la sélection après le chargement des données
    selectedOffers.value = [];
  } catch (e) {
    error.value = `Impossible de charger les offres de poste : ${e.message}`;
    console.error(e);
  } finally {
    loading.value = false;
  }
};

// --- Logique de Filtrage et Recherche ---
const filteredOffers = computed(() => {
  let filtered = offers.value;

  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase();
    filtered = filtered.filter((offer) =>
      offer.title.toLowerCase().includes(query) ||
      offer.department.toLowerCase().includes(query)
    );
  }

  if (filterDepartment.value) {
    filtered = filtered.filter(
      (offer) => offer.department === filterDepartment.value
    );
  }

  if (filterStatus.value) {
    const now = new Date();
    filtered = filtered.filter((offer) => {
      const deadlineDate = new Date(offer.deadline);
      if (filterStatus.value === 'active') {
        return deadlineDate >= now;
      } else if (filterStatus.value === 'expired') {
        return deadlineDate < now;
      }
      return true;
    });
  }

  return filtered;
});

const availableDepartments = computed(() => {
  const departments = new Set(offers.value.map((offer) => offer.department));
  return Array.from(departments).sort();
});

// --- Logique de Pagination ---
const totalPages = computed(() =>
  Math.ceil(filteredOffers.value.length / perPage)
);

const paginatedOffers = computed(() => {
  const start = (currentPage.value - 1) * perPage;
  const end = start + perPage;
  return filteredOffers.value.slice(start, end);
});

const startIndex = computed(() => (currentPage.value - 1) * perPage);
const endIndex = computed(() =>
  Math.min(currentPage.value * perPage, filteredOffers.value.length)
);

const visiblePages = computed(() => {
  const pages = [];
  const maxVisible = 5;
  let start = Math.max(1, currentPage.value - Math.floor(maxVisible / 2));
  let end = Math.min(totalPages.value, start + maxVisible - 1);

  if (end - start + 1 < maxVisible) {
    start = Math.max(1, end - maxVisible + 1);
  }

  for (let i = start; i <= end; i++) {
    pages.push(i);
  }
  return pages;
});

function goToPage(page) {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
}

watch(
  [filteredOffers, perPage],
  () => {
    if (currentPage.value > totalPages.value) {
      currentPage.value = 1;
    }
    selectedOffers.value = []; // Clear selection when filters or pagination changes
  },
  { immediate: true }
);

// --- Logique de Sélection Multiple ---

// Vérifie si toutes les offres de la page actuelle sont sélectionnées
const isAllSelected = computed(() => {
  if (paginatedOffers.value.length === 0) return false;
  return paginatedOffers.value.every((offer) =>
    selectedOffers.value.includes(offer.id)
  );
});

// Vérifie si la sélection est partielle (certains éléments sélectionnés, mais pas tous)
const isIndeterminate = computed(() => {
  return (
    selectedOffers.value.length > 0 &&
    !isAllSelected.value &&
    paginatedOffers.value.some((offer) =>
      selectedOffers.value.includes(offer.id)
    )
  );
});

// Bascule la sélection de toutes les offres de la page actuelle
const toggleSelectAll = () => {
  if (isAllSelected.value) {
    // Si tout est sélectionné, désélectionne tout sur la page actuelle
    paginatedOffers.value.forEach((offer) => {
      const index = selectedOffers.value.indexOf(offer.id);
      if (index > -1) {
        selectedOffers.value.splice(index, 1);
      }
    });
  } else {
    // Si rien ou seulement une partie est sélectionnée, sélectionne tout sur la page actuelle
    paginatedOffers.value.forEach((offer) => {
      if (!selectedOffers.value.includes(offer.id)) {
        selectedOffers.value.push(offer.id);
      }
    });
  }
};

// --- Logique des Actions sur Offre de Poste ---
const viewOffer = (offerId) => {
  console.log(`Voir les détails de l'offre de poste ID : ${offerId}`);
  // Exemple: router.push({ name: 'OfferDetails', params: { id: offerId } });
};

const editOffer = (offerId) => {
  console.log(`Modifier l'offre de poste ID : ${offerId}`);
  // Exemple: router.push({ name: 'OfferEdit', params: { id: offerId } });
};

const confirmDeleteOffer = (offerId) => {
  if (confirm(`Êtes-vous sûr de vouloir supprimer l'offre de poste ID ${offerId} ?`)) {
    deleteOffer(offerId);
  }
};

const deleteOffer = async (offerId) => {
  console.log(`Suppression de l'offre de poste ID : ${offerId}`);
  try {
    // Simuler la suppression API
    await new Promise((resolve) => setTimeout(resolve, 300));
    offers.value = offers.value.filter((offer) => offer.id !== offerId);
    selectedOffers.value = selectedOffers.value.filter((id) => id !== offerId); // Supprimer des sélections aussi
    alert('Offre de poste supprimée avec succès !');
  } catch (e) {
    alert(`Erreur lors de la suppression: ${e.message}`);
  }
};

const confirmDeleteSelectedOffers = () => {
  if (
    confirm(
      `Êtes-vous sûr de vouloir supprimer les ${selectedOffers.value.length} offres sélectionnées ?`
    )
  ) {
    deleteSelectedOffers();
  }
};

const deleteSelectedOffers = async () => {
  console.log(
    `Suppression des offres sélectionnées : ${selectedOffers.value.join(', ')}`
  );
  try {
    // Simuler la suppression API pour chaque élément sélectionné
    await new Promise((resolve) => setTimeout(resolve, 500)); // Simule un délai pour la suppression multiple
    offers.value = offers.value.filter(
      (offer) => !selectedOffers.value.includes(offer.id)
    );
    selectedOffers.value = []; // Vider la sélection après suppression
    alert('Offres sélectionnées supprimées avec succès !');
  } catch (e) {
    alert(`Erreur lors de la suppression multiple: ${e.message}`);
  }
};

// --- Fonctions d'aide pour le style et le statut ---
const getOfferStatus = (deadline) => {
  const now = new Date();
  const deadlineDate = new Date(deadline);
  if (deadlineDate < now) {
    return 'Expirée';
  }
  const diffTime = Math.abs(deadlineDate - now);
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  if (diffDays <= 7) {
    return `Active (J-${diffDays})`;
  }
  return 'Active';
};

const statusBadgeClass = (deadline) => {
  const status = getOfferStatus(deadline);
  if (status.includes('Expirée')) {
    return 'bg-red-100 text-red-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
  } else if (status.includes('(J-')) {
    return 'bg-orange-100 text-orange-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
  } else {
    return 'bg-green-100 text-green-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
  }
};

const deadlineClass = (deadline) => {
  const now = new Date();
  const deadlineDate = new Date(deadline);
  if (deadlineDate < now) {
    return 'text-red-600 font-semibold';
  }
  const diffTime = Math.abs(deadlineDate - now);
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  if (diffDays <= 7) {
    return 'text-orange-600 font-semibold';
  }
  return 'text-gray-800';
};

const formatDate = (dateStr) => {
  if (!dateStr) return '-';
  const options = { year: 'numeric', month: 'short', day: 'numeric' };
  return new Date(dateStr).toLocaleDateString('fr-FR', options);
};
</script>

<style scoped>
/* Aucun style spécifique n'est nécessaire ici car Tailwind CSS gère la plupart du design. */
/* Vous pouvez ajouter des styles personnalisés si nécessaire, par exemple pour la case à cocher 'indeterminate' */
.form-checkbox:indeterminate {
  background-color: #6366f1; /* Indigo-600 */
  border-color: #6366f1; /* Indigo-600 */
  box-shadow: none; /* Enlève l'ombre par défaut si gênante */
}
</style>
