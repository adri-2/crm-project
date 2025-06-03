<template>
  <div class="p-6 bg-white rounded-lg shadow">
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
        Add Job
      </RouterLink>
    </div>

    <div class="overflow-x-auto">
      <table class="min-w-full text-sm text-left text-gray-700">
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
            v-for="job in jobs"
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
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';

const jobs = [
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
];
</script>
