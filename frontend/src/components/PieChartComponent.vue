<template>
  <div class="rounded-md p-4 shadow">
    <div
      v-if="loading"
      class="h-[230px] w-full flex items-center justify-center"
    >
      <p class="text-gray-500">Chargement des données...</p>
    </div>
    <div
      v-else-if="error"
      class="h-[230px] w-full flex items-center justify-center"
    >
      <p class="text-red-500">Erreur: {{ error }}</p>
    </div>
    <div v-else class="h-[230px] w-full flex items-center justify-center">
      <Pie :data="chartData" :options="mergedChartOptions" />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue';
import { Pie } from 'vue-chartjs';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement
} from 'chart.js';

// Register the necessary Chart.js components
ChartJS.register(Title, Tooltip, Legend, ArcElement);

// --- Component Props ---
const props = defineProps({
  // Data for the pie chart, expected as an object { label: value, ... }
  // Example: { 'Tech': 40, 'RH': 20, 'Marketing': 15 }
  departmentData: {
    type: Object,
    default: () => ({
      'Tech': 40,
      'RH': 20,
      'Marketing': 15,
      'Finance': 10,
      'Production': 15
    })
  },
  // Optional: Allows overriding default Chart.js options
  chartCustomOptions: {
    type: Object,
    default: () => ({})
  },
  // Optional: Simulate loading state for development/demo
  simulateLoading: {
    type: Boolean,
    default: false
  },
  // Optional: Simulate error state for development/demo
  simulateError: {
    type: Boolean,
    default: false
  }
});

// --- Reactive States ---
const loading = ref(false);
const error = ref(null);

// --- Chart Data (Computed Property for Reactivity) ---
// This computed property ensures the chart data updates whenever
// props.departmentData changes.
const chartData = computed(() => {
  return {
    labels: Object.keys(props.departmentData),
    datasets: [
      {
        label: 'Répartition',
        data: Object.values(props.departmentData),
        backgroundColor: [
          '#6366F1', // Indigo-500
          '#10B981', // Emerald-500
          '#F59E0B', // Amber-500
          '#EF4444', // Red-500
          '#3B82F6'  // Blue-500
        ],
        // Adding hover border for better visual feedback
        hoverBorderColor: '#ffffff',
        hoverBorderWidth: 4,
      }
    ]
  };
});

// --- Default Chart Options ---
const defaultChartOptions = {
  responsive: true,
  maintainAspectRatio: false, // Essential for controlling size with Tailwind's h-[330px]
  plugins: {
    legend: {
      position: 'right', // Place legend on the right for better use of space
      labels: {
        color: '#4B5563', // Tailwind's gray-700 for legend text
        font: {
          size: 14, // Slightly larger font for readability
        }
      }
    },
    title: {
      display: false, // Title is handled by the h2 tag
      text: 'Répartition par département'
    },
    tooltip: {
        // Customize tooltip to show percentage
        callbacks: {
            label: function(context) {
                let label = context.label || '';
                if (label) {
                    label += ': ';
                }
                const value = context.parsed;
                const total = context.dataset.data.reduce((a, b) => a + b, 0);
                const percentage = total > 0 ? ((value / total) * 100).toFixed(1) : 0;
                return `${label}${value} (${percentage}%)`;
            }
        }
    }
  }
};

// --- Merged Chart Options (Computed Property) ---
// Combines default options with any custom options provided via props.
const mergedChartOptions = computed(() => {
  // A simple merge for top-level properties. For deep merges, consider a utility like lodash.merge.
  return { ...defaultChartOptions, ...props.chartCustomOptions };
});

// --- Loading and Error Simulation (for Development) ---
onMounted(() => {
  if (props.simulateLoading) {
    loading.value = true;
    error.value = null; // Clear previous errors
    setTimeout(() => {
      loading.value = false;
      if (props.simulateError) {
        error.value = 'Failed to fetch department data.';
      }
    }, 1500); // Simulate 1.5 seconds loading time
  }
});
</script>

<style scoped>
/* No specific scoped styles needed as Tailwind CSS handles most of the styling */
</style>
