<template>
  <div class="p-6 bg-white rounded-lg shadow">
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

    <div class="overflow-x-auto ">
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
            v-for="user in users"
            :key="user.email"
            class="border-b hover:bg-gray-50"
          >
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
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
const users = [
  {
    name: "Lindsay Walton",
    title: "Front-end Developer",
    email: "lindsay.walton@example.com",
    role: "Member",
  },
  {
    name: "Courtney Henry",
    title: "Designer",
    email: "courtney.henry@example.com",
    role: "Admin",
  },
  {
    name: "Tom Cook",
    title: "Director of Product",
    email: "tom.cook@example.com",
    role: "Member",
  },
  {
    name: "Whitney Francis",
    title: "Copywriter",
    email: "whitney.francis@example.com",
    role: "Admin",
  },
  {
    name: "Leonard Krasner",
    title: "Senior Designer",
    email: "leonard.krasner@example.com",
    role: "Owner",
  },
  {
    name: "Floyd Miles",
    title: "Principal Designer",
    email: "floyd.miles@example.com",
    role: "Member",
  },
]
</script>
