<template>
  <div class="p-6 bg-white rounded-lg shadow">
    <div class="flex justify-between items-center mb-4">
      <div>
        <h2 class="text-xl font-semibold text-gray-800">Offres de poste</h2>
        <p class="text-sm text-gray-500">
          Liste des offres avec le poste, le département, les dates clés et les
          candidatures.
        </p>
      </div>

      <RouterLink
        to="/recruitment/offers/new"
        class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg text-sm"
      >
        Nouveau
      </RouterLink>
    </div>

    <div class="overflow-x-auto">
      <table class="min-w-full text-sm text-left text-gray-700">
        <thead class="text-xs uppercase text-gray-500 border-b">
          <tr>
            <th class="px-4 py-3">Poste</th>
            <th class="px-4 py-3">Département</th>
            <th class="px-4 py-3">Créée le</th>
            <th class="px-4 py-3">Date limite</th>
            <th class="px-4 py-3">Demandes</th>
            <th class="px-4 py-3">Reçues</th>
            <th class="px-4 py-3"></th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="job in jobs"
            :key="job.id"
            class="border-b hover:bg-gray-50"
          >
            <td class="px-4 py-3 font-medium text-gray-900">{{ job.title }}</td>
            <td class="px-4 py-3">{{ job.department }}</td>
            <td class="px-4 py-3">{{ formatDate(job.created_at) }}</td>
            <td class="px-4 py-3">{{ formatDate(job.deadline) }}</td>
            <td class="px-4 py-3 text-center">{{ job.requests }}</td>
            <td class="px-4 py-3 text-center">{{ job.applications }}</td>
            <td
              class="px-4 py-3 text-indigo-600 font-medium cursor-pointer hover:underline"
            >
              Modifier
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';

const jobs = [
  {
    id: 1,
    title: "Développeur Frontend",
    department: "Informatique",
    created_at: "2025-05-01",
    deadline: "2025-06-15",
    requests: 10,
    applications: 6,
  },
  {
    id: 2,
    title: "Analyste RH",
    department: "Ressources Humaines",
    created_at: "2025-04-20",
    deadline: "2025-06-01",
    requests: 8,
    applications: 8,
  },
  {
    id: 3,
    title: "Assistant Marketing",
    department: "Marketing",
    created_at: "2025-05-10",
    deadline: "2025-06-30",
    requests: 15,
    applications: 11,
  },
  {
    id: 4,
    title: "Chef de projet",
    department: "Gestion de projet",
    created_at: "2025-04-05",
    deadline: "2025-06-10",
    requests: 5,
    applications: 2,
  },
  {
    id: 5,
    title: "Comptable",
    department: "Finance",
    created_at: "2025-05-15",
    deadline: "2025-06-25",
    requests: 7,
    applications: 3,
  },
];

// Formateur de date
const formatDate = (dateStr) => {
  const options = { year: 'numeric', month: 'short', day: 'numeric' }
  return new Date(dateStr).toLocaleDateString('fr-FR', options)
}
</script>
