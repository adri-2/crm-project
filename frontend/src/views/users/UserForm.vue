<template>
  <div class="min-h-screen bg-white flex items-start justify-center py-10 px-4">
    <div
      class="bg-white p-8 sm:p-10 shadow-xl rounded-2xl w-full border border-gray-100"
    >
      <div
        class="flex flex-col md:flex-row items-center md:items-end md:space-x-8 mb-10 pb-4 border-b border-gray-100"
      >
        <div
          class="h-28 md:w-36 md:h-36 rounded-full bg-gray-100 flex items-center justify-center overflow-hidden border-4 border-blue-100 shadow-md flex-shrink-0 mb-4 md:mb-0 cursor-pointer group relative"
          @click="triggerFileInput"
        >
          <img
            :src="profileImagePreview || defaultImg"
            class="object-cover w-full h-full group-hover:opacity-75 transition-opacity duration-200"
            onerror="this.onerror=null;this.src='https://via.placeholder.com/150/F0F4F8/6B7280?text=👤';"
          />
          <div
            class="absolute inset-0 flex items-center justify-center   transition-opacity duration-200 text-white text-xs sm:text-sm font-medium rounded-full text-center p-2"
          >
            <!-- Changer la photo -->
          </div>
          <input
            type="file"
            ref="fileInput"
            @change="handleFileChange"
            class="hidden"
            accept="image/*"
          />
        </div>

        <div class="flex-1 w-full text-center md:text-left">
          <input
            type="text"
            class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-xl text-3xl md:text-5xl px-0 pt-6 pb-2 bg-transparent placeholder-gray-400 font-extrabold text-gray-800"
            placeholder="Nom Complet"
          />
          <p class="text-gray-600 flex items-center mt-3 md:mt-4">
            <input
              type="text"
              class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-lg text-lg md:text-2xl px-0 pt-1 pb-1 bg-transparent placeholder-gray-500 font-medium"
              placeholder="Titre du poste"
            />
          </p>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-8 mb-10">
        <div>
          <h3
            class="text-lg font-semibold text-blue-700 border-b border-blue-200 pb-2 mb-6"
          >
            CONTACT PROFESSIONNEL
          </h3>
          <div class="space-y-6">
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2"
                >Adresse e-mail professionnelle</span
              >
              <input
                type="email"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="ex. johndoe@entreprise.com"
              />
            </label>
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2"
                >Téléphone professionnel</span
              >
              <input
                type="tel"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="ex. +123 456 7890"
              />
            </label>
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2"
                >Téléphone portable professionnel</span
              >
              <input
                type="tel"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="ex. +123 456 7890"
              />
            </label>
            <div class="mt-4">
              <span class="font-semibold text-gray-700 block mb-2"
                >Étiquettes</span
              >
              <div class="text-gray-500 text-sm mb-2">
                ex. : Fondateur, Motorisé, Bâtiment B
              </div>
              <input
                type="text"
                class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="Ajouter des étiquettes (séparées par des virgules)"
              />
            </div>
          </div>
        </div>

        <div>
          <h3
            class="text-lg font-semibold text-blue-700 border-b border-blue-200 pb-2 mb-6"
          >
            DÉTAILS DU POSTE
          </h3>
          <div class="space-y-6">
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2"
                >Département</span
              >
              <input
                type="text"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="ex. Ventes"
              />
            </label>
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2">Poste</span>
              <input
                type="text"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="ex. Directeur Commercial"
              />
            </label>
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2"
                >Manager</span
              >
              <input
                type="text"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="Nom du manager"
              />
            </label>
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2">
                Mentor
                <span
                  class="text-blue-500 cursor-pointer text-xs align-top font-normal"
                  >(?)</span
                >
              </span>
              <input
                type="text"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="Nom du mentor"
              />
            </label>
          </div>
        </div>
      </div>

      <div class="border-b border-gray-200 mb-8">
        <nav class="flex space-x-8 text-base font-medium">
          <a
            href="#"
            :class="[
              'px-3 py-3 border-b-2 transition-all duration-200',
              activeTab === 'cv'
                ? 'border-blue-600 text-blue-700 font-bold'
                : 'border-transparent text-gray-600 hover:border-blue-500 hover:text-blue-600',
            ]"
            @click.prevent="activeTab = 'cv'"
          >
            CV
          </a>
          <a
            href="#"
            :class="[
              'px-3 py-3 border-b-2 transition-all duration-200',
              activeTab === 'private'
                ? 'border-blue-600 text-blue-700 font-bold'
                : 'border-transparent text-gray-600 hover:border-blue-500 hover:text-blue-600',
            ]"
            @click.prevent="activeTab = 'private'"
          >
            Informations privées
          </a>
          <a
            href="#"
            :class="[
              'px-3 py-3 border-b-2 transition-all duration-200',
              activeTab === 'pay'
                ? 'border-blue-600 text-blue-700 font-bold'
                : 'border-transparent text-gray-600 hover:border-blue-500 hover:text-blue-600',
            ]"
            @click.prevent="activeTab = 'pay'"
          >
            Paie
          </a>
        </nav>
      </div>

      <div
        v-if="activeTab === 'private'"
        class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-8 mb-10"
      >
        <div>
          <h3
            class="text-lg font-semibold text-gray-700 border-b border-gray-200 pb-2 mb-6"
          >
            COORDONNÉES PRIVÉES
          </h3>
          <div class="space-y-6">
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2">
                Adresse personnelle
                <span
                  class="text-blue-500 cursor-pointer text-xs align-top font-normal"
                  >(?)</span
                >
              </span>
              <input
                type="text"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="Adresse complète (rue, ville, code postal, pays)"
              />
            </label>
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2"
                >Numéro de téléphone privé</span
              >
              <input
                type="tel"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="ex. +987 654 3210"
              />
            </label>
          </div>
        </div>
        <div>
          <h3
            class="text-lg font-semibold text-gray-700 border-b border-gray-200 pb-2 mb-6"
          >
            ÉDUCATION
          </h3>
          <div class="space-y-6">
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2">
                Niveau scolaire
                <span
                  class="text-blue-500 cursor-pointer text-xs align-top font-normal"
                  >(?)</span
                >
              </span>
              <input
                type="text"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="ex. Master, Licence"
              />
            </label>
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2">
                Champ d'étude
                <span
                  class="text-blue-500 cursor-pointer text-xs align-top font-normal"
                  >(?)</span
                >
              </span>
              <input
                type="text"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="ex. Informatique, Marketing"
              />
            </label>
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2">
                Établissement scolaire
                <span
                  class="text-blue-500 cursor-pointer text-xs align-top font-normal"
                  >(?)</span
                >
              </span>
              <input
                type="text"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="Nom de l'école/université"
              />
            </label>
          </div>
        </div>
      </div>

      <div
        v-if="activeTab === 'cv'"
        class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-8 mb-10"
      >
        <div>
          <h3
            class="text-lg font-semibold text-gray-700 border-b border-gray-200 pb-2 mb-6"
          >
            CV
          </h3>
          <div class="space-y-6">
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2">
                Fichier CV
                <span
                  class="text-blue-500 cursor-pointer text-xs align-top font-normal"
                  >(?)</span
                >
              </span>
              <input
                type="file"
                class="mt-1 block w-full text-sm text-gray-500
                file:mr-4 file:py-2 file:px-4
                file:rounded-md file:border-0
                file:text-sm file:font-semibold
                file:bg-blue-50 file:text-blue-700
                hover:file:bg-blue-100"
              />
            </label>
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2"
                >Compétences</span
              >
              <input
                type="text"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="ex. JavaScript, Gestion de projet (séparées par des virgules)"
              />
            </label>
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2">
                Certifications
                <span
                  class="text-blue-500 cursor-pointer text-xs align-top font-normal"
                  >(?)</span
                >
              </span>
              <input
                type="text"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="ex. PMP, AWS Certified"
              />
            </label>
          </div>
        </div>
      </div>

      <div
        v-if="activeTab === 'pay'"
        class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-8 mb-10"
      >
        <div>
          <h3
            class="text-lg font-semibold text-gray-700 border-b border-gray-200 pb-2 mb-6"
          >
            PAIE
          </h3>
          <div class="space-y-6">
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2"
                >Salaire brut (annuel)</span
              >
              <input
                type="number"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="ex. 50000"
              />
            </label>
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2"
                >Bonus (annuel)</span
              >
              <input
                type="number"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="ex. 5000"
              />
            </label>
          </div>
        </div>
        <div>
          <h3
            class="text-lg font-semibold text-gray-700 border-b border-gray-200 pb-2 mb-6"
          >
            INFORMATIONS BANCAIRES
          </h3>
          <div class="space-y-6">
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2">IBAN</span>
              <input
                type="text"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="Numéro IBAN"
              />
            </label>
            <label class="block">
              <span class="font-semibold text-gray-700 block mb-2"
                >BIC/SWIFT</span
              >
              <input
                type="text"
                class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full bg-transparent placeholder-gray-500 pb-1 px-0"
                placeholder="Code BIC/SWIFT"
              />
            </label>
          </div>
        </div>
      </div>

      <div
        class="mt-10 pt-6 border-t border-gray-100 flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4 justify-end"
      >
        <button
          class="bg-gray-200 text-gray-700 font-medium px-8 py-3 rounded-lg hover:bg-gray-300 transition-colors duration-200 ease-in-out shadow-md hover:shadow-lg"
        >
          Annuler
        </button>
        <button
          class="bg-blue-600 text-white font-medium px-8 py-3 rounded-lg hover:bg-blue-700 transition-colors duration-200 ease-in-out shadow-md hover:shadow-lg"
        >
          Enregistrer
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const activeTab = ref('cv'); // Onglet affiché par défaut
const defaultImg = ref('../../assets/placeholder.png')

// Référence pour le champ de saisie de fichier
const fileInput = ref(null);
// Référence pour l'aperçu de l'image de profil
const profileImagePreview = ref(null);

// Fonction pour déclencher le clic sur le champ de saisie de fichier caché
const triggerFileInput = () => {
  fileInput.value.click();
};

// Fonction pour gérer le changement de fichier
const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    // Créer une URL pour l'aperçu de l'image
    profileImagePreview.value = URL.createObjectURL(file);
    // Ici, vous pouvez également appeler une fonction pour téléverser le fichier
    // uploadProfileImage(file);
  }
};

// Note: navClass n'est pas utilisée dans ce template, mais est maintenue.
function navClass(path) {
  return [
    'transition-all duration-200',
    'block rounded-lg px-4 py-2 text-base font-semibold tracking-wide',
    route.path === '/user/list'
      ? 'bg-gradient-to-r from-blue-500 to-indigo-500 text-white shadow-lg scale-105'
      : 'text-blue-700 hover:bg-indigo-700 hover:text-white',
  ];
}
</script>
