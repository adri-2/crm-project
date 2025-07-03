<template>
  <div
    class="min-h-screen bg-gradient-to-br from-gray-50 via-white to-indigo-100"
  >
    <nav class="bg-gradient-to-r from-white shadow-lg">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="flex h-16 items-center justify-between">
          <div class="flex items-center gap-4">
            <div
              class="shadow border-b-blue-400 border-2 rounded-full p-[1px] flex items-center justify-center"
            >
              <!-- <img
                class="size-10 drop-shadow-lg"
                src="https://tailwindcss.com/plus-assets/img/logos/mark.svg?color=indigo&shade=500"
                alt="Your Company"
              /> -->
              <img
                src="..\assets\logo1.png"
                alt=""
                class=" rounded-full flex items-center justify-center size-14 drop-shadow-lg"
              />
            </div>
            <div class="hidden md:block">
              <NavBar />
            </div>
          </div>
          <div class="md:block">
            <div class="ml-4 flex items-center md:ml-6 gap-4">
              <!-- Notifications -->
              <div
                class="relative ml-3"
                @click.stop="toggleNotifications"
                ref="notifRef"
              >
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
              <!-- User menu -->
              <div class="relative ml-3" @click.stop="toggleMenu" ref="menuRef">
                <button
                  type="button"
                  class="relative flex max-w-xs items-center rounded-full bg-indigo-800 text-sm focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-800 focus:outline-none"
                  :aria-expanded="showMenu"
                  aria-haspopup="true"
                  id="user-menu-button"
                >
                  <span class="absolute -inset-1.5"></span>
                  <img
                    class="size-10 rounded-full border-2 border-white shadow"
                    src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                    alt="User avatar"
                  />
                </button>
                <transition name="fade">
                  <div
                    v-if="showMenu"
                    class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-lg bg-white/90 py-2 shadow-2xl ring-1 ring-black/10 backdrop-blur transition-all duration-200"
                    role="menu"
                    aria-orientation="vertical"
                    aria-labelledby="user-menu-button"
                    tabindex="-1"
                  >
                    <a
                      href="#"
                      class="block px-4 py-2 text-sm text-gray-700 hover:bg-indigo-100 hover:text-indigo-700 rounded transition"
                      role="menuitem"
                      tabindex="-1"
                      id="user-menu-item-0"
                      >Votre profil</a
                    >
                    <a
                      href="#"
                      class="block px-4 py-2 text-sm text-gray-700 hover:bg-indigo-100 hover:text-indigo-700 rounded transition"
                      role="menuitem"
                      tabindex="-1"
                      id="user-menu-item-1"
                      >Paramètres</a
                    >
                    <a
                      href="#"
                      class="block px-4 py-2 text-sm text-gray-700 hover:bg-red-50 hover:text-red-600 rounded transition"
                      role="menuitem"
                      tabindex="-1"
                      id="user-menu-item-2"
                      >Déconnexion</a
                    >
                  </div>
                </transition>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- ...mobile menu unchanged... -->
      <div class="md:hidden" id="mobile-menu">
        <!-- ... -->
      </div>
    </nav>
    <main>
      <div class="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8 ">
        <RouterView />
      </div>
    </main>
  </div>
</template>

<script setup>
import NavBar from './NavBar.vue';
import { RouterLink, RouterView } from 'vue-router';
import { ref, onMounted, onUnmounted } from 'vue';

const showMenu = ref(false);
const showNotifications = ref(false);
const menuRef = ref(null);
const notifRef = ref(null);

function toggleMenu() {
  showMenu.value = !showMenu.value;
  showNotifications.value = false;
}
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

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.2s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>
