<template>
  <div class="min-h-screen bg-white flex flex-col">
    
      <!-- Form Header -->
      <div class="bg-gradient-to-r from-orange-500 to-orange-600 px-6 py-12 md:py-16 text-white relative shrink-0">
        <button @click="$router.push('/')" class="absolute top-6 left-6 md:top-8 md:left-8 text-orange-100 hover:text-white flex items-center gap-2 font-medium transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-5 h-5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5 3 12m0 0 7.5-7.5M3 12h18" />
          </svg>
          Volver
        </button>
        <h2 class="text-3xl md:text-5xl font-extrabold text-center tracking-tight">Registro de Asistencia</h2>
        <p class="text-orange-100 text-center mt-4 md:text-lg">Selecciona al usuario y la actividad correspondiente</p>
      </div>

      <!-- Form Body -->
      <div class="flex-1 w-full max-w-4xl mx-auto p-6 md:p-12 lg:p-16">
        <form @submit.prevent="submitAttendance" class="space-y-10 md:space-y-12">
        
        <!-- Step 1: Beneficiary Search -->
        <div class="space-y-4">
          <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center border-b pb-2 gap-4">
            <div>
              <h3 class="text-xl font-semibold text-gray-800">1. Buscar Usuario</h3>
              <p class="text-sm text-gray-500">Ingresa la cédula, número de ID o Nombre para buscar al asistente.</p>
            </div>
            <button type="button" @click="showRegisterForm = true" class="text-sm bg-orange-100 text-orange-700 font-bold px-3 py-2 rounded-md hover:bg-orange-200 transition-colors">
              + Primer Registro
            </button>
          </div>
          
          <div class="relative">
            <input 
              v-model="searchQuery" 
              type="text" 
              placeholder="Ej: 8-000-0000 o 'Juan Pérez'" 
              class="w-full pl-4 pr-12 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition-all font-medium text-gray-700"
            >
            <button type="button" @click="searchBeneficiaries" class="absolute right-2 top-2 p-1.5 bg-orange-100 text-orange-600 rounded-md hover:bg-orange-200">
              Buscar
            </button>
          </div>

          <!-- Simulation of Search Results -->
          <ul v-if="beneficiaries.length > 0" class="mt-2 divide-y divide-gray-100 border border-gray-200 rounded-lg max-h-48 overflow-y-auto">
             <li v-for="b in beneficiaries" :key="b.id" 
                 @click="selectBeneficiary(b)"
                 class="p-3 hover:bg-orange-50 cursor-pointer flex justify-between items-center transition-colors"
                 :class="{ 'bg-orange-100 border-l-4 border-orange-500': selectedBeneficiary?.id === b.id }">
               <div>
                 <p class="font-medium text-gray-800">{{ b.first_name }} {{ b.last_name }}</p>
                 <p class="text-xs text-gray-500">
                    <span v-if="b.ci">Cédula: {{ b.ci }} | </span>
                    Edad: {{ calculateAge(b.dob) }}
                 </p>
               </div>
               <span v-if="selectedBeneficiary?.id === b.id" class="text-orange-600 font-bold px-2">&check; Seleccionado</span>
             </li>
          </ul>
        </div>

        <!-- Step 2: Activity Selection -->
        <div class="space-y-4" :class="{'opacity-50 pointer-events-none': !selectedBeneficiary}">
          <h3 class="text-xl font-semibold text-gray-800 border-b pb-2">2. Seleccionar Actividad y Evento</h3>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Activity Dropdown -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Actividad</label>
              <select 
                v-model="selectedActivity" 
                class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-500 bg-white"
                @change="updateEvents"
              >
                <option :value="null" disabled>Selecciona una opción...</option>
                <option v-for="act in activities" :key="act.id" :value="act">{{ act.name }}</option>
              </select>
            </div>

            <!-- Event Dropdown -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Evento</label>
              <select 
                v-model="selectedEvent" 
                :disabled="!selectedActivity"
                class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-500 bg-white disabled:bg-gray-100 disabled:text-gray-400"
              >
                <option :value="null" disabled>Selecciona un evento...</option>
                <option v-for="ev in availableEvents" :key="ev.id" :value="ev">{{ ev.name }}</option>
              </select>
            </div>
          </div>
        </div>

        <div v-if="submissionSuccess" class="p-4 bg-green-50 text-green-700 rounded-lg border border-green-200">
           ✅ ¡Asistencia registrada exitosamente!
        </div>

        <div v-if="submissionError" class="p-4 bg-red-50 text-red-700 rounded-lg border border-red-200 flex items-start gap-3">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-6 h-6 shrink-0 mt-0.5">
               <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
            </svg>
            <div>
               <p class="font-bold">Error de Registro</p>
               <p class="text-sm mt-1">{{ submissionError }}</p>
            </div>
        </div>

        <!-- Submit Button -->
        <div class="pt-4">
          <button 
            type="submit" 
            :disabled="!selectedBeneficiary || !selectedEvent || loading"
            class="w-full py-4 px-6 rounded-xl text-lg font-bold text-white bg-orange-600 hover:bg-orange-700 disabled:opacity-50 disabled:cursor-not-allowed shadow-lg hover:shadow-xl transition-all"
          >
            {{ loading ? 'Guardando...' : 'Registrar Asistencia' }}
          </button>
        </div>

        </form>
      </div>

    <!-- Public Register Modal -->
    <div v-if="showRegisterForm" class="fixed inset-0 bg-gray-900/60 backdrop-blur-sm overflow-y-auto h-full w-full z-50 flex justify-center items-center p-4">
        <div class="bg-white p-8 rounded-2xl shadow-2xl w-full max-w-lg border border-orange-100">
            <h2 class="text-2xl font-bold mb-2 text-gray-800">Primer Registro</h2>
            <p class="text-sm text-gray-500 mb-6">Completa tus datos para crear tu perfil en la plataforma.</p>
            
            <form @submit.prevent="submitRegistration" class="space-y-5">
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Nombre *</label>
                        <input v-model="regForm.first_name" required type="text" class="block w-full rounded-lg border-gray-300 shadow-sm p-3 border focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition-all bg-gray-50">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Apellido *</label>
                        <input v-model="regForm.last_name" required type="text" class="block w-full rounded-lg border-gray-300 shadow-sm p-3 border focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition-all bg-gray-50">
                    </div>
                </div>

                <div>
                   <label class="block text-sm font-medium text-gray-700 mb-1">Cédula o ID (Opcional)</label>
                   <input v-model="regForm.ci" type="text" class="block w-full rounded-lg border-gray-300 shadow-sm p-3 border focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition-all bg-gray-50">
                </div>

                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Fecha de Nac. *</label>
                        <input v-model="regForm.dob" required type="date" class="block w-full rounded-lg border-gray-300 shadow-sm p-3 border focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition-all bg-gray-50">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Sexo *</label>
                        <select v-model="regForm.sex" required class="block w-full rounded-lg border-gray-300 shadow-sm p-3 border focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition-all bg-gray-50">
                            <option value="M">Masculino</option>
                            <option value="F">Femenino</option>
                            <option value="O">Otro</option>
                        </select>
                    </div>
                </div>

                <div>
                   <label class="block text-sm font-medium text-gray-700 mb-1">Sector / Ubicación *</label>
                   <input v-model="regForm.sector" required type="text" class="block w-full rounded-lg border-gray-300 shadow-sm p-3 border focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition-all bg-gray-50">
                </div>

                <div v-if="regError" class="text-sm text-red-600 bg-red-50 p-3 rounded-lg border border-red-100">
                    {{ regError }}
                </div>
                
                <div class="flex justify-end gap-3 mt-8 pt-4 border-t border-gray-100">
                    <button type="button" @click="showRegisterForm = false" class="px-5 py-2.5 border border-gray-300 rounded-xl text-gray-700 font-medium hover:bg-gray-50 transition-colors">Cancelar</button>
                    <button type="submit" :disabled="regLoading" class="px-5 py-2.5 bg-orange-600 text-white font-bold rounded-xl shadow-md hover:bg-orange-700 hover:shadow-lg transition-all disabled:opacity-50">
                        {{ regLoading ? 'Creando Perfil...' : 'Crear Perfil' }}
                    </button>
                </div>
            </form>
        </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import apiClient from '../plugins/axios'

