<template>
  <div class="h-full   flex items-center justify-center bg-gray-100 p-4 sm:p-6">
    <div
      class="w-full max-w-md bg-white rounded-lg shadow-xl drop-shadow p-8 space-y-6 border border-gray-200"
    >
      <div class="text-center">
        <h2 class="text-3xl font-extrabold text-gray-900 mb-2">
          Connectez-vous à votre compte
        </h2>
        <p class="text-sm text-gray-600">
          Entrez vos identifiants pour accéder à votre tableau de bord.
        </p>
      </div>

      <form @submit.prevent="handleLogin" class="space-y-6">
        <div>
          <label
            for="email"
            class="block text-sm font-medium text-gray-700 mb-1"
            >Adresse e-mail</label
          >
          <input
            id="email"
            name="email"
            type="email"
            autocomplete="email"
            required
            v-model="email"
            class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            placeholder="votre.email@example.com"
          />
        </div>

        <div>
          <label
            for="password"
            class="block text-sm font-medium text-gray-700 mb-1"
            >Mot de passe</label
          >
          <input
            id="password"
            name="password"
            type="password"
            autocomplete="current-password"
            required
            v-model="password"
            class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            placeholder="********"
          />
        </div>

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <input
              id="remember-me"
              name="remember-me"
              type="checkbox"
              v-model="rememberMe"
              class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
            />
            <label for="remember-me" class="ml-2 block text-sm text-gray-900">
              Se souvenir de moi
            </label>
          </div>

          <div class="text-sm">
            <a
              href="#"
              class="font-medium text-indigo-600 hover:text-indigo-500"
            >
              Mot de passe oublié ?
            </a>
          </div>
        </div>

        <div v-if="errorMessage" class="text-red-600 text-sm text-center">
          {{ errorMessage }}
        </div>

        <div>
          <button
            type="submit"
            :disabled="loading"
            class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-colors duration-200 ease-in-out"
            :class="{ 'opacity-50 cursor-not-allowed': loading }"
          >
            <span v-if="loading" class="flex items-center">
              <svg
                class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle
                  class="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  stroke-width="4"
                ></circle>
                <path
                  class="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                ></path>
              </svg>
              Connexion en cours...
            </span>
            <span v-else>Se connecter</span>
          </button>
        </div>
      </form>

      <div class="text-center text-sm text-gray-600">
        Pas encore de compte ?
        <a href="#" class="font-medium text-indigo-600 hover:text-indigo-500">
          Créez-en un
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter();

const email = ref('');
const password = ref('');
const rememberMe = ref(false);
const loading = ref(false);
const errorMessage = ref('');

const handleLogin = async () => {
  loading.value = true;
  errorMessage.value = '';

  // Simulation d'un appel API de connexion
  try {
    // Remplacez ceci par votre véritable appel API (ex: fetch('/api/login', { method: 'POST', body: JSON.stringify({ email: email.value, password: password.value }) }))
    await new Promise((resolve, reject) => {
      setTimeout(() => {
        if (email.value === 'admin@gmail.com' && password.value === 'admin') {
          resolve('/dashboard'); // Connexion réussie
        } else {
          reject(new Error('Identifiants invalides.')); // Connexion échouée
        }
      }, 1500); // Simule un délai réseau
    });

    // Si la connexion réussit
    // alert('Connexion réussie ! Redirection vers le tableau de bord...');
    // Ici, vous redirigeriez l'utilisateur, par exemple avec vue-router:
    router.push('/dashboard');
  } catch (error) {
    errorMessage.value = error.message;
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
/* Aucun style spécifique n'est nécessaire ici car Tailwind CSS gère la plupart du design. */
/* Assurez-vous que Tailwind CSS est correctement configuré dans votre projet Vue. */
</style>
