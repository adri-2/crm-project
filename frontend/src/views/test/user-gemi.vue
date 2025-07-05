<template>
  <div
    class="bg-white p-6 sm:p-8 md:p-10 shadow-xl rounded-2xl w-full max-w-4xl mx-auto my-8"
  >
    <div
      class="flex flex-col md:flex-row items-center md:items-start md:space-x-8 mb-8 space-y-6 md:space-y-0"
    >
      <div
        class="relative w-28 h-28 md:w-36 md:h-36 rounded-full bg-gray-100 flex items-center justify-center overflow-hidden border-4 border-blue-200 shadow-lg mx-auto md:mx-0 group cursor-pointer"
        @click="triggerFileInput"
      >
        <img
          v-if="employee.photoPreview || !isNewEmployee"
          :src="employee.photoPreview || employee.photoUrl || '../../public/placeholder-photo.png'"
          alt="Photo de profil"
          class="object-cover w-full h-full transition-opacity duration-300 group-hover:opacity-75"
        />
        <img
          v-else
          src="../../public/placeholder-photo.png"
          alt="Photo de profil par défaut"
          class="object-cover w-full h-full transition-opacity duration-300 group-hover:opacity-75"
        />
        <div
          class="absolute inset-0 bg-black bg-opacity-40 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300"
        >
          <span class="text-white text-sm font-semibold">Changer</span>
        </div>
        <input
          type="file"
          ref="fileInput"
          @change="handlePhotoUpload"
          class="hidden"
          accept="image/*"
        />
      </div>

      <div class="flex-1 w-full text-center md:text-left">
        <label for="employee-name" class="sr-only">Nom de l'employé</label>
        <input
          id="employee-name"
          type="text"
          v-model="employee.name"
          class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-2xl h-14 sm:h-16 text-2xl sm:text-3xl md:text-4xl px-2 sm:px-4 pt-2 sm:pt-6 pb-2 bg-transparent placeholder-gray-400 font-bold"
          placeholder="Nom de l'employé"
        />
        <p
          class="text-gray-500 flex items-center justify-center md:justify-start mt-2"
        >
          <span class="mr-2 text-xl md:text-2xl">💼</span>
          <label for="employee-title" class="sr-only">Titre du poste</label>
          <input
            id="employee-title"
            type="text"
            v-model="employee.jobTitle"
            class="border-0 border-b-2 border-blue-500 focus:border-blue-700 focus:outline-none w-full max-w-xl text-lg sm:text-xl md:text-2xl px-2 sm:px-4 pt-1 bg-transparent placeholder-gray-400"
            placeholder="Titre du poste"
          />
        </p>
      </div>
    </div>

    <h3
      class="text-lg font-semibold text-gray-700 border-b border-gray-200 pb-3 mb-6"
    >
      COORDONNÉES PROFESSIONNELLES
    </h3>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-6 mb-8">
      <div>
        <label for="email" class="block text-sm font-medium text-gray-700 mb-1"
          >Adresse e-mail professionnelle</label
        >
        <input
          id="email"
          type="email"
          v-model="employee.workEmail"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="ex. johndoe@example.com"
        />
      </div>
      <div>
        <label
          for="work-phone"
          class="block text-sm font-medium text-gray-700 mb-1"
          >Téléphone professionnel</label
        >
        <input
          id="work-phone"
          type="tel"
          v-model="employee.workPhone"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="ex. +1 234 567 8900"
        />
      </div>
      <div>
        <label
          for="mobile-phone"
          class="block text-sm font-medium text-gray-700 mb-1"
          >Téléphone portable professionnel</label
        >
        <input
          id="mobile-phone"
          type="tel"
          v-model="employee.mobilePhone"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="ex. +1 987 654 3210"
        />
      </div>
      <div class="mt-4 md:mt-0">
        <label for="tags" class="block text-sm font-medium text-gray-700 mb-1"
          >Étiquettes</label
        >
        <div class="text-gray-500 text-xs mb-1">
          ex. : Fondateur, Motorisé, Bâtiment B
        </div>
        <input
          id="tags"
          type="text"
          v-model="employee.tags"
          class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="Ajouter des étiquettes (séparées par des virgules)"
        />
      </div>
    </div>

    <h3
      class="text-lg font-semibold text-gray-700 border-b border-gray-200 pb-3 mb-6"
    >
      INFORMATIONS SUR LE POSTE
    </h3>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-6 mb-8">
      <div>
        <label
          for="department"
          class="block text-sm font-medium text-gray-700 mb-1"
          >Département</label
        >
        <input
          id="department"
          type="text"
          v-model="employee.department"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="ex. Marketing"
        />
      </div>
      <div>
        <label
          for="position"
          class="block text-sm font-medium text-gray-700 mb-1"
          >Poste</label
        >
        <input
          id="position"
          type="text"
          v-model="employee.position"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="ex. Directeur Commercial"
        />
      </div>
      <div>
        <label
          for="manager"
          class="block text-sm font-medium text-gray-700 mb-1"
          >Manager</label
        >
        <input
          id="manager"
          type="text"
          v-model="employee.manager"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="Nom du manager"
        />
      </div>
      <div>
        <label
          for="mentor"
          class="block text-sm font-medium text-gray-700 mb-1"
        >
          Mentor
          <span
            class="text-blue-500 cursor-help"
            title="Personne désignée pour guider l'employé"
            >?</span
          >
        </label>
        <input
          id="mentor"
          type="text"
          v-model="employee.mentor"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="Nom du mentor"
        />
      </div>
    </div>

    <div class="border-b border-gray-200 mb-6">
      <nav class="flex space-x-6 sm:space-x-8 text-base font-medium">
        <a
          href="#"
          :class="[
            'px-3 py-2 border-b-2 transition-colors duration-200',
            activeTab === 'cv'
              ? 'border-purple-600 text-purple-700 font-semibold'
              : 'border-transparent text-gray-600 hover:border-purple-400 hover:text-purple-600'
          ]"
          @click.prevent="activeTab = 'cv'"
          >CV</a
        >
        <a
          href="#"
          :class="[
            'px-3 py-2 border-b-2 transition-colors duration-200',
            activeTab === 'private'
              ? 'border-purple-600 text-purple-700 font-semibold'
              : 'border-transparent text-gray-600 hover:border-purple-400 hover:text-purple-600'
          ]"
          @click.prevent="activeTab = 'private'"
          >Informations privées</a
        >
        <a
          href="#"
          :class="[
            'px-3 py-2 border-b-2 transition-colors duration-200',
            activeTab === 'pay'
              ? 'border-purple-600 text-purple-700 font-semibold'
              : 'border-transparent text-gray-600 hover:border-purple-400 hover:text-purple-600'
          ]"
          @click.prevent="activeTab = 'pay'"
          >Paie</a
        >
      </nav>
    </div>

    <div
      v-if="activeTab === 'private'"
      class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-6 mb-8"
    >
      <div>
        <h3
          class="text-base font-semibold text-gray-600 border-b border-gray-200 pb-2 mb-4"
        >
          COORDONNÉES PRIVÉES
        </h3>
        <label
          for="personal-address"
          class="block text-sm font-medium text-gray-700 mb-1"
        >
          Adresse personnelle
          <span
            class="text-blue-500 cursor-help"
            title="Adresse résidentielle de l'employé"
            >?</span
          >
        </label>
        <input
          id="personal-address"
          type="text"
          v-model="employee.privateInfo.address"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="ex. 123 Rue de l'Exemple, Ville, Code Postal"
        />
        <label
          for="private-phone"
          class="block text-sm font-medium text-gray-700 mt-4 mb-1"
          >Numéro de téléphone privé</label
        >
        <input
          id="private-phone"
          type="tel"
          v-model="employee.privateInfo.privatePhone"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="ex. +237 6XX XXX XXX"
        />
      </div>
      <div>
        <h3
          class="text-base font-semibold text-gray-600 border-b border-gray-200 pb-2 mb-4"
        >
          ÉDUCATION
        </h3>
        <label
          for="education-level"
          class="block text-sm font-medium text-gray-700 mb-1"
        >
          Niveau scolaire
          <span
            class="text-blue-500 cursor-help"
            title="Dernier diplôme ou niveau d'études atteint"
            >?</span
          >
        </label>
        <input
          id="education-level"
          type="text"
          v-model="employee.privateInfo.educationLevel"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="ex. Licence, Master, Doctorat"
        />
        <label
          for="field-of-study"
          class="block text-sm font-medium text-gray-700 mt-4 mb-1"
        >
          Champ d'étude
          <span
            class="text-blue-500 cursor-help"
            title="Domaine principal d'études"
            >?</span
          >
        </label>
        <input
          id="field-of-study"
          type="text"
          v-model="employee.privateInfo.fieldOfStudy"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="ex. Informatique, Marketing, Droit"
        />
        <label
          for="school"
          class="block text-sm font-medium text-gray-700 mt-4 mb-1"
        >
          Établissement scolaire
          <span
            class="text-blue-500 cursor-help"
            title="Nom de l'école, université, etc."
            >?</span
          >
        </label>
        <input
          id="school"
          type="text"
          v-model="employee.privateInfo.school"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="ex. Université de Yaoundé I"
        />
      </div>
    </div>

    <div
      v-if="activeTab === 'cv'"
      class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-6 mb-8"
    >
      <div>
        <h3
          class="text-base font-semibold text-gray-600 border-b border-gray-200 pb-2 mb-4"
        >
          CV & COMPÉTENCES
        </h3>
        <label
          for="cv-upload"
          class="block text-sm font-medium text-gray-700 mb-1"
        >
          CV
          <span
            class="text-blue-500 cursor-help"
            title="Fichier du CV de l'employé"
            >?</span
          >
        </label>
        <input
          id="cv-upload"
          type="file"
          ref="cvFileInput"
          @change="handleCvUpload"
          class="mt-1 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
        />
        <p v-if="employee.cvFileName" class="text-xs text-gray-600 mt-1">
          Fichier actuel:
          <span class="font-medium">{{ employee.cvFileName }}</span>
        </p>

        <label
          for="skills"
          class="block text-sm font-medium text-gray-700 mt-4 mb-1"
          >Compétences</label
        >
        <textarea
          id="skills"
          v-model="employee.skills"
          rows="3"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400 resize-y"
          placeholder="ex. JavaScript, Vue.js, Gestion de projet, Communication"
        ></textarea>

        <label
          for="certification"
          class="block text-sm font-medium text-gray-700 mt-4 mb-1"
        >
          Certifications
          <span
            class="text-blue-500 cursor-help"
            title="Liste des certifications obtenues"
            >?</span
          >
        </label>
        <input
          id="certification"
          type="text"
          v-model="employee.certifications"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="ex. PMP, AWS Certified, Scrum Master"
        />
      </div>
    </div>

    <div
      v-if="activeTab === 'pay'"
      class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-6 mb-8"
    >
      <div>
        <h3
          class="text-base font-semibold text-gray-600 border-b border-gray-200 pb-2 mb-4"
        >
          PAIE
        </h3>
        <label
          for="gross-salary"
          class="block text-sm font-medium text-gray-700 mb-1"
          >Salaire brut</label
        >
        <input
          id="gross-salary"
          type="number"
          v-model="employee.payInfo.grossSalary"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="ex. 50000"
        />
        <label
          for="bonus"
          class="block text-sm font-medium text-gray-700 mt-4 mb-1"
          >Bonus annuel</label
        >
        <input
          id="bonus"
          type="number"
          v-model="employee.payInfo.bonus"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="ex. 5000"
        />
      </div>
      <div>
        <h3
          class="text-base font-semibold text-gray-600 border-b border-gray-200 pb-2 mb-4"
        >
          INFORMATIONS BANCAIRES
        </h3>
        <label for="iban" class="block text-sm font-medium text-gray-700 mb-1"
          >IBAN</label
        >
        <input
          id="iban"
          type="text"
          v-model="employee.payInfo.iban"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="ex. FR76XXXXXXXXXXXXXXX"
        />
        <label
          for="bic"
          class="block text-sm font-medium text-gray-700 mt-4 mb-1"
          >BIC</label
        >
        <input
          id="bic"
          type="text"
          v-model="employee.payInfo.bic"
          class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-transparent placeholder-gray-400"
          placeholder="ex. XXXXXXXXXXX"
        />
      </div>
    </div>

    <div
      class="mt-10 flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4 justify-end"
    >
      <button
        @click="cancelForm"
        type="button"
        class="flex-1 sm:flex-none bg-red-500 hover:bg-red-600 text-white font-semibold px-6 py-2 rounded-lg transition-colors duration-200 shadow-md hover:shadow-lg"
      >
        Annuler
      </button>
      <button
        @click="saveEmployee"
        type="submit"
        class="flex-1 sm:flex-none bg-green-600 hover:bg-green-700 text-white font-semibold px-6 py-2 rounded-lg transition-colors duration-200 shadow-md hover:shadow-lg"
      >
        {{ isNewEmployee ? 'Créer Employé' : 'Sauvegarder' }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// Determine if we are creating a new employee or editing an existing one
// This could be passed as a prop, or inferred from a route parameter (e.g., /employee/new vs /employee/:id/edit)
const isNewEmployee = ref(true); // Set to true for a new employee form, false for editing

// Reactive state for the form fields
const employee = ref({
  id: null, // Will be null for new employee, or an ID for existing
  name: '',
  jobTitle: '',
  photoUrl: '', // URL of existing photo if editing
  photoFile: null, // File object for new upload
  photoPreview: null, // Data URL for image preview
  workEmail: '',
  workPhone: '',
  mobilePhone: '',
  tags: '',
  department: '',
  position: '',
  manager: '',
  mentor: '',
  cvFileName: '', // To display current CV filename if editing
  cvFile: null, // File object for new CV upload
  skills: '',
  certifications: '',
  privateInfo: {
    address: '',
    privatePhone: '',
    educationLevel: '',
    fieldOfStudy: '',
    school: '',
  },
  payInfo: {
    grossSalary: null,
    bonus: null,
    iban: '',
    bic: '',
  },
});

// For simulating data loading for an existing employee
// In a real app, you would fetch this data based on `employee.id` from your backend
if (!isNewEmployee.value) {
  // Simulate loading existing employee data
  employee.value = {
    id: 123,
    name: 'Jean Dupont',
    jobTitle: 'Développeur Frontend Senior',
    photoUrl: 'https://via.placeholder.com/150/FFD700/000000?text=JD', // Example existing photo
    photoFile: null,
    photoPreview: null,
    workEmail: 'jean.dupont@example.com',
    workPhone: '+237 242 123 456',
    mobilePhone: '+237 677 123 456',
    tags: 'Innovation, Lead Tech, Mentoring',
    department: 'Développement',
    position: 'Développeur Frontend',
    manager: 'Marie Curie',
    mentor: 'Albert Einstein',
    cvFileName: 'Jean_Dupont_CV_2025.pdf', // Simulating an existing CV
    cvFile: null,
    skills: 'Vue.js, React, JavaScript, Node.js, Git, UI/UX Design',
    certifications: 'AWS Certified Developer, Scrum Master',
    privateInfo: {
      address: '15 Rue de la Paix, Douala, Cameroun',
      privatePhone: '+237 699 876 543',
      educationLevel: 'Master 2',
      fieldOfStudy: 'Informatique',
      school: 'Université de Douala',
    },
    payInfo: {
      grossSalary: 60000,
      bonus: 8000,
      iban: 'FR76XXXXXXXXXXXXXXXXXXXXX',
      bic: 'XAFRCMPM',
    },
  };
}

// References for file inputs
const fileInput = ref(null); // For photo input
const cvFileInput = ref(null); // For CV input

// Function to trigger the hidden file input click for photo
const triggerFileInput = () => {
  fileInput.value.click();
};

// Handle photo file selection and preview
const handlePhotoUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    employee.value.photoFile = file;
    const reader = new FileReader();
    reader.onload = (e) => {
      employee.value.photoPreview = e.target.result;
    };
    reader.readAsDataURL(file);
  } else {
    employee.value.photoFile = null;
    employee.value.photoPreview = null;
  }
};

