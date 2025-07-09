<template>
  <div
    class="flex flex-col p-6 bg-white rounded-lg shadow-xl drop-shadow min-h-[500px]"
    :class="{'min-w-[800px]': !isMobile}"
  >
    <div
      class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6 gap-4 sm:gap-0"
    >
      <div>
        <h2 class="text-2xl font-bold text-gray-800 mb-1">Employées</h2>
      </div>

      <div class="flex items-center space-x-4">
        <button
          v-if="selectedUserIds.length > 0"
          @click="confirmDeleteSelectedUsers"
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
          Supprimer ({{ selectedUserIds.length }})
        </button>

        <RouterLink
          to="/user/new"
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
          Nouvel Utilisateur
        </RouterLink>
      </div>
    </div>

    <div class="mb-4 flex flex-col sm:flex-row gap-4">
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Rechercher par nom, email, titre..."
        class="flex-1 px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-sm"
      />
      <select
        v-model="filterRole"
        class="px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-sm"
      >
        <option value="">Tous les rôles</option>
        <option v-for="role in availableRoles" :key="role" :value="role">
          {{ role }}
        </option>
      </select>
    </div>

    <div
      class="overflow-x-auto overflow-y-auto bg-white flex flex-col grow border border-gray-200 rounded-lg"
    >
      <table
        class="min-w-full table-auto text-sm text-left text-gray-700 divide-y divide-gray-200"
      >
        <thead
          class="bg-gray-50 text-xs uppercase text-gray-500 sticky top-0 z-10"
        >
          <tr>
            <th class="px-6 py-3 font-medium tracking-wider">
              <input
                type="checkbox"
                :checked="areAllUsersSelected"
                @change="toggleSelectAll"
                class="form-checkbox h-4 w-4 text-indigo-600 transition duration-150 ease-in-out rounded border-gray-300 focus:ring-indigo-500"
              />
            </th>
            <th class="px-6 py-3 font-medium tracking-wider">#</th>
            <th class="px-6 py-3 font-medium tracking-wider">Nom</th>
            <th class="px-6 py-3 font-medium tracking-wider">Titre</th>
            <th class="px-6 py-3 font-medium tracking-wider">Email</th>
            <th class="px-6 py-3 font-medium tracking-wider">Rôle</th>
            <th class="px-6 py-3 font-medium tracking-wider">Téléphone</th>
            <th class="px-6 py-3 font-medium tracking-wider">Département</th>

            <!-- <th class="px-6 py-3 font-medium tracking-wider text-right">
              Actions
            </th> -->
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200">
          <tr v-if="loading" class="text-center text-gray-500 py-4">
            <td colspan="9" class="px-6 py-4">Chargement des employées...</td>
          </tr>
          <tr
            v-else-if="filteredUsers.length === 0 && !loading"
            class="text-center text-gray-500 py-4"
          >
            <td colspan="9" class="px-6 py-4">Aucun employée trouvé.</td>
          </tr>
          <tr
            v-for="user in paginatedUsers"
            :key="user.id"
            class="hover:bg-gray-50 transition-colors duration-150 ease-in-out"
          >
            <td class="px-6 py-4">
              <input
                type="checkbox"
                :checked="selectedUserIds.includes(user.id)"
                @change="toggleUserSelection(user.id)"
                class="form-checkbox h-4 w-4 text-indigo-600 transition duration-150 ease-in-out rounded border-gray-300 focus:ring-indigo-500"
              />
            </td>
            <td class="px-6 py-4">{{ user.id }}</td>
            <td
              class="px-6 py-4 font-medium text-gray-900 flex items-center whitespace-nowrap"
            >
              <img
                :src="user.avatar"
                alt="Avatar"
                class="h-8 w-8 rounded-full mr-3 object-cover"
                v-if="user.avatar"
              />
              {{ user.name }}
            </td>
            <td class="px-6 py-4 text-indigo-600  whitespace-nowrap">
              {{ user.title }}
            </td>
            <td class="px-6 py-4 text-gray-800">{{ user.email }}</td>
            <td class="px-6 py-4">
              <span :class="roleBadgeClass(user.role)">
                {{ user.role }}
              </span>
            </td>
            <td class="px-6 py-4 text-gray-800  whitespace-nowrap">
              {{ user.phone }}
            </td>
            <td class="px-6 py-4 text-gray-800">{{ user.department }}</td>
            <!-- <td class="px-6 py-4 text-right">
              <button
                @click="confirmDeleteUser(user.id)"
                class="ml-4 text-red-600 hover:text-red-800 font-medium cursor-pointer hover:underline text-sm"
              >
                Supprimer
              </button>
            </td> -->
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
        <span class="font-medium">{{ filteredUsers.length }}</span>
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
const perPage = 10; // Nombre d'utilisateurs par page
const currentPage = ref(1); // Page actuelle de la pagination
const searchQuery = ref(''); // Terme de recherche
const filterRole = ref(''); // Filtre par rôle
const loading = ref(true); // État de chargement des données
const error = ref(null); // Message d'erreur
const isMobile = ref(false); // Pour adapter le min-width sur mobile

