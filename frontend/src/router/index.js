import { createRouter, createWebHistory } from "vue-router";
// import HomeView from "../views/HomeView.vue";
import UserList from "@/views/users/UserList.vue";
import UserForm from "@/views/users/UserForm.vue";
import JobForm from "@/views/jobs/JobForm.vue";
import JobList from "@/views/jobs/JobList.vue";
import DashBoard from "@/views/DashBoard.vue";
import JobOfferForm from "@/views/recruitment/JobOfferForm.vue";
import JobOfferList from "@/views/recruitment/JobOfferList.vue";
import CandidateList from "@/views/recruitment/CandidateList.vue";
import CandidatForm from "@/views/recruitment/CandidatForm.vue";
import LoginView from "@/views/LoginView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "login",
      component: () => import("../views/LoginView.vue"),
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
    {
      path: "/dashboard",
      name: "dashboard",
      component: DashBoard,
    },
    {
      path: "/recruitment/offers/new",
      name: "recruitment-offers-new",
      component: JobOfferForm,
    },
    {
      path: "/recruitment/offers/list",
      name: "recruitment-offers-list",
      component: JobOfferList,
    },
    {
      path: "/recruitment/candidates",
      name: "recruitment-candidates",
      component: CandidateList,
    },
    {
      path: "/recruitment/candidates/new",
      name: "recruitment-candidates-new",
      component: CandidatForm,
    },
    //

    //  {
    //   path: "/stagiaire/list",
    //   name: "stagiaire-list",
    //   component: CandidatForm,
    // },
    //  {
    //   path: "/stagiaire/new",
    //   name: "stagiaire-new",
    //   component: CandidatForm,
    // },
  ],
});

export default router;
