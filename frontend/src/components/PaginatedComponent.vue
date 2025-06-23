<template>
  <div
    class="rounded-lg bg-white shadow-md p-6 min-h-[350px] flex flex-col justify-between"
  >
    <!-- Slot : contenu de la liste -->
    <div class="grow">
      <slot
        :items="paginatedItems"
        :currentPage="currentPage"
        :totalPages="totalPages"
        :goToPage="goToPage"
      />
    </div>

    <!-- Pagination -->
    <div class="mt-6 flex justify-between items-center">
      <p class="text-sm text-gray-700">
        Affichage
        <span class="font-medium">{{ startIndex + 1 }}</span>
        à
        <span class="font-medium">{{ endIndex }}</span>
        sur
        <span class="font-medium">{{ items.length }}</span>
        résultats
      </p>
      <div class="flex gap-1">
        <button
          @click="goToPage(currentPage - 1)"
          :disabled="currentPage === 1"
          class="px-3 py-1 text-sm rounded border border-gray-300 text-gray-700 hover:bg-gray-50 disabled:opacity-50"
        >
          Précédent
        </button>
        <button
          v-for="page in totalPages"
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
          Suivant
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, toRefs, watchEffect } from 'vue';

const props = defineProps({
  items: {
    type: Array,
    required: true,
  },
  perPage: {
    type: Number,
    default: 8, // Nombre d'éléments par page
  },
});

const { items, perPage } = toRefs(props);
const currentPage = ref(1);

const totalPages = computed(() => Math.ceil(items.value.length / perPage.value));

const paginatedItems = computed(() => {
  const start = (currentPage.value - 1) * perPage.value;
  const end = start + Number(perPage.value); // forcer la conversion
  return items.value.slice(start, end);
});


const startIndex = computed(() => (currentPage.value - 1) * perPage.value);
const endIndex = computed(() => Math.min(currentPage.value * perPage.value, items.value.length));

function goToPage(page) {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
}

// reset page if list changes
watchEffect(
    ()=>{
        if (currentPage.value > totalPages.value){
            currentPage.value = totalPages.value
        }
    }
);
watch(
  () => items.value.length,
  () => {
    currentPage.value = 1;
  }
);
</script>

<!-- 
<template>
  <PaginatedComponent :items="users" :perPage="8">
    <template #default="{ items, currentPage, totalPages, goToPage }">
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
          Add<span class="ml-2"> </span>user
        </RouterLink>
      </div>
      <div
        class="flex flex-col justify-between overflow-x-auto bg-white min-h-[350px]"
      >
        <table class="min-w-full text-sm text-left text-gray-700 scroll-auto">
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
              v-for="user in items"
              :key="user.email"
              class="border-b hover:bg-gray-50"
            >
              <td class="px-4 py-3 font-medium text-gray-900">
                {{ user.name }}
              </td>
              <td class="px-4 py-3 text-indigo-600">
                {{ user.title || '-' }}
              </td>
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
      </div>
    </template>
  </PaginatedComponent>
   </div> 
</template> -->

<!-- <script setup>
import PaginatedComponent from '@/components/PaginatedComponent.vue'
import { RouterLink } from 'vue-router'

const users = [
  { name: 'Alice', title: 'Developer', email: 'a@example.com', role: 'Admin' },
  { name: 'Bob', title: 'Designer', email: 'b@example.com', role: 'Member' },
  { name: 'Carol', title: 'Manager', email: 'c@example.com', role: 'Admin' },
  { name: 'Dan', title: 'QA', email: 'd@example.com', role: 'Member' },
  { name: 'Eva', title: 'Support', email: 'e@example.com', role: 'Member' },
  { name: 'Fred', title: 'Lead', email: 'f@example.com', role: 'Admin' },
  { name: 'George', title: 'Owner', email: 'g@example.com', role: 'Owner' },
    { name: 'Alice', title: 'Developer', email: 'a@example.com', role: 'Admin' },
  { name: 'Bob', title: 'Designer', email: 'b@example.com', role: 'Member' },
  { name: 'Carol', title: 'Manager', email: 'c@example.com', role: 'Admin' },
  { name: 'Dan', title: 'QA', email: 'd@example.com', role: 'Member' },
  { name: 'Eva', title: 'Support', email: 'e@example.com', role: 'Member' },
  { name: 'Fred', title: 'Lead', email: 'f@example.com', role: 'Admin' },
  { name: 'George', title: 'Owner', email: 'g@example.com', role: 'Owner' },
    { name: 'Alice', title: 'Developer', email: 'a@example.com', role: 'Admin' },
  { name: 'Bob', title: 'Designer', email: 'b@example.com', role: 'Member' },
  { name: 'Carol', title: 'Manager', email: 'c@example.com', role: 'Admin' },
  { name: 'Dan', title: 'QA', email: 'd@example.com', role: 'Member' },
  { name: 'Eva', title: 'Support', email: 'e@example.com', role: 'Member' },
  { name: 'Fred', title: 'Lead', email: 'f@example.com', role: 'Admin' },
  { name: 'George', title: 'Owner', email: 'g@example.com', role: 'Owner' },
   { name: 'Alice', title: 'Developer', email: 'a@example.com', role: 'Admin' },
  { name: 'Bob', title: 'Designer', email: 'b@example.com', role: 'Member' },
  { name: 'Carol', title: 'Manager', email: 'c@example.com', role: 'Admin' },
  { name: 'Dan', title: 'QA', email: 'd@example.com', role: 'Member' },
  { name: 'Eva', title: 'Support', email: 'e@example.com', role: 'Member' },
  { name: 'Fred', title: 'Lead', email: 'f@example.com', role: 'Admin' },
  { name: 'George', title: 'Owner', email: 'g@example.com', role: 'Owner' },
]
</script>  -->
