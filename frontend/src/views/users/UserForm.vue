<template>
  <div class="bg-white p-6 shadow rounded-lg">
    <!-- En-tête avec nom et photo -->
    <div class="flex items-start space-x-6 mb-6">
      <div
        class="w-34 h-34 rounded bg-gray-100 flex items-center justify-center text-gray-400 text-2xl"
      >
        <img src="../../../public/placeholder phote.png" alt="" srcset="" />
      </div>
      <div class="flex-1">
        <!-- name user-->

        <input
          type="text"
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-[500px] h-[100px] text-4xl px-4 pt-10"
          placeholder="Nom de l'employé"
        />
        <!-- poste -->

        <p class="text-gray-500 flex items-center space-x-1">
          <span class="text-purple-500">💼</span>
          <input
            type="text"
            class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-[470px] text-2xl px-4 pt-1"
            placeholder="Titre du poste"
          />
        </p>
      </div>
    </div>

    <!-- Coordonnées -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
      <div>
        <p>
          <strong>Adresse e-mail professionnelle</strong><br /><span
            class="text-gray-500"
          >
            <input
              type="text"
              class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
              placeholder="ex. johndoe@example.com"
          /></span>
        </p>
        <p class="mt-2"><strong>Téléphone professionnel</strong></p>
        <input
          type="text"
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
        />
        <p class="mt-2"><strong>Téléphone portable professionnel</strong></p>
        <input
          type="text"
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
        />
        <p class="mt-2">
          <strong>Étiquettes</strong><br /><span class="text-gray-500"
            >ex. : Fondateur, Motorisé, Bâtiment B</span
          >
        </p>
      </div>
      <div>
        <p><strong>Département</strong></p>
        <input
          type="text"
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
        />
        <p class="mt-2">
          <strong>Poste</strong><br /><span class="text-gray-500">
            <input
              type="text"
              class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
              placeholder="ex. Directeur Commercial"
          /></span>
        </p>
        <p class="mt-2">
          <strong>Manager</strong>
          <input
            type="text"
            class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
          />
        </p>

        <p class="mt-2">
          <strong>Mentor</strong>
          <span class="text-blue-500 cursor-pointer">?</span>
          <input
            type="text"
            class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80 "
          />
        </p>
      </div>
    </div>

    <!-- Onglets -->
    <div class="border-b border-gray-200 mb-4">
      <nav class="flex space-x-4 text-sm font-medium">
        <a
          href="#"
          class="px-3 py-2 border-b-2 border-transparent hover:border-purple-500 hover:text-purple-600"
          >CV</a
        >
        <!-- <a
          href="#"
          class="px-3 py-2 border-b-2 border-transparent hover:border-purple-500 hover:text-purple-600"
          >Informations professionnelles</a
        > -->
        <a
          href="#"
          class="px-3 py-2 border-b-2 border-transparent hover:border-purple-500 text-purple-600"
          >Informations privées</a
        >
        <a
          href="#"
          class="px-3 py-2 border-b-2 border-transparent hover:border-purple-500 hover:text-purple-600"
          >Paie</a
        >
        <!-- <a
          href="#"
          class="px-3 py-2 border-b-2 border-purple-500 text-purple-600"
          >Paramètres</a
        > -->
      </nav>
    </div>

    <!-- Bloc paramètres -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div>
        <h3
          class="text-sm font-semibold text-gray-600  border-gray-200 border-b pb-2 mb-4"
        >
          COORDONNEES PRIVEES
        </h3>
        <p>
          <strong>Adresse personnelle</strong>
          <span class="text-blue-500 cursor-pointer">?</span>
          <input
            type="text"
            class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
          />
        </p>
        <p class="mt-2">
          <strong>Numéro de téléphone privé</strong>
          <input
            type="text"
            class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
          />
        </p>
      </div>
      <div>
        <h3
          class="text-sm font-semibold text-gray-600  border-gray-200 border-b pb-2 mb-4"
        >
          Éducation
        </h3>
        <p>
          <strong>Niveau du certificat</strong>
          <span class="text-blue-500 cursor-pointer"> ?</span>
          <input
            type="text"
            class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
          />
        </p>
        <p class="mt-2">
          <strong>Champ d'étude</strong>
          <span class="text-blue-500 cursor-pointer">?</span>
          <input
            type="text"
            class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
          />
        </p>
        <p class="mt-2">
          <strong>Établissement scolaire</strong>
          <span class="text-blue-500 cursor-pointer">?</span>
          <input
            type="text"
            class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
          />
        </p>
      </div>
    </div>
    <!-- Footer -->
    <div class="mt-6 block space-x-2">
      <button
        class="bg-green-700 text-white px-4 py-2 rounded hover:bg-green-900"
      >
        Save
      </button>
      <button
        class="border bg-red-500 hover:bg-red-700 border-gray-300 text-gray-700 px-3 py-2 rounded"
      >
        Annuler
      </button>
      <!-- <button class="border border-gray-300 text-gray-700 px-3 py-2 rounded">
        Activité
      </button> -->
    </div>
  </div>
</template>

<script setup>
// Pas de logique encore, tout est statique ici
</script>