// Données des utilisateurs (simulées - à remplacer par un appel API)
const users = ref([]); // Initialement vide, sera rempli par fetchData

// Nouveau : État pour les utilisateurs sélectionnés
const selectedUserIds = ref([]);

// --- Détection Mobile (pour ajuster le style si besoin) ---
onMounted(() => {
  checkIfMobile();
  window.addEventListener('resize', checkIfMobile);
  fetchUsers(); // Récupère les utilisateurs au montage du composant
});

const checkIfMobile = () => {
  isMobile.value = window.innerWidth < 768; // Exemple pour les écrans < md
};

// --- Logique de Récupération des Utilisateurs ---
const fetchUsers = async () => {
  loading.value = true;
  error.value = null;
  try {
    // --- SIMULATION D'APPEL API ---
    // En production, vous feriez un appel à votre API Django ici
    // Exemple avec fetch :
    // const response = await fetch('/api/users/');
    // if (!response.ok) throw new Error('Échec de la récupération des utilisateurs.');
    // const data = await response.json();
    // users.value = data;

    // Données fictives pour la démo
    await new Promise(resolve => setTimeout(resolve, 800)); // Simule un délai réseau
    users.value = [
      { id: '1', name: "Lindsay Walton", title: "Développeur Front-end", email: "lindsay.walton@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '2', name: "Courtney Henry", title: "Designer", email: "courtney.henry@example.com", role: "Admin", avatar: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '3', name: "Tom Cook", title: "Directeur", email: "tom.cook@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '4', name: "Whitney Francis", title: "Copywriter", email: "whitney.francis@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '5', name: "Leonard Krasner", title: "Designer Senior", email: "leonard.krasner@example.com", role: "Propriétaire", avatar: 'https://images.unsplash.com/photo-1520785643438-5be78edd20d4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '6', name: "Floyd Miles", title: "Designer Principal", email: "floyd.miles@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1519244706279-b2ee4f6d6230?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '7', name: "Emily Selman", title: "VP, Expérience Utilisateur", email: "emily.selman@example.com", role: "Admin", avatar: 'https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '8', name: "Kristin Watson", title: "Développeur Front-end", email: "kristin.watson@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1509783236416-c9ad59ae4727?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '9', name: "Jenny Wilson", title: "Designer Produit", email: "jenny.wilson@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '10', name: "Cody Fisher", title: "Chef de Produit", email: "cody.fisher@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1502823403499-6ccfcfbd4f0e?ixlib=rb-1.2.1&ixid=eyJhcApp_idIjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '11', name: "Jane Cooper", title: "Coordinatrice Marketing", email: "jane.cooper@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29329?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '12', name: "Wade Warren", title: "Ingénieur Logiciel", email: "wade.warren@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1463453091185-6156198c8900?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '13', name: "Lindsay Walton 2", title: "Développeur Front-end", email: "lindsay.walton2@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '14', name: "Courtney Henry 2", title: "Designer", email: "courtney.henry2@example.com", role: "Admin", avatar: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '15', name: "Tom Cook 2", title: "Directeur", email: "tom.cook2@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '16', name: "Whitney Francis 2", title: "Copywriter", email: "whitney.francis2@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '17', name: "Leonard Krasner 2", title: "Designer Senior", email: "leonard.krasner2@example.com", role: "Propriétaire", avatar: 'https://images.unsplash.com/photo-1520785643438-5be78edd20d4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '18', name: "Floyd Miles 2", title: "Designer Principal", email: "floyd.miles2@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1519244706279-b2ee4f6d6230?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '19', name: "Emily Selman 2", title: "VP, Expérience Utilisateur", email: "emily.selman2@example.com", role: "Admin", avatar: 'https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '20', name: "Kristin Watson 2", title: "Développeur Front-end", email: "kristin.watson2@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1509783236416-c9ad59ae4727?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '21', name: "Jenny Wilson 2", title: "Designer Produit", email: "jenny.wilson2@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '22', name: "Cody Fisher 2", title: "Chef de Produit", email: "cody.fisher2@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1502823403499-6ccfcfbd4f0e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '23', name: "Jane Cooper 2", title: "Coordinatrice Marketing", email: "jane.cooper2@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29329?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '24', name: "Wade Warren 2", title: "Ingénieur Logiciel", email: "wade.warren2@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1463453091185-6156198c8900?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '25', name: "Lindsay Walton 3", title: "Développeur Front-end", email: "lindsay.walton3@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '26', name: "Courtney Henry 3", title: "Designer", email: "courtney.henry3@example.com", role: "Admin", avatar: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '27', name: "Tom Cook 3", title: "Directeur", email: "tom.cook3@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '28', name: "Whitney Francis 3", title: "Copywriter", email: "whitney.francis3@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '29', name: "Leonard Krasner 3", title: "Designer Senior", email: "leonard.krasner3@example.com", role: "Propriétaire", avatar: 'https://images.unsplash.com/photo-1520785643438-5be78edd20d4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '30', name: "Floyd Miles 3", title: "Designer Principal", email: "floyd.miles3@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1519244706279-b2ee4f6d6230?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '31', name: "Emily Selman 3", title: "VP, Expérience Utilisateur", email: "emily.selman3@example.com", role: "Admin", avatar: 'https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '32', name: "Kristin Watson 3", title: "Développeur Front-end", email: "kristin.watson3@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1509783236416-c9ad59ae4727?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '33', name: "Jenny Wilson 3", title: "Designer Produit", email: "jenny.wilson3@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '34', name: "Cody Fisher 3", title: "Chef de Produit", email: "cody.fisher3@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1502823403499-6ccfcfbd4f0e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '35', name: "Jane Cooper 3", title: "Coordinatrice Marketing", email: "jane.cooper3@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29329?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '36', name: "Wade Warren 3", title: "Ingénieur Logiciel", email: "wade.warren3@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1463453091185-6156198c8900?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '37', name: "Lindsay Walton 4", title: "Développeur Front-end", email: "lindsay.walton4@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '38', name: "Courtney Henry 4", title: "Designer", email: "courtney.henry4@example.com", role: "Admin", avatar: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '39', name: "Tom Cook 4", title: "Directeur", email: "tom.cook4@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '40', name: "Whitney Francis 4", title: "Copywriter", email: "whitney.francis4@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '41', name: "Leonard Krasner 4", title: "Designer Senior", email: "leonard.krasner4@example.com", role: "Propriétaire", avatar: 'https://images.unsplash.com/photo-1520785643438-5be78edd20d4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
      { id: '42', name: "Floyd Miles 4", title: "Designer Principal", email: "floyd.miles4@example.com", role: "Membre", avatar: 'https://images.unsplash.com/photo-1519244706279-b2ee4f6d6230?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80', phone: "+33 6 12 34 56 78", department: "Technique", },
    ];
  } catch (e) {
    error.value = `Impossible de charger les utilisateurs: ${e.message}`;
    console.error(e);
  } finally {
    loading.value = false;
  }
};

// --- Logique de Filtrage et Recherche ---
const filteredUsers = computed(() => {
  let filtered = users.value;

  // Appliquer le filtre de recherche
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase();
    filtered = filtered.filter(user =>
      user.name.toLowerCase().includes(query) ||
      user.email.toLowerCase().includes(query) ||
      user.title.toLowerCase().includes(query)
    );
  }

  // Appliquer le filtre de rôle
  if (filterRole.value) {
    filtered = filtered.filter(user => user.role === filterRole.value);
  }

  return filtered;
});

