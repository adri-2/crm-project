<template>
  <div class="w-full">
    <!-- Filtres par date -->
    <div class="flex flex-col sm:flex-row gap-4 mb-4">
      <div class="flex flex-col">
        <label for="startDate" class="text-sm text-gray-700">Début</label>
        <input
          type="date"
          id="startDate"
          v-model="startDate"
          class="rounded-md border-gray-300 shadow-sm text-sm"
        />
      </div>

      <div class="flex flex-col">
        <label for="endDate" class="text-sm text-gray-700">Fin</label>
        <input
          type="date"
          id="endDate"
          v-model="endDate"
          class="rounded-md border-gray-300 shadow-sm text-sm"
        />
      </div>
    </div>

    <!-- Graphique -->
    <div class="h-[300px] w-full">
      <Bar :data="filteredChartData" :options="chartOptions" />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

// Données initiales
const rawData = [
  { date: '2024-01-02', value: 5 },
  { date: '2024-01-04', value: 38 },
  { date: '2024-01-07', value: 106 },
  { date: '2024-02-03', value: 140 },
  { date: '2024-02-05', value: 94 },
  { date: '2024-03-05', value: 70 },
  { date: '2024-04-06', value: 140 },
  { date: '2024-05-07', value: 94 },
  { date: '2024-06-07', value: 70 },
  { date: '2024-07-02', value: 5 },
  { date: '2024-08-04', value: 38 },
  { date: '2024-09-07', value: 106 },
  { date: '2024-10-03', value: 140 },
  { date: '2024-11-05', value: 94 },
  { date: '2024-13-05', value: 70 },
  { date: '2024-14-06', value: 140 },
  { date: '2024-15-07', value: 94 },
  { date: '2024-16-07', value: 70 },
]

// Filtres de date
const startDate = ref('')
const endDate = ref('')

// Données filtrées pour le chart
const filteredChartData = computed(() => {
  const filtered = rawData.filter(item => {
    const itemDate = new Date(item.date)
    const start = startDate.value ? new Date(startDate.value) : null
    const end = endDate.value ? new Date(endDate.value) : null
    return (!start || itemDate >= start) && (!end || itemDate <= end)
  })

  return {
    labels: filtered.map(d => new Date(d.date).toLocaleDateString('fr-FR', { day: '2-digit', month: 'short' })),
    datasets: [
      {
        label: 'Embauches',
        data: filtered.map(d => d.value),
        backgroundColor: '#4F46E5'
      }
    ]
  }
})

const chartOptions = {
  responsive: true,
  plugins: {
    legend: { display: false },
    title: {
      display: true,
      text: 'Embauches sur période sélectionnée'
    }
  },
  scales: {
    y: {
      beginAtZero: true,
      ticks: { precision: 0 }
    }
  }
}
</script>
