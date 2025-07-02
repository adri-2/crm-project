<template>
  <div class="bg-white shadow p-4 rounded-md">
    <h2 class="text-lg font-semibold text-gray-700 mb-4">
      Évolution des Stagiaires et Employés par Mois
    </h2>

    <div class="flex flex-col sm:flex-row gap-4 mb-6">
      <div class="flex flex-col flex-1">
        <label for="startDate" class="text-sm text-gray-700 font-medium mb-1"
          >Date de début</label
        >
        <input
          type="month"
          id="startDate"
          v-model="startDate"
          class="rounded-md border-gray-300 shadow-sm text-base p-2 focus:ring-blue-500 focus:border-blue-500 transition duration-150 ease-in-out"
        />
      </div>

      <div class="flex flex-col flex-1">
        <label for="endDate" class="text-sm text-gray-700 font-medium mb-1"
          >Date de fin</label
        >
        <input
          type="month"
          id="endDate"
          v-model="endDate"
          class="rounded-md border-gray-300 shadow-sm text-base p-2 focus:ring-blue-500 focus:border-blue-500 transition duration-150 ease-in-out"
        />
      </div>
    </div>

    <div
      v-if="loading"
      class="h-[300px] w-full flex items-center justify-center"
    >
      <p class="text-gray-500">Chargement des données du graphique...</p>
    </div>
    <div
      v-else-if="error"
      class="h-[300px] w-full flex items-center justify-center"
    >
      <p class="text-red-500">
        Erreur lors du chargement des données : {{ error }}
      </p>
    </div>
    <div
      v-else-if="!filteredChartData.labels.length"
      class="h-[300px] w-full flex items-center justify-center"
    >
      <p class="text-gray-500">
        Aucune donnée disponible pour la période sélectionnée.
      </p>
    </div>
    <div v-else class="h-[300px] w-full">
      <Bar :data="filteredChartData" :options="chartOptions" />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue';
import { Bar } from 'vue-chartjs';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js';

// Enregistre les composants Chart.js essentiels pour les graphiques en barres
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

// --- États Réactifs ---
// Dates de début et de fin pour le filtrage, au format 'AAAA-MM'
const startDate = ref('');
const endDate = ref('');
// État de chargement des données
const loading = ref(false);
// Message d'erreur si la récupération des données échoue
const error = ref(null);

// --- Données Brutes (Simulées) ---
// Ces données représenteraient ce que votre API Django retournerait.
// Chaque objet contient le mois, le nombre d'employés et de stagiaires.
const rawEmployeeData = ref([
  { month: '2024-01', employees: 50, interns: 5 },
  { month: '2024-02', employees: 52, interns: 6 },
  { month: '2024-03', employees: 55, interns: 7 },
  { month: '2024-04', employees: 58, interns: 8 },
  { month: '2024-05', employees: 60, interns: 9 },
  { month: '2024-06', employees: 63, interns: 10 },
  { month: '2024-07', employees: 65, interns: 11 },
  { month: '2024-08', employees: 68, interns: 12 },
  { month: '2024-09', employees: 70, interns: 13 },
  { month: '2024-10', employees: 72, interns: 14 },
  { month: '2024-11', employees: 75, interns: 15 },
  { month: '2024-12', employees: 78, interns: 16 },
  { month: '2025-01', employees: 80, interns: 17 },
  { month: '2025-02', employees: 82, interns: 18 },
  { month: '2025-03', employees: 85, interns: 19 },
  { month: '2025-04', employees: 88, interns: 20 },
  { month: '2025-05', employees: 90, interns: 21 },
  { month: '2025-06', employees: 92, interns: 22 },
  { month: '2025-07', employees: 95, interns: 23 }, // Mois actuel
]);

// --- Initialisation et Récupération des Données ---
// Définit la période par défaut (ex: les 6 derniers mois) et déclenche la récupération des données
onMounted(() => {
  const today = new Date();
  // Format 'AAAA-MM' pour le mois actuel
  const currentMonth = today.toISOString().slice(0, 7);

  // Définit la date de fin au mois actuel
  endDate.value = currentMonth;

  // Définit la date de début aux 6 mois précédents
  const sixMonthsAgo = new Date();
  sixMonthsAgo.setMonth(today.getMonth() - 5); // Soustrait 5 pour inclure le mois actuel + 5 mois précédents = 6 mois
  startDate.value = sixMonthsAgo.toISOString().slice(0, 7);

  // Appelle la fonction pour récupérer/simuler les données initiales
  fetchData();
});

// Fonction pour récupérer les données (simule un appel API)
const fetchData = async () => {
  loading.value = true; // Active l'état de chargement
  error.value = null;   // Réinitialise les erreurs précédentes
  try {
    // --- ICI : Intégrez votre appel API Django réel ---
    // Exemple d'appel réel :
    // const response = await fetch(`/api/employees-interns/?start=${startDate.value}&end=${endDate.value}`);
    // if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    // const data = await response.json();
    // rawEmployeeData.value = data; // Mettez à jour les données brutes avec celles de l'API

    // --- Simulation d'un délai réseau ---
    await new Promise(resolve => setTimeout(resolve, 800));

    // --- Simulation d'une erreur (décommenter pour tester) ---
    // if (Math.random() > 0.8) {
    //   throw new Error('Échec de la récupération des données pour la démonstration.');
    // }

  } catch (err) {
    // Capture et affiche l'erreur
    error.value = err.message || 'Une erreur inconnue est survenue.';
  } finally {
    loading.value = false; // Désactive l'état de chargement
  }
};

