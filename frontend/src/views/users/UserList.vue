<template>
  <div class="p-6 bg-white rounded-lg shadow-2xl drop-shadow">
    <div class="flex justify-between items-center mb-4">
      <div>
        <h2 class="text-xl font-semibold text-gray-800">Users</h2>
        <p class="text-sm text-gray-500">
          A list of all the users in your account including their name, title,
          email and role.
        </p>
      </div>
      <RouterLink
        to="/user/new"
        class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg text-sm"
      >
        Add user
      </RouterLink>
    </div>

    <div
      class="flex flex-col justify-between overflow-x-auto bg-white min-h-[400px]"
    >
      <table class="min-w-full text-sm text-left text-gray-700">
        <thead class="text-xs uppercase text-gray-500 border-b">
          <tr>
            <th class="px-4 py-3">Name</th>
            <th class="px-4 py-3">Title</th>
            <th class="px-4 py-3">Email</th>
            <th class="px-4 py-3">Role</th>
            <th class="px-4 py-3"></th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="user in paginatedUsers"
            :key="user.email + user.name"
            class="border-b hover:bg-gray-50"
          >
            <td class="px-4 py-3 font-medium text-gray-900">{{ user.name }}</td>
            <td class="px-4 py-3 text-indigo-600">{{ user.title }}</td>
            <td class="px-4 py-3">{{ user.email }}</td>
            <td class="px-4 py-3">{{ user.role }}</td>
            <td>
              <RouterLink
                :to="`/user/edit/${encodeURIComponent(user.email)}`"
                class="px-4 py-3 text-indigo-600 font-medium cursor-pointer hover:underline"
              >
                Edit
              </RouterLink>
            </td>
          </tr>
          <tr v-if="paginatedUsers.length === 0">
            <td colspan="5" class="text-center py-6 text-gray-400">
              No users found.
            </td>
          </tr>
        </tbody>
      </table>

      <div class="mt-6 flex justify-between items-center">
        <p class="text-sm text-gray-700">
          Showing
          <span class="font-medium">{{ startIndex + 1 }}</span>
          to
          <span class="font-medium">{{ endIndex }}</span>
          of
          <span class="font-medium">{{ allUsers.length }}</span>
          results
        </p>
        <div class="flex gap-1">
          <button
            @click="goToPage(currentPage - 1)"
            :disabled="currentPage === 1"
            class="px-3 py-1 text-sm rounded border border-gray-300 text-gray-700 hover:bg-gray-50 disabled:opacity-50"
          >
            Previous
          </button>
          <button
            v-for="page in visiblePages"
            :key="page"
            @click="goToPage(page)"
            :class="[
              'px-3 py-1 text-sm rounded border',
              page === currentPage
                ? 'bg-indigo-600 text-white border-indigo-600'
                : 'border-gray-300 text-gray-700 hover:bg-gray-50'
            ]"
          >
            {{ page }}
          </button>
          <button
            @click="goToPage(currentPage + 1)"
            :disabled="currentPage === totalPages"
            class="px-3 py-1 text-sm rounded border border-gray-300 text-gray-700 hover:bg-gray-50 disabled:opacity-50"
          >
            Next
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { RouterLink } from 'vue-router';

const perPage = 10;
const currentPage = ref(1);

const allUsers = [
  { name: "Lindsay Walton", title: "Front-end Developer", email: "lindsay.walton@example.com", role: "Member" },
  { name: "Courtney Henry", title: "Designer", email: "courtney.henry@example.com", role: "Admin" },
  { name: "Tom Cook", title: "Director of Product", email: "tom.cook@example.com", role: "Member" },
  { name: "Whitney Francis", title: "Copywriter", email: "whitney.francis@example.com", role: "Admin" },
  { name: "Leonard Krasner", title: "Senior Designer", email: "leonard.krasner@example.com", role: "Owner" },
  { name: "Floyd Miles", title: "Principal Designer", email: "floyd.miles@example.com", role: "Member" },
  { name: "Robert Fox", title: "UX Researcher", email: "robert.fox@example.com", role: "Member" },
  { name: "Albert Flores", title: "Manager", email: "albert.flores@example.com", role: "Admin" },
  // Ajoutez d'autres utilisateurs ici...
  { name: "Lindsay Walton", title: "Front-end Developer", email: "lindsay.walton@example.com", role: "Member" },
  { name: "Courtney Henry", title: "Designer", email: "courtney.henry@example.com", role: "Admin" },
  { name: "Tom Cook", title: "Director of Product", email: "tom.cook@example.com", role: "Member" },
  { name: "Whitney Francis", title: "Copywriter", email: "whitney.francis@example.com", role: "Admin" },
  { name: "Leonard Krasner", title: "Senior Designer", email: "leonard.krasner@example.com", role: "Owner" },
  { name: "Floyd Miles", title: "Principal Designer", email: "floyd.miles@example.com", role: "Member" },
  { name: "Robert Fox", title: "UX Researcher", email: "robert.fox@example.com", role: "Member" },
  { name: "Albert Flores", title: "Manager", email: "albert.flores@example.com", role: "Admin" },
  { name: "Lindsay Walton", title: "Front-end Developer", email: "lindsay.walton@example.com", role: "Member" },
  { name: "Courtney Henry", title: "Designer", email: "courtney.henry@example.com", role: "Admin" },
  { name: "Tom Cook", title: "Director of Product", email: "tom.cook@example.com", role: "Member" },
  { name: "Whitney Francis", title: "Copywriter", email: "whitney.francis@example.com", role: "Admin" },
  { name: "Leonard Krasner", title: "Senior Designer", email: "leonard.krasner@example.com", role: "Owner" },
  { name: "Floyd Miles", title: "Principal Designer", email: "floyd.miles@example.com", role: "Member" },
  { name: "Robert Fox", title: "UX Researcher", email: "robert.fox@example.com", role: "Member" },
  { name: "Albert Flores", title: "Manager", email: "albert.flores@example.com", role: "Admin" },
  { name: "Lindsay Walton", title: "Front-end Developer", email: "lindsay.walton@example.com", role: "Member" },
  { name: "Courtney Henry", title: "Designer", email: "courtney.henry@example.com", role: "Admin" },
  { name: "Tom Cook", title: "Director of Product", email: "tom.cook@example.com", role: "Member" },
  { name: "Whitney Francis", title: "Copywriter", email: "whitney.francis@example.com", role: "Admin" },
  { name: "Leonard Krasner", title: "Senior Designer", email: "leonard.krasner@example.com", role: "Owner" },
  { name: "Floyd Miles", title: "Principal Designer", email: "floyd.miles@example.com", role: "Member" },
  { name: "Robert Fox", title: "UX Researcher", email: "robert.fox@example.com", role: "Member" },
  { name: "Albert Flores", title: "Manager", email: "albert.flores@example.com", role: "Admin" },
];

const totalPages = computed(() => Math.ceil(allUsers.length / perPage));

const paginatedUsers = computed(() => {
  const start = (currentPage.value - 1) * perPage;
  return allUsers.slice(start, start + perPage);
});

const startIndex = computed(() => (currentPage.value - 1) * perPage);
const endIndex = computed(() =>
  Math.min(currentPage.value * perPage, allUsers.length)
);

// Pagination dynamique (max 5 pages visibles)
const visiblePages = computed(() => {
  const pages = [];
  let start = Math.max(1, currentPage.value - 2);
  let end = Math.min(totalPages.value, start + 4);
  if (end - start < 4) start = Math.max(1, end - 4);
  for (let i = start; i <= end; i++) pages.push(i);
  return pages;
});

function goToPage(page) {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
}
</script>