// Récupérer tous les rôles uniques pour le filtre
const availableRoles = computed(() => {
  const roles = new Set(users.value.map(user => user.role));
  return Array.from(roles).sort();
});

// --- Logique de Pagination ---
const totalPages = computed(() => Math.ceil(filteredUsers.value.length / perPage));

const paginatedUsers = computed(() => {
  const start = (currentPage.value - 1) * perPage;
  return filteredUsers.value.slice(start, start + perPage);
});

const startIndex = computed(() => (currentPage.value - 1) * perPage);
const endIndex = computed(() =>
  Math.min(currentPage.value * perPage, filteredUsers.value.length)
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
watch([filteredUsers, perPage], () => {
  if (currentPage.value > totalPages.value) {
    currentPage.value = 1;
  }
  // Important : réinitialiser les sélections quand la liste filtrée change
  selectedUserIds.value = [];
}, { immediate: true });


// --- Logique de Sélection ---

// Vérifie si tous les utilisateurs de la page actuelle sont sélectionnés
const areAllUsersSelected = computed(() => {
  return paginatedUsers.value.length > 0 && paginatedUsers.value.every(user => selectedUserIds.value.includes(user.id));
});

// Bascule la sélection d'un utilisateur individuel
const toggleUserSelection = (userId) => {
  const index = selectedUserIds.value.indexOf(userId);
  if (index > -1) {
    selectedUserIds.value.splice(index, 1); // Désélectionner
  } else {
    selectedUserIds.value.push(userId); // Sélectionner
  }
};

// Bascule la sélection de tous les utilisateurs de la page actuelle
const toggleSelectAll = () => {
  if (areAllUsersSelected.value) {
    // Si tout est sélectionné, désélectionner tout
    selectedUserIds.value = selectedUserIds.value.filter(id => !paginatedUsers.value.map(u => u.id).includes(id));
  } else {
    // Sinon, sélectionner tous les utilisateurs de la page actuelle qui ne le sont pas déjà
    paginatedUsers.value.forEach(user => {
      if (!selectedUserIds.value.includes(user.id)) {
        selectedUserIds.value.push(user.id);
      }
    });
  }
};

// --- Logique des Actions Utilisateur ---
const editUser = (userId) => {
  // Implémentez la logique d'édition ici (ex: router.push(`/user/${userId}/edit`))
  console.log(`Éditer l'utilisateur avec l'ID : ${userId}`);
  // Exemple: router.push({ name: 'UserEdit', params: { id: userId } });
};

const confirmDeleteUser = (userId) => {
  if (confirm(`Êtes-vous sûr de vouloir supprimer l'utilisateur avec l'ID ${userId} ?`)) {
    deleteUsers([userId]); // Appelle la fonction de suppression générique avec un tableau
  }
};

const confirmDeleteSelectedUsers = () => {
  if (selectedUserIds.value.length > 0 && confirm(`Êtes-vous sûr de vouloir supprimer les ${selectedUserIds.value.length} utilisateurs sélectionnés ?`)) {
    deleteUsers(selectedUserIds.value);
  }
};

const deleteUsers = async (idsToDelete) => {
  // Implémentez la logique de suppression ici (appel API)
  console.log(`Suppression des utilisateurs avec les IDs : ${idsToDelete.join(', ')}`);
  try {
    // SIMULATION : Filtrez les utilisateurs en local
    await new Promise(resolve => setTimeout(resolve, 500)); // Simule un délai réseau pour la suppression
    users.value = users.value.filter(u => !idsToDelete.includes(u.id));
    selectedUserIds.value = []; // Réinitialiser les sélections après suppression
    alert('Utilisateurs supprimés avec succès !');

    // En production, vous feriez des appels API pour chaque suppression ou un appel groupé
    // Exemple pour une suppression multiple :
    // const response = await fetch('/api/users/bulk_delete/', {
    //   method: 'POST', // ou 'DELETE' avec un corps de requête si votre API le permet
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify({ ids: idsToDelete })
    // });
    // if (!response.ok) throw new Error('Échec de la suppression groupée.');
    // users.value = users.value.filter(u => !idsToDelete.includes(u.id));
    // selectedUserIds.value = [];
    // alert('Utilisateurs supprimés avec succès !');

  } catch (e) {
    alert(`Erreur lors de la suppression: ${e.message}`);
    console.error(e);
  }
};

// --- Fonctions d'aide pour le style (badges de rôle) ---
const roleBadgeClass = (role) => {
  switch (role) {
    case 'Admin':
      return 'bg-blue-100 text-blue-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
    case 'Membre':
      return 'bg-green-100 text-green-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
    case 'Propriétaire':
      return 'bg-purple-100 text-purple-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
    default:
      return 'bg-gray-100 text-gray-800 px-2.5 py-0.5 rounded-full text-xs font-medium';
  }
};
</script>

<style scoped>
/* Pas de styles spécifiques nécessaires ici, Tailwind CSS gère tout. */
/* Si vous avez besoin de styles complexes non gérables par Tailwind, mettez-les ici */
</style>
