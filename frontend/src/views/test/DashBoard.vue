<template>
  <div class="bg-gray-100 min-h-screen p-4">
    <header class="bg-white shadow p-4 mb-4 rounded-md">
      <h1 class="text-xl font-semibold text-gray-800">
        Tableau de Bord Recrutement
      </h1>
    </header>
    <main class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <PipelineOverview />

      <KPICard title="Délai Moyen de Recrutement" value="45 jours" />
      <KPICard title="Coût par Embauche" value="5000 $" />
      <KPICard title="Taux d'Acceptation Offres" value="85%" />
      <KPICard title="Taux de Rétention 6 Mois" value="92%" />

      <RecruitmentFunnelChart :pipelineData="pipelineData" />
      <SourceDoughnutChart :sourceData="sourceData" />

      <div class="bg-white shadow p-4 rounded-md">
        <h2 class="text-lg font-semibold text-gray-700 mb-2">Postes Urgents</h2>
        <ul>
          <li class="py-1">Développeur Front-end</li>
          <li class="py-1">Chef de Projet Technique</li>
        </ul>
      </div>

      <div class="bg-white shadow p-4 rounded-md col-span-full">
        <h2 class="text-lg font-semibold text-gray-700 mb-2">
          Activités des Recruteurs
        </h2>
        <p class="text-gray-500">
          Graphique d'activités des recruteurs (à implémenter)
        </p>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import PipelineOverview from './PipelineOverview.vue'; // Gardons cette vue d'ensemble textuelle
import KPICard from './KPICard.vue';
import RecruitmentFunnelChart from './RecruitmentFunnelChart.vue';
import SourceDoughnutChart from './SourceDoughnutChart.vue';

// Données d'exemple (elles viendraient de votre API Django en production)
const pipelineData = ref({
  'Candidatures': 120,
  'Présélection': 85,
  'Entretiens': 55,
  'Offres': 20,
  'Embauchés': 15
});

const sourceData = ref({
  'LinkedIn': 60,
  'Indeed': 35,
  'Cooptation': 15,
  'Site Carrière': 10
});

// Fonction pour simuler la mise à jour des données (pour le test)
// setTimeout(() => {
//   pipelineData.value['Candidatures'] = 150;
//   sourceData.value['LinkedIn'] = 75;
// }, 5000);
</script>
