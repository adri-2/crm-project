<template>
  <div class="bg-white rounded-md shadow p-6">
    <!-- Titre du poste -->
    <div class="mb-4">
      <label class="block text-2xl font-semibold text-gray-700">Poste</label>
      <input
        type="text"
        placeholder=" Titre du poste par ex. Directeur Commercial"
        class="mt-2  border-b border-blue-500 focus:border-blue-700 focus:outline-none  text-3xl text-gray-600 placeholder-gray-400  w-[670px] "
      />
    </div>

    <!-- Tabs -->
    <div class="border-b border-gray-200 mb-6">
      <nav class="-mb-px flex space-x-4">
        <a
          href="#"
          class="text-sm font-medium text-gray-900 border-b-2 border-indigo-600 pb-2"
          >Détails</a
        >
        <a
          href="#"
          class="text-sm font-medium text-gray-500 hover:text-gray-700 pb-2"
          >Résumé</a
        >
      </nav>
    </div>

    <!-- Infos -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-y-4 gap-x-8 text-sm">
      <div>
        <p class="font-medium text-gray-700">Département</p>
        <!-- <p class="text-gray-600">–</p> -->
        <input
          type="text"
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
          placeholder="Departement"
        />
      </div>

      <div>
        <p class="font-medium text-gray-700">
          Cible <span class="text-xs text-blue-500 cursor-help">?</span>
        </p>
        <!-- <p class="text-gray-600">1 nouveaux employés</p> -->
        <input
          type="text"
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
          placeholder="Nombre de nouveaux employés"
        />
      </div>

      <div>
        <p class="font-medium text-gray-700">
          Lieu de travail
          <span class="text-xs text-blue-500 cursor-help">?</span>
        </p>

        <select
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
        >
          <option value="">Sur cite</option>
          <option value="">Hydride</option>
          <option value="">Tele travaille</option>
        </select>
      </div>

      <div>
        <p class="font-medium text-gray-700">
          Chef Departement
          <span class="text-xs text-blue-500 cursor-help">?</span>
        </p>
        <div class="flex items-center space-x-2 mt-1">
          <select
            class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
          >
            <option value="">1</option>
            <option value="">2</option>
            <option value="">3</option>
          </select>
        </div>
      </div>

      <div>
        <p class="font-medium text-gray-700">Secteur d'activité</p>
        <!-- <p class="text-gray-500">
          Par ex. Santé, Services informatiques, Agriculture …
        </p> -->
        <select
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
        >
          <option value="">Santé</option>
          <option value="">Services informatiques</option>
          <option value="">Agriculture</option>
        </select>
      </div>

      <div>
        <p class="font-medium text-gray-700">
          Interviewers <span class="text-xs text-blue-500 cursor-help">?</span>
        </p>
        <select
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
        >
          <option value="">1</option>
          <option value="">2</option>
          <option value="">3</option>
        </select>
      </div>

      <div>
        <p class="font-medium text-gray-700">Type d'emploi</p>
        <select
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
        >
          <option value="">1</option>
          <option value="">2</option>
          <option value="">3</option>
        </select>
      </div>

      <div>
        <p class="font-medium text-gray-700">
          Dates de la mission
          <span class="text-xs text-blue-500 cursor-help">?</span>
        </p>
        <input
          type="date"
          name=""
          id=""
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
        />
      </div>

      <div>
        <p class="font-medium text-gray-700">Compétences attendues</p>
        <select
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-80"
        >
          <option value="">Santé</option>
          <option value="">Services informatiques</option>
          <option value="">Agriculture</option>
        </select>
      </div>

      <div class="flex">
        <!-- <p class="font-medium text-gray-700">Horaires</p> -->
        <p class="font-medium text-gray-700 mr-2">Heure de Debut</p>
        <input
          type="time"
          name=""
          id=""
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-20 mb-4"
        />
        <p class="font-medium text-gray-700 mr-2 ml-4">Heure de Fin</p>
        <input
          type="time"
          name=""
          id=""
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-20 mb-4"
        />
      </div>

      <div class="flex ">
        <p class="font-medium text-gray-700 mr-2">Rémunération</p>
        <input
          type="text"
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-60"
          placeholder="5000000"
        />

        <p class="font-medium text-gray-700 ml-5 mr-2">Device</p>
        <select
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-20"
        >
          <option value="">FXA</option>
          <option value="">$</option>
          <option value="">EURO</option>
        </select>
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
