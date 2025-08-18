import { acceptHMRUpdate, defineStore } from "pinia";
import { ref } from "vue";
import Cookies from "js-cookie";

export const useAuth = defineStore(
  "auth",
  () => {
    const user = ref(null);

    // Charger l'utilisateur depuis le cookie au démarrage
    const loadUser = () => {
      const userData = Cookies.get("auth");
      if (userData) {
        user.value = JSON.parse(userData);
      }
    };

    const setUser = (userData) => {
      user.value = userData;
      Cookies.set("auth", JSON.stringify(userData), { expires: 1, secure: true });
    };

    const getUser = () => {
      return user.value;
    };

    const clearUser = () => {
      user.value = null;
      Cookies.remove("auth");
    };

    // Charger l'utilisateur dès l'initialisation
    loadUser();

    return {
      user,
      setUser,
      getUser,
      clearUser,
    };
  }
);

// Support du Hot Module Replacement (HMR)
if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useAuth, import.meta.hot));
}
