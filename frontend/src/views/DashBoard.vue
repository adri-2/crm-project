<template>
  <!-- En-tête -->
  <div
    class="p-8 bg-gradient-to-br  bg-white/85 min-h-screen shadow-2xl rounded-2xl"
  >
    <header
      class="mb-8 flex flex-col md:flex-row md:items-center md:justify-between"
    >
      <!-- Titre et sous-titre -->
      <div>
        <h1 class="text-3xl font-extrabold text-blue-900 tracking-tight">
          RH Dashboard
        </h1>
        <p class="text-gray-500 mt-1">Vue d'ensemble des activités RH</p>
      </div>
      <!-- Boutons -->
      <div class="mt-4 md:mt-0 flex space-x-2">
        <button
          class="bg-blue-600 text-white px-4 py-2 rounded-lg shadow hover:bg-blue-700 transition"
        >
          Exporter
        </button>
        <button
          class="bg-white border border-blue-600 text-blue-600 px-4 py-2 rounded-lg shadow hover:bg-blue-50 transition"
        >
          Paramètres
        </button>
      </div>
    </header>

    <!-- Statistiques principales -->
    <section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8 ">
      <div
        class="bg-blue-800 rounded-2xl shadow-lg p-6 flex flex-col items-start hover:shadow-2xl transition"
      >
        <h3 class="text-sm text-white mb-1">Employés</h3>
        <p class="text-3xl font-bold text-white">125</p>
      </div>
      <div
        class="bg-green-600 rounded-2xl shadow-lg p-6 flex flex-col items-start hover:shadow-xl transition"
      >
        <h3 class="text-sm text-white mb-1">Candidatures</h3>
        <p class="text-3xl font-bold text-white">38</p>
      </div>
      <div
        class="bg-orange-600  rounded-2xl shadow-lg p-6 flex flex-col items-start hover:shadow-xl transition"
      >
        <h3 class="text-sm text-white mb-1">Présences aujourd'hui</h3>
        <p class="text-3xl font-bold text-white">92</p>
      </div>
      <div
        class="bg-red-600 rounded-2xl shadow-lg p-6 flex flex-col items-start hover:shadow-xl transition"
      >
        <h3 class="text-sm text-white mb-1">Absences</h3>
        <p class="text-3xl font-bold text-white">8</p>
      </div>
    </section>

    <!-- Graphiques principaux -->
    <section class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
      <!-- Répartition par département -->
      <div
        class="bg-white rounded-2xl shadow-lg p-6 hover:shadow-xl transition h-90"
      >
        <h2 class="text-lg font-semibold text-gray-700 mb-4 flex items-center">
          <span
            class="inline-block w-2 h-2 bg-blue-500 rounded-full mr-2"
          ></span>
          Répartition par département
        </h2>
        <PieChartComponent />
      </div>
      <!-- Candidats par source -->
      <div
        class="bg-white rounded-2xl shadow-lg p-6 w-full h-90 hover:shadow-xl transition"
      >
        <h2 class="text-lg font-semibold text-gray-700 mb-4 flex items-center">
          <span
            class="inline-block w-2 h-2 bg-red-500 rounded-full mr-2"
          ></span>
          Candidats par source
        </h2>
        <SourceDoughnutChart />
      </div>
      <!-- (BarChartComponent commenté) -->
    </section>

    <!-- Présence par mois -->
    <section class="mb-8 w-full">
      <div
        class="bg-white rounded-2xl shadow-lg p-6 w-full hover:shadow-xl transition"
      >
        <h2 class="text-lg font-semibold text-gray-700 mb-4 flex items-center">
          <span
            class="inline-block w-2 h-2 bg-green-500 rounded-full mr-2"
          ></span>
          Présence par mois
        </h2>
        <BarChartPresence />
      </div>
    </section>

    <!-- Entonnoir de recrutement -->
    <section class="mb-8 w-full">
      <div
        class="bg-white rounded-2xl shadow-lg p-6 w-full hover:shadow-xl transition"
      >
        <h2 class="text-lg font-semibold text-gray-700 mb-4 flex items-center">
          <span
            class="inline-block w-2 h-2 bg-yellow-500 rounded-full mr-2"
          ></span>
          Entonnoir de recrutement
        </h2>
        <RecruitmentFunnelChart />
      </div>
    </section>

    <!-- Activité récente -->
    <section class="bg-white rounded-2xl shadow-lg p-6">
      <h2 class="text-lg font-semibold text-gray-700 mb-4 flex items-center">
        <span class="inline-block w-2 h-2 bg-gray-400 rounded-full mr-2"></span>
        Activité récente
      </h2>
      <ul class="divide-y divide-gray-200">
        <li class="py-3 flex justify-between text-sm text-gray-700">
          <span class="font-medium">Nouvelle candidature :</span>
          <span>Jean Dupont (Développeur)</span>
          <span class="text-gray-400">il y a 2 heures</span>
        </li>
        <li class="py-3 flex justify-between text-sm text-gray-700">
          <span class="font-medium">Absence signalée :</span>
          <span>Claire Martin</span>
          <span class="text-gray-400">il y a 3 heures</span>
        </li>
        <li class="py-3 flex justify-between text-sm text-gray-700">
          <span class="font-medium">Contrat signé :</span>
          <span>Romain Lefebvre</span>
          <span class="text-gray-400">il y a 1 jour</span>
        </li>
      </ul>
    </section>
  </div>
</template>

<script setup>
// Import des composants graphiques
import PieChartComponent from '@/components/PieChartComponent.vue';
import BarChartComponent from '@/components/BarChartComponent.vue';
import BarChartPresence from '@/components/BarChartPresence.vue';
import RecruitmentFunnelChart from './test/RecruitmentFunnelChart.vue';
import SourceDoughnutChart from './test/SourceDoughnutChart.vue';
</script>
