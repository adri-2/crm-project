<template>
  <!-- <div class="min-h-screen bg-gray-50 flex items-center justify-center py-10"> -->
  <div class="bg-white p-8 shadow-xl rounded-2xl w-full ">
    <!-- En-tête avec nom et photo -->
    <div
      class="flex flex-col md:flex-row items-start md:space-x-8 mb-8 space-y-4 md:space-y-0 "
    >
      <div
        class="w-24 h-24  md:w-32 md:h-32 rounded-full bg-gray-100 flex items-center justify-center overflow-hidden border-4 border-blue-100 shadow mx-auto md:mx-0"
      >
        <img
          src="../../../public/placeholder phote.png"
          alt=""
          class="object-cover w-full h-full"
        />
      </div>
      <div class="flex-1 w-full ml-5">
        <input
          type="text"
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-xl h-16 md:h-20 text-2xl md:text-4xl px-4 pt-6 md:pt-10 bg-transparent placeholder-gray-400"
          placeholder="Nom de l'employé"
        />
        <p class="text-gray-500 flex items-center mt-2">
          <!-- <span class="text-purple-500 mr-2">💼</span> -->
          <input
            type="text"
            class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-lg text-lg md:text-2xl px-4 pt-1 bg-transparent placeholder-gray-400"
            placeholder="Titre du poste"
          />
        </p>
      </div>
    </div>

    <!-- Coordonnées -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
      <div>
        <label class="block mb-4">
          <span class="font-semibold">Adresse e-mail professionnelle</span>
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent placeholder-gray-400"
            placeholder="ex. johndoe@example.com"
          />
        </label>
        <label class="block mb-4">
          <span class="font-semibold">Téléphone professionnel</span>
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </label>
        <label class="block mb-4">
          <span class="font-semibold">Téléphone portable professionnel</span>
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </label>
        <div class="mt-4">
          <span class="font-semibold">Étiquettes</span>
          <div class="text-gray-400 text-sm mb-1">
            ex. : Fondateur, Motorisé, Bâtiment B
          </div>
          <input
            type="text"
            class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </div>
      </div>
      <div>
        <label class="block mb-4">
          <span class="font-semibold">Département</span>
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </label>
        <label class="block mb-4">
          <span class="font-semibold">Poste</span>
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
            placeholder="ex. Directeur Commercial"
          />
        </label>
        <label class="block mb-4">
          <span class="font-semibold">Manager</span>
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </label>
        <label class="block mb-4">
          <span class="font-semibold"
            >Mentor <span class="text-blue-500 cursor-pointer">?</span></span
          >
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </label>
      </div>
    </div>

    <!-- Onglets -->
    <div class="border-b border-gray-200 mb-6">
      <nav class="flex space-x-8 text-base font-medium">
        <a
          href="#"
          :class="[
        'px-3 py-2 border-b-2 transition',
        activeTab === 'cv'
          ? 'border-purple-500 text-purple-600'
          : 'border-transparent hover:border-purple-500 hover:text-purple-600'
        ]"
          @click.prevent="activeTab = 'cv'"
          >CV</a
        >
        <a
          href="#"
          :class="[
        'px-3 py-2 border-b-2 transition',
        activeTab === 'private'
          ? 'border-purple-500 text-purple-600'
          : 'border-transparent hover:border-purple-500 hover:text-purple-600'
        ]"
          @click.prevent="activeTab = 'private'"
          >Informations privées</a
        >
        <a
          href="#"
          :class="[
        'px-3 py-2 border-b-2 transition',
        activeTab === 'pay'
          ? 'border-purple-500 text-purple-600'
          : 'border-transparent hover:border-purple-500 hover:text-purple-600'
        ]"
          @click.prevent="activeTab = 'pay'"
          >Paie</a
        >
      </nav>
    </div>

    <!-- Bloc paramètres -->
    <div
      v-if="activeTab === 'private'"
      class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8"
    >
      <div>
        <h3
          class="text-base font-semibold text-gray-600 border-b border-gray-200 pb-2 mb-4"
        >
          COORDONNEES PRIVEES
        </h3>
        <label class="block mb-4">
          <span class="font-semibold"
            >Adresse personnelle
            <span class="text-blue-500 cursor-pointer">?</span></span
          >
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </label>
        <label class="block mb-4">
          <span class="font-semibold">Numéro de téléphone privé</span>
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </label>
      </div>
      <div>
        <h3
          class="text-base font-semibold text-gray-600 border-b border-gray-200 pb-2 mb-4"
        >
          Éducation
        </h3>
        <label class="block mb-4">
          <span class="font-semibold"
            >Niveau scolaire
            <span class="text-blue-500 cursor-pointer">?</span></span
          >
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </label>
        <label class="block mb-4">
          <span class="font-semibold"
            >Champ d'étude
            <span class="text-blue-500 cursor-pointer">?</span></span
          >
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </label>
        <label class="block mb-4">
          <span class="font-semibold"
            >Établissement scolaire
            <span class="text-blue-500 cursor-pointer">?</span></span
          >
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </label>
      </div>
    </div>

    <div
      v-if="activeTab === 'cv'"
      class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8"
    >
      <div>
        <h3
          class="text-base font-semibold text-gray-600 border-b border-gray-200 pb-2 mb-4"
        >
          CV
        </h3>
        <label class="block mb-4">
          <span class="font-semibold"
            >Cv <span class="text-blue-500 cursor-pointer">?</span></span
          >
          <input
            type="file"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </label>
        <label class="block mb-4">
          <span class="font-semibold">Compétences</span>
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </label>
        <label class="block mb-4">
          <span class="font-semibold"
            >Certification
            <span class="text-blue-500 cursor-pointer">?</span></span
          >
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </label>
      </div>
    </div>

    <div
      v-if="activeTab === 'pay'"
      class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8"
    >
      <div>
        <h3
          class="text-base font-semibold text-gray-600 border-b border-gray-200 pb-2 mb-4"
        >
          Paie
        </h3>
        <label class="block mb-4">
          <span class="font-semibold">Salaire brut</span>
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </label>
        <label class="block mb-4">
          <span class="font-semibold">Bonus</span>
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </label>
      </div>
      <div>
        <h3
          class="text-base font-semibold text-gray-600 border-b border-gray-200 pb-2 mb-4"
        >
          Informations bancaires
        </h3>
        <label class="block mb-4">
          <span class="font-semibold">IBAN</span>
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </label>
        <label class="block mb-4">
          <span class="font-semibold">BIC</span>
          <input
            type="text"
            class="mt-1 border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-md bg-transparent"
          />
        </label>
      </div>
    </div>

    <!-- Footer -->
    <div class="mt-8 flex space-x-4 justify-end">
      <button
        class="bg-green-700 text-white px-6 py-2 rounded-lg hover:bg-green-900 transition"
      >
        Save
      </button>
      <button
        class="bg-red-500 hover:bg-red-700 text-white px-6 py-2 rounded-lg transition"
      >
        Annuler
      </button>
    </div>
  </div>
  <!-- </div> -->
</template>

<script setup>
import { ref } from 'vue'

const activeTab = ref('cv') // Onglet affiché par défaut
</script>
