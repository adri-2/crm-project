import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import UserList from "@/views/users/UserList.vue";
import UserForm from "@/views/users/UserForm.vue";
import JobForm from "@/views/jobs/JobForm.vue";
import JobList from "@/views/jobs/JobList.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/user/list",
      name: "list-user",
      component: UserList,
    },
    {
      path: "/user/new",
      name: "user-new",
      component: UserForm,
    },
    {
      path: "/job/new",
      name: "job-new",
      component: JobForm,
    },
    {
      path: "/job/list",
      name: "job-list",
      component: JobList,
    },
  ],
});

export default router;
