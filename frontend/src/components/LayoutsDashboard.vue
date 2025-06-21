<template>
  <div
    class="min-h-screen bg-gradient-to-br from-gray-50 via-white to-indigo-100"
  >
    <nav class="bg-gradient-to-r from-indigo-700 to-indigo-900 shadow-lg">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="flex h-16 items-center justify-between">
          <div class="flex items-center gap-4">
            <div class="shrink-0">
              <img
                class="size-10 drop-shadow-lg"
                src="https://tailwindcss.com/plus-assets/img/logos/mark.svg?color=indigo&shade=500"
                alt="Your Company"
              />
            </div>
            <div class="hidden md:block">
              <NavBar />
            </div>
          </div>
          <div class="hidden md:block">
            <div class="ml-4 flex items-center md:ml-6 gap-4">
              <button
                type="button"
                class="relative rounded-full bg-indigo-800 p-2 text-indigo-200 hover:text-white hover:bg-indigo-700 transition focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-800 focus:outline-none"
              >
                <span class="absolute -inset-1.5"></span>
                <span class="sr-only">View notifications</span>
                <svg
                  class="size-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  aria-hidden="true"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M14.857 17.082a23.848 23.848 0 0 0 5.454-1.31A8.967 8.967 0 0 1 18 9.75V9A6 6 0 0 0 6 9v.75a8.967 8.967 0 0 1-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 0 1-5.714 0m5.714 0a3 3 0 1 1-5.714 0"
                  />
                </svg>
              </button>
              <div class="relative ml-3">
                <div>
                  <button
                    type="button"
                    class="relative flex max-w-xs items-center rounded-full bg-indigo-800 text-sm focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-800 focus:outline-none"
                    id="user-menu-button"
                    aria-expanded="false"
                    aria-haspopup="true"
                  >
                    <span class="absolute -inset-1.5"></span>
                    <span class="sr-only">Open user menu</span>
                    <img
                      class="size-10 rounded-full border-2 border-white shadow"
                      src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                      alt=""
                    />
                  </button>
                </div>
                <div
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
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Mobile menu placeholder -->
      <div class="md:hidden" id="mobile-menu"></div>
    </nav>

    <header class="bg-white/80 shadow-2xl backdrop-blur-lg rounded-b-xl">
      <div
        class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8 flex items-center gap-4"
      >
        <svg
          class="size-10 text-indigo-500 drop-shadow"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M3 12l2-2m0 0l7-7 7 7M13 5v6h6m-6 0v6m0 0H7m6 0h6"
          />
        </svg>
        <h1
          class="text-4xl font-extrabold tracking-tight text-indigo-900 drop-shadow"
        >
          Dashboard
        </h1>
      </div>
    </header>
    <main>
      <div class="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8">
        <!-- <div class="rounded-2xl bg-gray-100 shadow-2xl p-10 min-h-[400px]"> -->
        <RouterView />
        <!-- </div> -->
      </div>
    </main>
  </div>
</template>
<script setup>
import NavBar from './NavBar.vue';
import { RouterLink, RouterView } from 'vue-router';
</script>
