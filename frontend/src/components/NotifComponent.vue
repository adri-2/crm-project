<template>
  <div class="relative ml-3" @click.stop="toggleNotifications" ref="notifRef">
    <button
      type="button"
      class="relative rounded-full bg-indigo-800 p-2 text-indigo-200 hover:text-white hover:bg-indigo-700 transition focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-800 focus:outline-none"
      :aria-expanded="showNotifications"
      aria-haspopup="true"
      aria-controls="notification-menu"
      id="notification-menu-button"
      tabindex="0"
    >
      <svg
        class="size-6"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M14.857 17.082a23.848 23.848 0 0 0 5.454-1.31A8.967 8.967 0 0 1 18 9.75V9A6 6 0 0 0 6 9v.75a8.967 8.967 0 0 1-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 0 1-5.714 0m5.714 0a3 3 0 1 1-5.714 0"
        />
      </svg>
    </button>
    <transition name="fade">
      <div
        v-if="showNotifications"
        class="absolute right-0 z-10 mt-2 w-64 origin-top-right rounded-lg bg-white/90 py-2 shadow-2xl ring-1 ring-black/10 backdrop-blur transition-all duration-200"
        role="menu"
        aria-orientation="vertical"
        aria-labelledby="notification-menu-button"
        tabindex="-1"
        id="notification-menu"
      >
        <p class="px-4 py-2 text-gray-700">Notification 1</p>
        <p class="px-4 py-2 text-gray-700">Notification 2</p>
      </div>
    </transition>
  </div>
</template>

<script setup>

import { ref, onMounted, onUnmounted } from 'vue';

const showNotifications = ref(false);

const notifRef = ref(null);


function toggleNotifications() {
  showNotifications.value = !showNotifications.value;
  showMenu.value = false;
}

function handleClickOutside(e) {
  if (
    menuRef.value && !menuRef.value.contains(e.target) &&
    notifRef.value && !notifRef.value.contains(e.target)
  ) {
    showMenu.value = false;
    showNotifications.value = false;
  }
}

onMounted(() => document.addEventListener('click', handleClickOutside));
onUnmounted(() => document.removeEventListener('click', handleClickOutside));
</script>
