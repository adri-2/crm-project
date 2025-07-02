<template>
  <div class="bg-white shadow p-4 rounded-md">
    <h2 class="text-lg font-semibold text-gray-700 mb-4">
      Entonnoir de Recrutement
    </h2>

    <div v-if="loading" class="flex justify-center items-center h-48">
      <p class="text-gray-500">Chargement des données de l'entonnoir...</p>
    </div>
    <div v-else-if="error" class="flex justify-center items-center h-48">
      <p class="text-red-500">
        Erreur lors du chargement des données : {{ error }}
      </p>
    </div>
    <div v-else>
      <Bar :data="chartData" :options="mergedChartOptions" />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue';
// Assurez-vous d'avoir bien installé 'vue-chartjs'
// npm install chart.js vue-chartjs
import { Bar } from 'vue-chartjs';
import { Chart, registerables } from 'chart.js';

// Enregistre tous les composants Chart.js nécessaires
Chart.register(...registerables);

// --- Props du composant ---
const props = defineProps({
  // Données du pipeline, avec une valeur par défaut pour le développement/mock
  pipelineData: {
    type: Object,
    default: () => ({
      'Candidatures': 120,
      'Présélection': 85,
      'Entretiens': 55,
      'Offres': 20,
      'Embauchés': 15
    })
  },
  // Optionnel : permettre de surcharger les options par défaut de Chart.js
  chartCustomOptions: {
    type: Object,
    default: () => ({})
  },
  // Optionnel : simuler un chargement asynchrone (utile pour les démos)
  simulateLoading: {
    type: Boolean,
    default: false
  },
  // Optionnel : simuler une erreur de chargement
  simulateError: {
    type: Boolean,
    default: false
  }
});

// --- États réactifs ---
const loading = ref(false);
const error = ref(null);

// Couleurs personnalisées pour les étapes de l'entonnoir
// Plus facile à gérer et réutiliser
const FUNNEL_COLORS = {
  backgroundColor: [
    'rgba(59, 130, 246, 0.6)', // Bleu - Candidatures
    'rgba(245, 158, 11, 0.6)', // Jaune - Présélection
    'rgba(34, 197, 94, 0.6)',  // Vert - Entretiens
    'rgba(99, 102, 241, 0.6)', // Indigo - Offres
    'rgba(168, 85, 247, 0.6)'  // Violet - Embauchés
  ],
  borderColor: [
    'rgba(59, 130, 246, 1)',
    'rgba(245, 158, 11, 1)',
    'rgba(34, 197, 94, 1)',
    'rgba(99, 102, 241, 1)',
    'rgba(168, 85, 247, 1)'
  ]
};

// --- Données du graphique (Computed Property pour la réactivité) ---
// Utilise computed pour que les données du graphique se recalculent
// automatiquement si pipelineData change.
const chartData = computed(() => {
  return {
    labels: Object.keys(props.pipelineData),
    datasets: [
      {
        label: 'Nombre de Candidats',
        data: Object.values(props.pipelineData),
        backgroundColor: FUNNEL_COLORS.backgroundColor,
        borderColor: FUNNEL_COLORS.borderColor,
        borderWidth: 1,
      },
    ],
  };
});

// --- Options par défaut du graphique ---
const defaultChartOptions = {
  responsive: true,
  maintainAspectRatio: false, // Important pour contrôler la taille avec Tailwind CSS
  indexAxis: 'y', // Barres horizontales pour un effet entonnoir
  plugins: {
    legend: {
      display: false, // La légende est souvent redondante pour un entonnoir simple
    },
    title: {
      display: false, // Le titre est déjà dans le h2 du template
      text: 'Entonnoir de Recrutement',
    },
    tooltip: {
        callbacks: {
            // Afficher le pourcentage et le nombre dans l'info-bulle
            label: function(context) {
                let label = context.dataset.label || '';
                if (label) {
                    label += ': ';
                }
                const value = context.parsed.x;
                const total = context.dataset.data.reduce((a, b) => a + b, 0);
                const percentage = total > 0 ? ((value / total) * 100).toFixed(1) : 0;
                return `${label}${value} (${percentage}%)`;
            }
        }
    }
  },
  scales: {
    x: {
      beginAtZero: true,
      title: {
        display: true,
        text: 'Nombre de Candidats',
        color: '#4B5563' // gray-700
      },
      grid: {
        color: 'rgba(229, 231, 235, 0.5)' // gray-200 avec transparence
      }
    },
    y: {
      title: {
        display: true,
        text: 'Étapes du Pipeline',
        color: '#4B5563' // gray-700
      },
      grid: {
        color: 'rgba(229, 231, 235, 0.5)'
      }
    }
  }
};

// --- Options finales du graphique (Computed Property) ---
// Fusionne les options par défaut avec les options personnalisées passées via props
const mergedChartOptions = computed(() => {
  // Utiliser une fusion profonde si les options personnalisées peuvent modifier des objets imbriqués
  // Pour cet exemple simple, Object.assign est suffisant, mais lodash.merge pourrait être mieux pour des cas complexes.
  return { ...defaultChartOptions, ...props.chartCustomOptions };
});

// --- Logique de chargement simulée (pour le développement) ---
onMounted(() => {
  if (props.simulateLoading) {
    loading.value = true;
    error.value = null; // Réinitialiser l'erreur si on simule un nouveau chargement
    setTimeout(() => {
      loading.value = false;
      if (props.simulateError) {
        error.value = 'Échec de la récupération des données de l\'API.';
      }
    }, 1500); // Simuler un délai de 1.5 secondes
  }
});

// Watch n'est plus strictement nécessaire pour mettre à jour `chartData.value.labels`
// et `chartData.value.datasets[0].data` car `chartData` est maintenant un `computed`
// qui dépend directement de `props.pipelineData`.
// Cependant, si vous aviez d'autres logiques de transformation qui ne sont pas `computed`,
// un `watch` pourrait être utile.
// Pour cet exemple, le `computed` fait le travail efficacement.
</script>

<style scoped>
/* Optionnel: Styles spécifiques au composant si nécessaire, bien que Tailwind CSS soit préféré */
</style>
