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
import AboutView from "@/views/AboutView.vue";


export default [
    {
      path: "/",
      name: "login",
      component: LoginView,
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: AboutView,
    },
    {
      path: "/dashboard",
      name: "dashboard",
      component: DashBoard,
    },
    {
        path: "/user",
        name: "user",
        children: [
          {
            path: "list",
            name: "list-user",
            component: UserList,
          },
          {
            path: "new",
            name: "user-new",
            component: UserForm,
          },
        ],
    },
    {
      path: "/recruitment",
      name: "recruitment",
      children: [
        {
          path: "offers",
          name: "recruitment-offers",
          children: [
            {
              path: "list",
              name: "recruitment-offers-list",
              component: JobOfferList,
            },
            {
              path: "new",
              name: "recruitment-offers-new",
              component: JobOfferForm,
            },
          ],
        },
        {
          path: "candidates",
          name: "recruitment-candidates",
          children: [
            {
              path: "list",
              name: "recruitment-candidates-list",
              component: CandidateList,
            },
            {
              path: "new",
              name: "recruitment-candidates-new",
              component: CandidatForm,
            },
          ],
        },
      ],
    },
    {
      path: "/job",
      name: "job",
      children: [
        {
          path: "list",
          name: "list-job",
          component: JobList,
        },
        {
          path: "new",
          name: "job-new",
          component: JobForm,
        },
      ],
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
]