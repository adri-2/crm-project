<template>
  <!-- <nav class="bg-gradient-to-r from-white shadow-xl rounded-xl mx-8 my-4"> -->
  <!-- <div class="flex items-center justify-between px-8 py-4"> -->
  <div class="flex items-baseline space-x-4  bg-white justify-between px-auto">
    <RouterLink to="/dashboard" :class="navClass('/dashboard')">
      Dashboard
    </RouterLink>
    <RouterLink to="/user/list" :class="navClass('/user/list')">
      Employés
    </RouterLink>
    <RouterLink to="/job/list" :class="navClass('/job/list')">
      Postes
    </RouterLink>

    <RouterLink
      to="/recruitment/offers/list"
      :class="navClass('/recruitment/offers/list')"
    >
      Recruitments
    </RouterLink>
    <RouterLink
      to="/recruitment/candidates/"
      :class="navClass('/recruitment/candidates/')"
    >
      Candidatures
    </RouterLink>
    <!-- <RouterLink to="/about" :class="navClass('/about')"> About </RouterLink> -->
  </div>
  <!-- </div> -->
  <!-- </nav> -->
</template>

<script setup>
import { useRoute,RouterLink  } from 'vue-router';


const route = useRoute();

function navClass(path) {
  return [
    'transition-all duration-200',
    'block rounded-lg px-4 py-2 text-base font-semibold tracking-wide',
    route.path === path
      ? 'bg-gradient-to-r from-blue-500 to-indigo-500 text-white shadow-lg scale-105'
      : 'text-bleu-700 hover:bg-indigo-700 hover:text-white'
  ];
}
</script>