// Helpers
const calculateAge = (dobString) => {
    if (!dobString) return '?';
    const dob = new Date(dobString);
    const diff_ms = Date.now() - dob.getTime();
    const age_dt = new Date(diff_ms); 
    return Math.abs(age_dt.getUTCFullYear() - 1970);
}

// State
const searchQuery = ref('')
const beneficiaries = ref([])
const selectedBeneficiary = ref(null)

const activities = ref([])
const selectedActivity = ref(null)
const availableEvents = ref([])
const selectedEvent = ref(null)

const loading = ref(false)
const submissionSuccess = ref(false)
const submissionError = ref('')

// Public Registration State
const showRegisterForm = ref(false)
const regLoading = ref(false)
const regError = ref('')
const regForm = ref({
    ci: '',
    first_name: '',
    last_name: '',
    dob: '',
    sex: 'M',
    sector: ''
})

// Methods
const fetchActivities = async () => {
    try {
        const res = await apiClient.get('public/activities/')
        activities.value = res.data
    } catch (e) {
        console.error("Error fetching activities", e)
    }
}

const searchBeneficiaries = async () => {
    if (!searchQuery.value) return;
    try {
        const res = await apiClient.get(`public/beneficiaries/?search=${searchQuery.value}`)
        beneficiaries.value = res.data
        if (res.data.length === 0) {
            alert("No se encontró ningún usuario con ese criterio.")
        }
    } catch (e) {
        console.error("Error searching", e)
    }
}

