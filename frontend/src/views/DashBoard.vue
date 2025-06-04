<template>
  <div class="p-6 bg-gray-50 min-h-screen">
    <header class="mb-6">
      <h1 class="text-2xl font-bold text-gray-800">RH Dashboard</h1>
      <p class="text-gray-500">Vue d'ensemble des activités RH</p>
    </header>

    <section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6 ">
      <div class="bg-white rounded-lg shadow p-4">
        <h3 class="text-sm text-gray-500">Employés</h3>
        <p class="text-2xl font-semibold text-gray-800">125</p>
      </div>
      <div class="bg-white rounded-lg shadow p-4">
        <h3 class="text-sm text-gray-500">Candidatures</h3>
        <p class="text-2xl font-semibold text-gray-800">38</p>
      </div>
      <div class="bg-white rounded-lg shadow p-4">
        <h3 class="text-sm text-gray-500">Présences aujourd'hui</h3>
        <p class="text-2xl font-semibold text-green-600">92</p>
      </div>
      <div class="bg-white rounded-lg shadow p-4">
        <h3 class="text-sm text-gray-500">Absences</h3>
        <p class="text-2xl font-semibold text-red-600">8</p>
      </div>
    </section>

    <section class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6 ">
      <div class="bg-white rounded-lg shadow p-4">
        <h2 class="text-lg font-semibold text-gray-700 mb-2 ">
          Répartition par département
        </h2>
        <PieChartComponent />
      </div>
      <div class="bg-white rounded-lg shadow p-4">
        <h2 class="text-lg font-semibold text-gray-700 mb-2 ">
          Embauches par mois
        </h2>
        <BarChartComponent />
      </div>
    </section>

    <section class="mb-6 w-full">
      <div class="bg-white rounded-lg shadow p-4 w-full">
        <h2 class="text-lg font-semibold text-gray-700 mb-2 ">
          Presence par mois
        </h2>
        <BarChartPresence />
      </div>
    </section>

    <section class="bg-white rounded-lg shadow p-4">
      <h2 class="text-lg font-semibold text-gray-700 mb-2">Activité récente</h2>
      <ul class="divide-y divide-gray-200">
        <li class="py-2 flex justify-between text-sm text-gray-600">
          <span>Nouvelle candidature : Jean Dupont (Développeur)</span>
          <span>il y a 2 heures</span>
        </li>
        <li class="py-2 flex justify-between text-sm text-gray-600">
          <span>Absence signalée : Claire Martin</span>
          <span>il y a 3 heures</span>
        </li>
        <li class="py-2 flex justify-between text-sm text-gray-600">
          <span>Contrat signé : Romain Lefebvre</span>
          <span>il y a 1 jour</span>
        </li>
      </ul>
    </section>
  </div>
</template>

<script setup>
import PieChartComponent from '@/components/PieChartComponent.vue';
import BarChartComponent from '@/components/BarChartComponent.vue';
import BarChartPresence from '@/components/BarChartPresence.vue';
</script>
