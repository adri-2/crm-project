<template>
  <!-- <header> -->
  <div class="ml-10 flex items-baseline space-x-4">
    <!-- <RouterLink
      to="/"
      @click="activeButton = 'home'"
      :class="[
    'block rounded-md px-3 py-2 text-base font-medium',
    activeButton === 'home'
      ? 'bg-gray-900 text-white'
      : 'text-gray-300 hover:bg-gray-700 hover:text-white'
  ]"
    >
      Home
    </RouterLink> -->

    <RouterLink
      to="/"
      @click="activeButton = 'dashboard'"
      :class="[
    'block rounded-md px-3 py-2 text-base font-medium',
    activeButton === 'dashboard'
      ? 'bg-gray-900 text-white'
      : 'text-gray-300 hover:bg-gray-700 hover:text-white'
  ]"
    >
      dashboard
    </RouterLink>

    <RouterLink
      to="/user/list"
      @click="activeButton = 'user'"
      :class="[
    'block rounded-md px-3 py-2 text-base font-medium',
    activeButton === 'user'
      ? 'bg-gray-900 text-white'
      : 'text-gray-300 hover:bg-gray-700 hover:text-white'
  ]"
    >
      List user
    </RouterLink>

    <RouterLink
      to="/job/list"
      @click="activeButton = 'job'"
      :class="[
    'block rounded-md px-3 py-2 text-base font-medium',
    activeButton === 'job'
      ? 'bg-gray-900 text-white'
      : 'text-gray-300 hover:bg-gray-700 hover:text-white'
  ]"
    >
      Job List
    </RouterLink>

    <RouterLink
      to="/about"
      @click="activeButton = 'about'"
      :class="[
    'block rounded-md px-3 py-2 text-base font-medium',
    activeButton === 'about'
      ? 'bg-gray-900 text-white'
      : 'text-gray-300 hover:bg-gray-700 hover:text-white'
  ]"
    >
      About
    </RouterLink>

    <RouterLink
      to="/recruitment/offers/list"
      @click="activeButton = 'recruitment-list'"
      :class="[
    'block rounded-md px-3 py-2 text-base font-medium',
    activeButton === 'recruitment-list'
      ? 'bg-gray-900 text-white'
      : 'text-gray-300 hover:bg-gray-700 hover:text-white'
  ]"
    >
      recruitment
    </RouterLink>
    <RouterLink
      to="/recruitment/candidates/"
      @click="activeButton = 'candidates'"
      :class="[
    'block rounded-md px-3 py-2 text-base font-medium',
    activeButton === 'candidates'
      ? 'bg-gray-900 text-white'
      : 'text-gray-300 hover:bg-gray-700 hover:text-white'
  ]"
    >
      candidates
    </RouterLink>
  </div>
</template>

<script setup>
import { ref } from 'vue';
const activeButton = ref('dashboard');

import { RouterLink } from 'vue-router';
</script>
