<template>
  <div
    class="flex flex-col  justify-center p-6 bg-white rounded-lg shadow h-[500px] w-[1200px]"
  >
    <div class="flex justify-between items-center mb-4">
      <div>
        <h2 class="text-xl font-semibold text-gray-800">Candidatures</h2>
        <p class="text-sm text-gray-500">
          Liste des candidatures avec les informations complètes du candidat et
          leur statut.
        </p>
      </div>
      <RouterLink
        to="/recruitment/candidates/new"
        class="bg-indigo-600 hover:bg-indigo-700 text-white px-8 py-2 rounded-lg text-sm"
      >
        Nouveau
      </RouterLink>
    </div>

    <div class=" overflow-x-auto h-full overflow-y-auto">
      <table class="min-w-full text-sm text-left text-gray-700">
        <thead class="text-xs uppercase text-gray-500 border-b">
          <tr>
            <th class=" px-8 py-3 ">Nom</th>
            <th class="px-8 py-3">Postulé<span class="m-2"></span>le</th>
            <th class="px-8 py-3">Poste</th>
            <th class="px-8 py-3">Statut</th>
            <th class="px-8 py-3">Raison<span class="m-2"></span>refus</th>
            <th class="px-8 py-3">Évaluation</th>
            <th class="px-8 py-3">Email</th>
            <th class="px-8 py-3">Étiquettes</th>
            <th class="px-8 py-3">Recruteur</th>
            <th class="px-8 py-3">Téléphone</th>
            <th class="px-8 py-3">Médium</th>
            <th class="px-8 py-3">Source</th>
            <th class="px-8 py-3"></th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="app in paginatedCandidat"
            :key="app.id"
            class="border-b hover:bg-gray-50"
          >
            <td class="w-full py-1 font-medium text-gray-900">
              {{ app.name }}
            </td>
            <td class="px-8 py-3">{{ formatDate(app.applied_at) }}</td>
            <td class="px-8 py-1">{{ app.position }}</td>
            <td class="px-8 py-1">{{ app.status }}</td>
            <td class="px-8 py-1 text-red-500">{{ app.rejection_reason }}</td>
            <td class="px-8 py-1">{{ app.evaluation }}</td>
            <td class="px-8 py-1">{{ app.email }}</td>
            <td class="px-8 py-1">{{ app.tags.join(', ') }}</td>
            <td class="px-8 py-1">{{ app.recruiter }}</td>
            <td class="px-8 py-1">{{ app.phone }}</td>
            <td class="px-8 py-1">{{ app.medium }}</td>
            <td class="px-8 py-1">{{ app.source }}</td>
            <td
              class="px-8 py-3 text-indigo-600 font-medium cursor-pointer hover:underline"
            >
              Voir
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- Pagination Controls -->
    <div class="mt-6 flex justify-between items-center shrink-0">
      <p class="text-sm text-gray-700">
        Showing
        <span class="font-medium">{{ startIndex + 1 }}</span>
        to
        <span class="font-medium">{{ endIndex }}</span>
        of
        <span class="font-medium">{{ candidats.length }}</span>
        results
      </p>
      <div class="flex gap-1">
        <button
          @click="goToPage(currentPage - 1)"
          :disabled="currentPage === 1"
          class="px-3 py-1 text-sm rounded border border-gray-300 text-gray-700 hover:bg-gray-50 disabled:opacity-50"
        >
          Previous
        </button>
        <button
          v-for="page in visiblePages"
          :key="page"
          @click="goToPage(page)"
          :class="[
              'px-3 py-1 text-sm rounded border',
              page === currentPage
                ? 'bg-indigo-600 text-white border-indigo-600'
                : 'border-gray-300 text-gray-700 hover:bg-gray-50'
            ]"
        >
          {{ page }}
        </button>
        <button
          @click="goToPage(currentPage + 1)"
          :disabled="currentPage === totalPages"
          class="px-3 py-1 text-sm rounded border border-gray-300 text-gray-700 hover:bg-gray-50 disabled:opacity-50"
        >
          Next
        </button>
      </div>
    </div>
    <!-- End Pagination Controls -->
  </div>
</template>

<script setup>
import {ref, computed, watch} from 'vue';

const perPage = 10;
const currentPage = ref(1);

const candidats =ref( [
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
    source: "Annonce en ligne"
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
    source: "Cooptation"
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
    source: "Stage précédent"
  },
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
    source: "Annonce en ligne"
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
    source: "Cooptation"
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
    source: "Stage précédent"
  },
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
    source: "Annonce en ligne"
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
    source: "Cooptation"
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
    source: "Stage précédent"
  },
]);

const totalPages = computed(() => Math.ceil(candidats.value.length / perPage));



const paginatedCandidat = computed(() => {
  const start = (currentPage.value - 1) * perPage;
  return candidats.value.slice(start, start + perPage);
});

const startIndex = computed(() => (currentPage.value - 1) * perPage);
const endIndex = computed(() =>
  Math.min(currentPage.value * perPage, candidats.value.length)
);

const visiblePages = computed(() => {
  const pages = [];
  let start = Math.max(1, currentPage.value - 2);
  let end = Math.min(totalPages.value, start + 4);
  if (end - start < 4) start = Math.max(1, end - 4);
  for (let i = start; i <= end; i++) pages.push(i);
  return pages;
});

function goToPage(page) {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
}

watch(candidats, () => {
  if (currentPage.value > totalPages.value) {
    currentPage.value = 1;
  }
});


// Formateur de date
const formatDate = (dateStr) => {
  const options = { year: 'numeric', month: 'short', day: 'numeric' }
  return new Date(dateStr).toLocaleDateString('fr-FR', options)
}
</script>