const selectBeneficiary = (b) => {
    selectedBeneficiary.value = b
}

const updateEvents = () => {
    selectedEvent.value = null
    if (selectedActivity.value && selectedActivity.value.events) {
        availableEvents.value = selectedActivity.value.events
    } else {
        availableEvents.value = []
    }
}

const submitAttendance = async () => {
    loading.value = true
    submissionSuccess.value = false
    submissionError.value = ''
    try {
        await apiClient.post('public/attendance/', {
            beneficiary: selectedBeneficiary.value.id,
            event: selectedEvent.value.id
        })
        submissionSuccess.value = true
        // Limpiamos form pero podríamos dejar seleccionado todo por rapidez y solo cambiar el beneficiario
        setTimeout(() => {
            selectedBeneficiary.value = null
            searchQuery.value = ''
            beneficiaries.value = []
            submissionSuccess.value = false
        }, 3000)
    } catch (e) {
        console.error("Error saving attendance", e)
        // Check if there is a specific error response, otherwise fallback to user-friendly duplicate message
        const responseData = e.response?.data
        if (responseData && typeof responseData === 'object') {
            const firstErrorNode = Object.values(responseData)[0]
            if (Array.isArray(firstErrorNode)) {
                 submissionError.value = "Lo sentimos, no puedes marcar asistencia 2 veces para la misma actividad y evento."
            } else {
                 submissionError.value = "Lo sentimos, no puedes marcar asistencia 2 veces para la misma actividad y evento."
            }
        } else {
            submissionError.value = "Lo sentimos, no puedes marcar asistencia 2 veces para la misma actividad y evento."
        }

        setTimeout(() => {
            submissionError.value = ''
        }, 5000)
    } finally {
        loading.value = false
    }
}

const submitRegistration = async () => {
    regLoading.value = true
    regError.value = ''
    try {
        const res = await apiClient.post('public/beneficiaries/', regForm.value)
        
        // Auto-select the newly created user in the main form
        selectedBeneficiary.value = res.data
        searchQuery.value = res.data.first_name + ' ' + res.data.last_name
        beneficiaries.value = [res.data]
        
        // Reset and close modal
        showRegisterForm.value = false
        regForm.value = { ci: '', first_name: '', last_name: '', dob: '', sex: 'M', sector: '' }
        alert("Perfil creado existosamente! Ahora solo selecciona tu actividad.")
    } catch (e) {
        console.error("Error creating profile", e)
        if (e.response?.data?.ci) {
            regError.value = "Ya existe un usuario con esta Cédula / ID."
        } else {
            regError.value = "Hubo un error al crear el perfil. Revisa tus datos."
        }
    } finally {
        regLoading.value = false
    }
}

onMounted(() => {
    fetchActivities()
})
</script>
