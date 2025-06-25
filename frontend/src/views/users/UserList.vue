<template>
  <div
    class="flex flex-col p-6 bg-white rounded-lg shadow-2xl  drop-shadow min-h-[500px] min-w-[800px]"
  >
    <div class="flex justify-between items-center mb-4 ">
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
        Nouveau
      </RouterLink>
    </div>

    <div class="overflow-y-auto bg-white flex flex-col grow">
      <!-- User Table -->
      <table class="min-w-full text-sm text-left text-gray-700 ">
        <thead class="text-xs uppercase text-gray-500 border-b">
          <tr>
            <th class="px-4 py-3">#</th>
            <th class="px-4 py-3">Name</th>
            <th class="px-4 py-3">Title</th>
            <th class="px-4 py-3">Email</th>
            <th class="px-4 py-3">Role</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="user in paginatedUsers"
            :key="user.email"
            class="border-b hover:bg-gray-50"
          >
            <td class="px-4 py-3">{{ user.id }}</td>
            <td class="px-4 py-3 font-medium text-gray-900">{{ user.name }}</td>
            <td class="px-4 py-3 text-indigo-600">{{ user.title }}</td>
            <td class="px-4 py-3">{{ user.email }}</td>
            <td class="px-4 py-3">{{ user.role }}</td>
            <td
              class="px-4 py-3 text-indigo-600 font-medium cursor-pointer hover:underline"
            >
              Edit
            </td>
          </tr>
        </tbody>
      </table>
      <!-- Pagination Controls -->
      <div class="mt-6 flex justify-between items-center shrink-0">
        <p class="text-sm text-gray-700">
          Showing
          <span class="font-medium">{{ startIndex + 1 }}</span>
          to
          <span class="font-medium">{{ endIndex }}</span>
          of
          <span class="font-medium">{{ users.length }}</span>
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
import { ref, computed, watch } from 'vue';
import { RouterLink } from 'vue-router';

const perPage = 10;
const currentPage = ref(1);