// Observe les changements dans les filtres de date.
// Si votre `fetchData` dépend des dates sélectionnées, décommenter `fetchData()` ici.
watch([startDate, endDate], () => {
  // fetchData(); // Décommenter si chaque changement de date doit déclencher un appel API
});

// --- Utilitaires ---
/**
 * Génère une liste de mois (au format AAAA-MM) entre deux dates (incluses).
 * @param {string} start - Date de début au format 'AAAA-MM'.
 * @param {string} end - Date de fin au format 'AAAA-MM'.
 * @returns {string[]} Tableau des mois.
 */
const getMonthsInRange = (start, end) => {
  const months = [];
  let currentDate = new Date(start + '-01'); // Crée une date pour le 1er du mois de début
  const endDateObj = new Date(end + '-01'); // Crée une date pour le 1er du mois de fin

  while (currentDate <= endDateObj) {
    months.push(currentDate.toISOString().slice(0, 7)); // Ajoute le mois au format 'AAAA-MM'
    currentDate.setMonth(currentDate.getMonth() + 1); // Passe au mois suivant
  }
  return months;
};

// --- Données du Graphique (Propriété Calculée) ---
// Cette propriété calculée prépare les données pour Chart.js en fonction des filtres de date.
const filteredChartData = computed(() => {
  // Retourne des données vides si en chargement, en erreur ou si les dates ne sont pas définies
  if (loading.value || error.value || !startDate.value || !endDate.value) {
    return { labels: [], datasets: [] };
  }

  // Récupère tous les mois dans la plage sélectionnée
  const allMonths = getMonthsInRange(startDate.value, endDate.value);

  // Initialise les données pour tous les mois à 0
  const employeeDataByMonth = allMonths.reduce((acc, month) => ({ ...acc, [month]: 0 }), {});
  const internDataByMonth = allMonths.reduce((acc, month) => ({ ...acc, [month]: 0 }), {});

  // Remplit les données avec les valeurs réelles de rawEmployeeData
  rawEmployeeData.value.forEach(item => {
    if (employeeDataByMonth.hasOwnProperty(item.month)) {
      employeeDataByMonth[item.month] = item.employees;
    }
    if (internDataByMonth.hasOwnProperty(item.month)) {
      internDataByMonth[item.month] = item.interns;
    }
  });

  // Formate les libellés des mois pour l'affichage (ex: "Juil. 25")
  const formattedLabels = allMonths.map(month => {
    const [year, mon] = month.split('-');
    const date = new Date(year, mon - 1); // Le mois est indexé à partir de 0 pour Date
    return date.toLocaleDateString('fr-FR', { month: 'short', year: '2-digit' });
  });

  // Retourne les données structurées pour Chart.js
  return {
    labels: formattedLabels,
    datasets: [
      {
        label: 'Employés',
        data: Object.values(employeeDataByMonth),
        backgroundColor: '#4F46E5', // Couleur Indigo-600 de Tailwind
        borderColor: '#4F46E5',
        borderWidth: 1,
      },
      {
        label: 'Stagiaires',
        data: Object.values(internDataByMonth),
        backgroundColor: '#10B981', // Couleur Emerald-500 de Tailwind
        borderColor: '#10B981',
        borderWidth: 1,
      }
    ]
  };
});

// --- Options du Graphique Chart.js ---
const chartOptions = {
  responsive: true,
  maintainAspectRatio: false, // Permet à Tailwind de contrôler la hauteur (h-[300px])
  plugins: {
    legend: {
      display: true, // Affiche la légende pour distinguer Employés/Stagiaires
      position: 'top',
      labels: {
        color: '#4B5563', // Couleur du texte de la légende (gris-700)
      }
    },
    title: {
      display: false, // Le titre est déjà dans le h2 du template
    },
    tooltip: {
        mode: 'index', // Affiche les données de toutes les barres pour le mois survolé
        intersect: false, // Le tooltip apparaît même si la souris n'est pas directement sur la barre
        callbacks: {
            label: function(context) {
                let label = context.dataset.label || '';
                if (label) {
                    label += ': ';
                }
                if (context.parsed.y !== null) {
                    label += context.parsed.y;
                }
                return label;
            }
        }
    }
  },
  scales: {
    x: {
      title: {
        display: true,
        text: 'Mois',
        color: '#4B5563' // Couleur du titre de l'axe X
      },
      grid: {
        display: false // Supprime les lignes de grille verticales
      }
    },
    y: {
      beginAtZero: true, // L'axe Y commence à 0
      ticks: {
        precision: 0 // Affiche des nombres entiers sur l'axe Y
      },
      title: {
        display: true,
        text: 'Nombre de Personnes',
        color: '#4B5563' // Couleur du titre de l'axe Y
      },
      grid: {
        color: 'rgba(229, 231, 235, 0.5)' // Lignes de grille horizontales légères
      }
    }
  }
};
</script>

<style scoped>
/* Aucun style spécifique n'est nécessaire ici car Tailwind CSS gère la plupart du design. */
/* Si vous aviez des styles très spécifiques qui ne sont pas gérés par Tailwind, vous les mettriez ici. */
</style>
