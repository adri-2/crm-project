<template>
  <div class="bg-white shadow p-4 rounded-md">
    <!-- <h2 class="text-lg font-semibold text-gray-700 mb-2">
      Candidats par Source
    </h2> -->
    <div class="relative h-[230px] w-full ">
      <Doughnut :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<script setup>
import { computed, watch } from 'vue';
import { Doughnut } from 'vue-chartjs';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

const props = defineProps({
    sourceData: {
        type: Object,
        default: () => ({
            'LinkedIn': 60,
            'Indeed': 35,
            'Cooptation': 15,
            'Site Carrière': 10
        })
    }
});

const backgroundColors = [
    'rgba(29, 78, 216, 0.7)',  // blue-700
    'rgba(163, 230, 53, 0.7)', // lime-400
    'rgba(249, 115, 22, 0.7)', // orange-600
    'rgba(139, 92, 246, 0.7)', // violet-500
    'rgba(244, 63, 94, 0.7)',  // rose-500 (extra color for scalability)
    'rgba(16, 185, 129, 0.7)'  // emerald-500 (extra color)
];

const chartData = computed(() => ({
    labels: Object.keys(props.sourceData),
    datasets: [
        {
            data: Object.values(props.sourceData),
            backgroundColor: backgroundColors.slice(0, Object.keys(props.sourceData).length),
            hoverOffset: 4
        }
    ]
}));

const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            position: 'right',
            labels: {
                color: '#374151', // gray-700
                font: {
                    size: 14
                }
            }
        },
        tooltip: {
            callbacks: {
                label: (context) => {
                    const label = context.label || '';
                    const value = context.parsed || 0;
                    return `${label}: ${value}`;
                }
            }
        }
    }
};
</script>