const users = ref([
  { id: '1', name: "Lindsay Walton", title: "Front-end Developer", email: "lindsay.walton@example.com", role: "Member" },
  { id: '2', name: "Courtney Henry", title: "Designer", email: "courtney.henry@example.com", role: "Admin" },
  { id: '3', name: "Tom Cook", title: "Director", email: "tom.cook@example.com", role: "Member" },
  { id: '4', name: "Whitney Francis", title: "Copywriter", email: "whitney.francis@example.com", role: "Member" },
  { id: '5', name: "Leonard Krasner", title: "Senior Designer", email: "leonard.krasner@example.com", role: "Owner" },
  { id: '6', name: "Floyd Miles", title: "Principal Designer", email: "floyd.miles@example.com", role: "Member" },
  { id: '7', name: "Emily Selman", title: "VP, User Experience", email: "emily.selman@example.com", role: "Admin" },
  { id: '8', name: "Kristin Watson", title: "Front-end Developer", email: "kristin.watson@example.com", role: "Member" },
  { id: '9', name: "Jenny Wilson", title: "Product Designer", email: "jenny.wilson@example.com", role: "Member" },
  { id: '10', name: "Cody Fisher", title: "Product Manager", email: "cody.fisher@example.com", role: "Member" },
  { id: '11', name: "Jane Cooper", title: "Marketing Coordinator", email: "jane.cooper@example.com", role: "Member" },
  { id: '12', name: "Wade Warren", title: "Software Engineer", email: "wade.warren@example.com", role: "Member" },
  { id: '13', name: "Lindsay Walton", title: "Front-end Developer", email: "lindsay.walton2@example.com", role: "Member" },
  { id: '14', name: "Courtney Henry", title: "Designer", email: "courtney.henry2@example.com", role: "Admin" },
  { id: '15', name: "Tom Cook", title: "Director", email: "tom.cook2@example.com", role: "Member" },
  { id: '16', name: "Whitney Francis", title: "Copywriter", email: "whitney.francis2@example.com", role: "Member" },
  { id: '17', name: "Leonard Krasner", title: "Senior Designer", email: "leonard.krasner2@example.com", role: "Owner" },
  { id: '18', name: "Floyd Miles", title: "Principal Designer", email: "floyd.miles2@example.com", role: "Member" },
  { id: '19', name: "Emily Selman", title: "VP, User Experience", email: "emily.selman2@example.com", role: "Admin" },
  { id: '20', name: "Kristin Watson", title: "Front-end Developer", email: "kristin.watson2@example.com", role: "Member" },
  { id: '21', name: "Jenny Wilson", title: "Product Designer", email: "jenny.wilson2@example.com", role: "Member" },
  { id: '22', name: "Cody Fisher", title: "Product Manager", email: "cody.fisher2@example.com", role: "Member" },
  { id: '23', name: "Jane Cooper", title: "Marketing Coordinator", email: "jane.cooper2@example.com", role: "Member" },
  { id: '24', name: "Wade Warren", title: "Software Engineer", email: "wade.warren2@example.com", role: "Member" },
  { id: '25', name: "Lindsay Walton", title: "Front-end Developer", email: "lindsay.walton3@example.com", role: "Member" },
  { id: '26', name: "Courtney Henry", title: "Designer", email: "courtney.henry3@example.com", role: "Admin" },
  { id: '27', name: "Tom Cook", title: "Director", email: "tom.cook3@example.com", role: "Member" },
  { id: '28', name: "Whitney Francis", title: "Copywriter", email: "whitney.francis3@example.com", role: "Member" },
  { id: '29', name: "Leonard Krasner", title: "Senior Designer", email: "leonard.krasner3@example.com", role: "Owner" },
  { id: '30', name: "Floyd Miles", title: "Principal Designer", email: "floyd.miles3@example.com", role: "Member" },
  { id: '31', name: "Emily Selman", title: "VP, User Experience", email: "emily.selman3@example.com", role: "Admin" },
  { id: '32', name: "Kristin Watson", title: "Front-end Developer", email: "kristin.watson3@example.com", role: "Member" },
  { id: '33', name: "Jenny Wilson", title: "Product Designer", email: "jenny.wilson3@example.com", role: "Member" },
  { id: '34', name: "Cody Fisher", title: "Product Manager", email: "cody.fisher3@example.com", role: "Member" },
  { id: '35', name: "Jane Cooper", title: "Marketing Coordinator", email: "jane.cooper3@example.com", role: "Member" },
  { id: '36', name: "Wade Warren", title: "Software Engineer", email: "wade.warren3@example.com", role: "Member" },
  { id: '37', name: "Lindsay Walton", title: "Front-end Developer", email: "lindsay.walton4@example.com", role: "Member" },
  { id: '38', name: "Courtney Henry", title: "Designer", email: "courtney.henry4@example.com", role: "Admin" },
  { id: '39', name: "Tom Cook", title: "Director", email: "tom.cook4@example.com", role: "Member" },
  { id: '40', name: "Whitney Francis", title: "Copywriter", email: "whitney.francis4@example.com", role: "Member" },
  { id: '41', name: "Leonard Krasner", title: "Senior Designer", email: "leonard.krasner4@example.com", role: "Owner" },
  { id: '42', name: "Floyd Miles", title: "Principal Designer", email: "floyd.miles4@example.com", role: "Member" },
  // { id: '43', name: "Emily Selman", title: "VP, User Experience", email: "emily.selman4@example.com", role: "Admin" },
  // { id: '44', name: "Kristin Watson", title: "Front-end Developer", email: "kristin.watson4@example.com", role: "Member" },
  // { id: '45', name: "Jenny Wilson", title: "Product Designer", email: "jenny.wilson4@example.com", role: "Member" },
  // { id: '46', name: "Cody Fisher", title: "Product Manager", email: "cody.fisher4@example.com", role: "Member" },
  // { id: '47', name: "Jane Cooper", title: "Marketing Coordinator", email: "jane.cooper4@example.com", role: "Member" },
  // { id: '48', name: "Wade Warren", title: "Software Engineer", email: "wade.warren4@example.com", role: "Member" },
]);

const totalPages = computed(() => Math.ceil(users.value.length / perPage));

const paginatedUsers = computed(() => {
  const start = (currentPage.value - 1) * perPage;
  return users.value.slice(start, start + perPage);
});

const startIndex = computed(() => (currentPage.value - 1) * perPage);
const endIndex = computed(() =>
  Math.min(currentPage.value * perPage, users.value.length)
);

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

watch(users, () => {
  if (currentPage.value > totalPages.value) {
    currentPage.value = 1;
  }
});
</script>