// Handle CV file selection
const handleCvUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    employee.value.cvFile = file;
    employee.value.cvFileName = file.name;
  } else {
    employee.value.cvFile = null;
    employee.value.cvFileName = '';
  }
};

// Active tab state
const activeTab = ref('cv'); // Default active tab

// Save employee data (simulation)
const saveEmployee = () => {
  console.log('Données de l\'employé à sauvegarder :', JSON.parse(JSON.stringify(employee.value)));

  // Here you would typically send `employee.value` to your backend API
  // You might use FormData if you are sending files (photoFile, cvFile)
  // Example for a real API call (simplified):
  /*
  const formData = new FormData();
  for (const key in employee.value) {
    if (key === 'privateInfo' || key === 'payInfo') {
      for (const subKey in employee.value[key]) {
        formData.append(`${key}[${subKey}]`, employee.value[key][subKey]);
      }
    } else if (key === 'photoFile' && employee.value.photoFile) {
      formData.append('photo', employee.value.photoFile);
    } else if (key === 'cvFile' && employee.value.cvFile) {
      formData.append('cv', employee.value.cvFile);
    } else {
      formData.append(key, employee.value[key]);
    }
  }

  fetch('/api/employees', {
    method: isNewEmployee.value ? 'POST' : 'PUT',
    body: formData, // For files
    // For JSON only: headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(employee.value)
  })
  .then(response => response.json())
  .then(data => {
    console.log('Success:', data);
    alert(isNewEmployee.value ? 'Employé créé avec succès !' : 'Employé mis à jour avec succès !');
    // Redirect or update UI
  })
  .catch((error) => {
    console.error('Error:', error);
    alert('Erreur lors de l\'enregistrement de l\'employé.');
  });
  */

  alert(isNewEmployee.value ? 'Employé créé (simulé) ! Vérifiez la console.' : 'Employé sauvegardé (simulé) ! Vérifiez la console.');
};

// Cancel form (simulation)
const cancelForm = () => {
  console.log('Annulation du formulaire.');
  // In a real application, you might navigate back or reset the form
  // router.back(); or router.push('/employees');
};
</script>

<style scoped>
/* No specific styles needed here as Tailwind CSS handles most of the design. */
/* The placeholder styling for inputs is handled by Tailwind's utility classes. */
</style>
