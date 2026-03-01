<template>
  <div class="min-h-screen bg-orange-500 flex flex-col justify-center py-12 sm:px-6 lg:px-8 relative overflow-hidden">
    
    <div class="sm:mx-auto sm:w-full sm:max-w-md z-10">
      <h2 class="mt-6 text-center text-4xl font-extrabold text-white tracking-tight drop-shadow-md">
        Inicia sesión
      </h2>
    </div>
    <div class="mt-20 sm:mx-auto sm:w-full sm:max-w-md relative z-10">
      <!-- ROBOT ANIMATION -->
      <div class="absolute -top-[90px] left-1/2 transform -translate-x-1/2 w-48 h-32 flex justify-center items-end z-20 pointer-events-none">
          
          <!-- Robot Head -->
          <div class="relative w-28 h-24 bg-white border-4 border-gray-200 rounded-[2rem] shadow-sm flex flex-col items-center justify-center pb-2 z-0 transition-transform duration-500"
               :class="[
                  {'-translate-y-1': isUsernameFocused || isPasswordFocused},
                  {'robot-shake': isError}
               ]">
              <!-- Ears -->
              <div class="absolute -left-3 top-8 w-2 h-6 bg-gray-300 rounded-l-md"></div>
              <div class="absolute -right-3 top-8 w-2 h-6 bg-gray-300 rounded-r-md"></div>
              
              <!-- Antenna base -->
              <div class="absolute -top-3 w-6 h-2 bg-gray-300 rounded-t-md"></div>
              <!-- Antenna stick -->
              <div class="absolute -top-7 w-1.5 h-4 bg-gray-300"></div>
              <!-- Antenna bulb -->
              <div class="absolute -top-[36px] w-4 h-4 rounded-full transition-colors duration-300"
                   :class="isError ? 'bg-red-500 shadow-[0_0_15px_rgba(239,68,68,0.6)]' : (isSuccess ? 'bg-green-500 shadow-[0_0_15px_rgba(34,197,94,0.6)]' : (isPasswordFocused ? 'bg-orange-500 shadow-[0_0_15px_rgba(249,115,22,0.6)]' : (isUsernameFocused ? 'bg-[#1e9d8e] shadow-[0_0_15px_rgba(30,157,142,0.6)]' : 'bg-gray-300')))"></div>
                   
              <!-- Visor / Face Screen -->
              <div class="w-[72px] h-[36px] bg-[#1c2b42] rounded-xl relative overflow-hidden flex items-center px-[10px] justify-between shadow-inner mt-1">
                   <!-- Eye Left -->
                   <div class="w-3.5 h-3.5 transition-all duration-300 ease-out"
                        :class="[
                          isError ? 'bg-red-400 h-1.5 rotate-45 rounded-sm' : (isSuccess ? 'bg-green-400 h-2 w-4 rounded-b-full -translate-y-0.5' : 'rounded-full'),
                          !isError && !isSuccess && isPasswordFocused ? 'bg-orange-400 h-1 translate-y-1' : '',
                          !isError && !isSuccess && !isPasswordFocused ? 'bg-[#2ab1a6]' : '',
                          isUsernameFocused && !isPasswordFocused && !isError && !isSuccess ? 'translate-x-[6px] scale-110' : ''
                        ]"></div>
                   <!-- Eye Right -->
                   <div class="w-3.5 h-3.5 transition-all duration-300 ease-out"
                        :class="[
                          isError ? 'bg-red-400 h-1.5 -rotate-45 rounded-sm' : (isSuccess ? 'bg-green-400 h-2 w-4 rounded-b-full -translate-y-0.5' : 'rounded-full'),
                          !isError && !isSuccess && isPasswordFocused ? 'bg-orange-400 h-1 translate-y-1' : '',
                          !isError && !isSuccess && !isPasswordFocused ? 'bg-[#2ab1a6]' : '',
                          isUsernameFocused && !isPasswordFocused && !isError && !isSuccess ? 'translate-x-[6px] scale-110' : ''
                        ]"></div>
              </div>
              
              <!-- Mouth -->
              <div class="flex gap-1.5 mt-2.5">
                  <div class="w-1 h-2 bg-gray-200 rounded-full" :class="isSuccess || isError ? 'hidden' : ''"></div>
                  <div class="w-1 bg-gray-300 rounded-full transition-all duration-300"
                       :class="isSuccess ? 'h-1.5 !w-6 rounded-b-full bg-green-200' : (isError ? 'h-1 !w-4 bg-red-200' : (isUsernameFocused ? 'h-3' : 'h-2.5'))"></div>
                  <div class="w-1 h-2 bg-gray-200 rounded-full" :class="isSuccess || isError ? 'hidden' : ''"></div>
              </div>
          </div>
          
          <!-- Left Hand -->
          <div class="absolute w-[42px] h-[52px] bg-white border-4 border-gray-200 shadow-md rounded-[1.2rem] transition-all duration-500 ease-[cubic-bezier(0.34,1.56,0.64,1)] z-30 flex items-center justify-center origin-bottom"
               :class="isSuccess ? 'bottom-12 left-2 rotate-[45deg] scale-100' : (isError || isUsernameFocused || isPasswordFocused ? 'bottom-8 left-10 rotate-[15deg] scale-100' : '-bottom-[20px] left-3 -rotate-[25deg] translate-y-4 scale-90')">
               <div class="w-4 h-1.5 bg-gray-200 rounded-full"></div>
          </div>
          
          <!-- Right Hand -->
          <div class="absolute w-[42px] h-[52px] bg-white border-4 border-gray-200 shadow-md rounded-[1.2rem] transition-all duration-500 ease-[cubic-bezier(0.34,1.56,0.64,1)] z-30 flex items-center justify-center origin-bottom"
               :class="isSuccess ? 'bottom-12 right-2 -rotate-[45deg] scale-100' : (isError || isPasswordFocused ? 'bottom-8 right-10 -rotate-[15deg] scale-100' : '-bottom-[20px] right-3 rotate-[25deg] translate-y-4 scale-90')">
               <div class="w-4 h-1.5 bg-gray-200 rounded-full"></div>
          </div>
      </div>

      <div class="bg-white py-10 px-6 shadow-xl sm:rounded-[2rem] sm:px-12 border border-gray-100 relative z-10 transition-shadow duration-500"
           :class="(isUsernameFocused || isPasswordFocused) ? 'shadow-2xl shadow-orange-100/50' : ''">
        <form class="space-y-6" @submit.prevent="handleLogin">
          <div>
            <label for="username" class="block text-sm font-semibold text-gray-700">Usuario</label>
            <div class="mt-1.5">
              <input id="username" v-model="username" type="text" required 
                     @focus="isUsernameFocused = true" @blur="isUsernameFocused = false"
                     autocomplete="username"
                     class="appearance-none block w-full px-4 py-3 border border-gray-300 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 sm:text-sm font-medium transition-colors text-gray-800">
            </div>
          </div>

          <div>
            <label for="password" class="block text-sm font-semibold text-gray-700">Contraseña</label>
            <div class="mt-1.5">
              <input id="password" v-model="password" type="password" required 
                     @focus="isPasswordFocused = true" @blur="isPasswordFocused = false"
                     autocomplete="current-password"
                     class="appearance-none block w-full px-4 py-3 border border-gray-300 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 sm:text-sm font-medium transition-colors text-gray-800">
            </div>
          </div>

          <!-- Error banner (shown below the robot too) -->
          <div v-if="error && !isError" class="text-sm text-red-700 bg-red-50 py-3 px-4 rounded-xl border border-red-200 flex items-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5 shrink-0">
              <path fill-rule="evenodd" d="M18 10a8 8 0 1 1-16 0 8 8 0 0 1 16 0Zm-8-5a.75.75 0 0 1 .75.75v4.5a.75.75 0 0 1-1.5 0v-4.5A.75.75 0 0 1 10 5Zm0 10a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z" clip-rule="evenodd" />
            </svg>
            {{ error }}
          </div>

          <div class="pt-2">
            <button type="submit" :disabled="loading || isSuccess" 
                    class="w-full flex justify-center py-3.5 px-4 border border-transparent rounded-xl shadow-md text-sm font-bold text-white bg-[#1c2b42] hover:bg-[#2a3c58] hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#1c2b42] disabled:opacity-50 transition-all uppercase tracking-wider">
              {{ isSuccess ? '¡Bienvenido! 🎉' : (loading ? 'Conectando...' : 'Iniciar Sesión') }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<style scoped>
.robot-shake {
  animation: robot-no 0.65s cubic-bezier(.36,.07,.19,.97) both;
}
@keyframes robot-no {
  0%   { transform: rotate(0deg); }
  10%  { transform: rotate(-10deg); }
  30%  { transform: rotate(10deg); }
  50%  { transform: rotate(-10deg); }
  70%  { transform: rotate(10deg); }
  90%  { transform: rotate(-4deg); }
  100% { transform: rotate(0deg); }
}
</style>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import apiClient from '../plugins/axios'

const router = useRouter()
const username = ref('')
const password = ref('')
const loading = ref(false)
const error = ref('')
const isUsernameFocused = ref(false)
const isPasswordFocused = ref(false)
const isError = ref(false)
const isSuccess = ref(false)

const handleLogin = async () => {
  if (loading.value || isSuccess.value) return
  loading.value = true
  error.value = ''
  isError.value = false
  isSuccess.value = false
  
  try {
    const response = await apiClient.post('token/', {
      username: username.value.trim(),
      password: password.value
    })
    
    localStorage.setItem('access_token', response.data.access)
    localStorage.setItem('refresh_token', response.data.refresh)
    
    isSuccess.value = true
    setTimeout(() => {
      router.push('/dashboard')
    }, 1200)

  } catch (err) {
    isError.value = true
    
    if (err.response?.status === 401) {
      error.value = 'Credenciales inválidas. Verifica tu usuario y contraseña.'
    } else if (err.code === 'ECONNABORTED' || !err.response) {
      error.value = 'No se pudo conectar al servidor. Intenta de nuevo.'
    } else {
      error.value = 'Hubo un error al intentar iniciar sesión. Intenta más tarde.'
    }

    // After shake animation, refocus username field
    setTimeout(() => {
      isError.value = false
    }, 1500)

    console.error('[Login Error]', err.response?.status, err.message)
  } finally {
    loading.value = false
  }
}
</script>
