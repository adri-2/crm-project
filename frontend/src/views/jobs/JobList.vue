<template>
  <div class="p-6 bg-white  drop-shadow rounded-lg shadow-2xl  min-h-[500px]">
    <div class="flex justify-between items-center mb-4">
      <div>
        <h2 class="text-xl font-semibold text-gray-800">Jobs</h2>
        <p class="text-sm text-gray-500">
          A list of all job offers including title, company, location, and type.
        </p>
      </div>

      <RouterLink
        to="/job/new"
        class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg text-sm"
      >
        Nouveau
      </RouterLink>
    </div>

    <div class="overflow-x-auto ">
      <table class="min-w-full text-sm text-left text-gray-700 bg-white">
        <thead class="text-xs uppercase text-gray-500 border-b">
          <tr>
            <th class="px-4 py-3">Title</th>
            <th class="px-4 py-3">Company</th>
            <th class="px-4 py-3">Location</th>
            <th class="px-4 py-3">Type</th>
            <th class="px-4 py-3"></th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="job in paginatedJobs"
            :key="job.id"
            class="border-b hover:bg-gray-50"
          >
            <td class="px-4 py-3 font-medium text-gray-900">{{ job.title }}</td>
            <td class="px-4 py-3 text-indigo-600">{{ job.company }}</td>
            <td class="px-4 py-3">{{ job.location }}</td>
            <td class="px-4 py-3">{{ job.type }}</td>
            <td
              class="px-4 py-3 text-indigo-600 font-medium cursor-pointer hover:underline"
            >
              Edit
            </td>
          </tr>
        </tbody>
      </table>
      <!-- Pagination Controls -->
      <div class="mt-6 flex justify-between items-center">
        <p class="text-sm text-gray-700">
          Showing
          <span class="font-medium">{{ startIndex + 1 }}</span>
          to
          <span class="font-medium">{{ endIndex }}</span>
          of
          <span class="font-medium">{{ jobs.length }}</span>
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
import { RouterLink } from 'vue-router';
import { ref, computed,watch    } from 'vue';

const perPage = 10; // Number of items per page
const currentPage = ref(1); // Current page number

const jobs = ref([
  {
    id: 1,
    title: "Frontend Developer",
    company: "TechCorp",
    location: "Remote",
    type: "Full-time",
  },
  {
    id: 2,
    title: "UI/UX Designer",
    company: "Creative Inc.",
    location: "Paris, France",
    type: "Part-time",
  },
  {
    id: 3,
    title: "Backend Engineer",
    company: "DevSolutions",
    location: "Berlin, Germany",
    type: "Full-time",
  },
  {
    id: 4,
    title: "Marketing Specialist",
    company: "MarketSmart",
    location: "Remote",
    type: "Freelance",
  },
  {
    id: 5,
    title: "Data Analyst",
    company: "Insights Co.",
    location: "Dakar, Senegal",
    type: "Full-time",
  },
]);

const totalPages = computed(()=> Math.ceil(jobs.value.length / perPage));
const paginatedJobs = computed(() => {
  const start = (currentPage.value - 1) * perPage;
  return jobs.value.slice(start, start + perPage);
});

const startIndex = computed(() => (currentPage.value - 1) * perPage);
const endIndex = computed(() =>
  Math.min(currentPage.value * perPage, jobs.value.length)
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

watch(jobs, () => {
  if (currentPage.value > totalPages.value) {
    currentPage.value = 1;
  }
});
</script>
