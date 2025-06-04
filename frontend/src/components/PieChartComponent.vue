<template>
  <div class="h-[400px]">
    <Pie :data="chartData" :options="chartOptions" />
  </div>
</template>

<script setup>
import { Pie } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, ArcElement)

const chartData = {
  labels: ['Tech', 'RH', 'Marketing', 'Finance', 'Production'],
  datasets: [
    {
      label: 'Répartition',
      data: [40, 20, 15, 10, 15],
      backgroundColor: ['#6366F1', '#10B981', '#F59E0B', '#EF4444', '#3B82F6']
    }
  ]
}

const chartOptions = {
  responsive: true,
  plugins: {
    legend: {
      position: 'top'
    },
    title: {
      display: true,
      text: 'Répartition par département'
    }
  }
}
</script>
