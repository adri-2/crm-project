<template>
  <div class="p-6 bg-white rounded-lg shadow">
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
        class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg text-sm"
      >
        Nouveau
      </RouterLink>
    </div>

    <div class="overflow-x-auto">
      <table class="min-w-full text-sm text-left text-gray-700">
        <thead class="text-xs uppercase text-gray-500 border-b">
          <tr>
            <th class="px-4 py-3">Nom</th>
            <th class="px-4 py-3">Postulé le</th>
            <th class="px-4 py-3">Poste</th>
            <th class="px-4 py-3">Statut</th>
            <th class="px-4 py-3">Raison refus</th>
            <th class="px-4 py-3">Évaluation</th>
            <th class="px-4 py-3">Email</th>
            <th class="px-4 py-3">Étiquettes</th>
            <th class="px-4 py-3">Recruteur</th>
            <th class="px-4 py-3">Téléphone</th>
            <th class="px-4 py-3">Médium</th>
            <th class="px-4 py-3">Source</th>
            <th class="px-4 py-3"></th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="app in applications"
            :key="app.id"
            class="border-b hover:bg-gray-50"
          >
            <td class="px-4 py-3 font-medium text-gray-900">{{ app.name }}</td>
            <td class="px-4 py-3">{{ formatDate(app.applied_at) }}</td>
            <td class="px-4 py-3">{{ app.position }}</td>
            <td class="px-4 py-3">{{ app.status }}</td>
            <td class="px-4 py-3 text-red-500">{{ app.rejection_reason }}</td>
            <td class="px-4 py-3">{{ app.evaluation }}</td>
            <td class="px-4 py-3">{{ app.email }}</td>
            <td class="px-4 py-3">{{ app.tags.join(', ') }}</td>
            <td class="px-4 py-3">{{ app.recruiter }}</td>
            <td class="px-4 py-3">{{ app.phone }}</td>
            <td class="px-4 py-3">{{ app.medium }}</td>
            <td class="px-4 py-3">{{ app.source }}</td>
            <td
              class="px-4 py-3 text-indigo-600 font-medium cursor-pointer hover:underline"
            >
              Voir
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
const applications = [
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
  }
];

// Formateur de date
const formatDate = (dateStr) => {
  const options = { year: 'numeric', month: 'short', day: 'numeric' }
  return new Date(dateStr).toLocaleDateString('fr-FR', options)
}
</script>
