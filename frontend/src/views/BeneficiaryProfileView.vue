<template>
  <div class="min-h-screen bg-gray-50">

    <!-- Main Content -->
    <div class="max-w-[1200px] mx-auto p-6 md:p-8 space-y-6">

     <div class="flex justify-between items-center mb-6">
       <div>
           <router-link to="/beneficiaries" class="text-[13px] font-medium text-[#8e98a8] hover:text-[#f05100] mb-2 inline-flex items-center transition-colors">
               <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-4 h-4 mr-1">
                 <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5 3 12m0 0 7.5-7.5M3 12h18" />
               </svg>
               Volver a Usuarios
           </router-link>
           <h1 class="text-[28px] font-extrabold text-[#1c2b42] tracking-tight">Perfil de Usuario</h1>
       </div>
     </div>

     <div v-if="loading" class="text-center py-12 text-gray-500">
         Cargando perfil...
     </div>

     <div v-else-if="profile" class="grid grid-cols-1 md:grid-cols-3 gap-6">
         <!-- Left Column: User Details -->
         <div class="col-span-1 space-y-6">
             <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden pb-4">
                 <div class="bg-[#f05100] h-32"></div>
                 <div class="px-6 relative">
                     <div class="w-28 h-28 rounded-full bg-white shadow-sm mx-auto -mt-14 flex items-center justify-center text-4xl font-extrabold text-[#f05100] uppercase tracking-wider">
                         {{ initials }}
                     </div>
                     <h2 class="text-2xl font-extrabold text-center text-[#1c2b42] mt-4 tracking-tight">{{ profile.first_name }} {{ profile.last_name }}</h2>
                     <p class="text-center text-[#8e98a8] text-sm mt-1 mb-8">{{ profile.ci || 'No registró Cédula / ID' }}</p>
                     
                     <div class="space-y-4 px-2">
                         <div class="flex items-start gap-4 mt-8">
                             <div class="mt-0.5 text-[#e55e5e] text-lg">
                               <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-[18px] h-[18px]">
                                 <path fill-rule="evenodd" d="m11.54 22.351.07.04.028.016a.76.76 0 0 0 .723 0l.028-.015.071-.041a16.975 16.975 0 0 0 1.144-.742 19.58 19.58 0 0 0 2.683-2.282c1.944-1.99 3.963-4.98 3.963-8.827a8.25 8.25 0 0 0-16.5 0c0 3.846 2.02 6.837 3.963 8.827a19.58 19.58 0 0 0 2.682 2.282 16.975 16.975 0 0 0 1.145.742ZM12 13.5a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z" clip-rule="evenodd" />
                               </svg>
                             </div>
                             <div>
                                 <span class="block text-[11px] text-[#8e98a8] font-medium leading-none mb-1">Sector</span>
                                 <span class="font-medium text-[#1c2b42] text-sm leading-none">{{ profile.sector || 'No especificado' }}</span>
                             </div>
                         </div>
                         <div class="flex items-start gap-4 mt-4">
                             <div class="mt-0.5 text-[#5e8ee5] text-lg">
                               <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-[18px] h-[18px]">
                                 <path d="M12.75 12.75a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM7.5 15.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5ZM8.25 17.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM9.75 15.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5ZM10.5 17.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM12 15.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5ZM12.75 17.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM14.25 15.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5ZM15 17.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM16.5 15.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5ZM15 12.75a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM16.5 13.5a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Z" />
                                 <path fill-rule="evenodd" d="M6.75 2.25A.75.75 0 0 1 7.5 3v1.5h9V3A.75.75 0 0 1 18 3v1.5h.75a3 3 0 0 1 3 3v11.25a3 3 0 0 1-3 3H5.25a3 3 0 0 1-3-3V7.5a3 3 0 0 1 3-3H6V3a.75.75 0 0 1 .75-.75Zm13.5 9a1.5 1.5 0 0 0-1.5-1.5H5.25a1.5 1.5 0 0 0-1.5 1.5v7.5a1.5 1.5 0 0 0 1.5 1.5h13.5a1.5 1.5 0 0 0 1.5-1.5v-7.5Z" clip-rule="evenodd" />
                               </svg>
                             </div>
                             <div>
                                 <span class="block text-[11px] text-[#8e98a8] font-medium leading-none mb-1">Nacimiento</span>
                                 <span class="font-medium text-[#1c2b42] text-sm leading-none">{{ profile.dob || 'No especificado' }}</span>
                             </div>
                         </div>
                         <div class="flex items-start gap-4 mt-4 mb-4">
                             <div class="mt-0.5 text-[#5e5a6a] text-lg">
                               <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-[18px] h-[18px]">
                                 <path fill-rule="evenodd" d="M7.5 6a4.5 4.5 0 1 1 9 0 4.5 4.5 0 0 1-9 0ZM3.751 20.105a8.25 8.25 0 0 1 16.498 0 .75.75 0 0 1-.437.695A18.683 18.683 0 0 1 12 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 0 1-.437-.695Z" clip-rule="evenodd" />
                               </svg>
                             </div>
                             <div>
                                 <span class="block text-[11px] text-[#8e98a8] font-medium leading-none mb-1">Sexo</span>
                                 <span class="font-medium text-[#1c2b42] text-sm leading-none">{{ profile.sex }}</span>
                             </div>
                         </div>
                         <div class="flex items-start gap-4 border-t border-gray-100 pt-5 mt-5">
                             <div class="mt-0.5 text-[#8e98a8] text-lg">
                               <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-[18px] h-[18px]">
                                 <path fill-rule="evenodd" d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25ZM12.75 6a.75.75 0 0 0-1.5 0v6c0 .414.336.75.75.75h4.5a.75.75 0 0 0 0-1.5h-3.75V6Z" clip-rule="evenodd" />
                               </svg>
                             </div>
                             <div>
                                 <span class="block text-[11px] text-[#8e98a8] font-medium leading-none mb-1">Registrado el</span>
                                 <span class="font-medium text-[#1c2b42] text-sm leading-none">{{ profile.created_at }}</span>
                             </div>
                         </div>
                     </div>
                 </div>
             </div>
         </div>

         <!-- Right Column: Stats & Breakdown -->
         <div class="col-span-1 md:col-span-2 space-y-6">
             
             <!-- Top Activities Breakdown -->
             <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
                 <div class="flex items-center justify-between mb-6">
                     <h3 class="text-[17px] font-extrabold text-[#1c2b42] flex items-center gap-2">
                         Actividades Frecuentes
                         <span class="text-[10px] py-1 px-2.5 bg-[#feefe6] text-[#f05100] rounded-full font-bold uppercase tracking-wider">Tops</span>
                     </h3>
                     <div class="text-right">
                         <span class="text-xs text-gray-500 font-medium">Asistencias Totales:</span>
                         <span class="ml-1 text-lg font-extrabold text-[#1c2b42]">{{ profile.stats.total_attendance }}</span>
                     </div>
                 </div>
                 
                 <div v-if="profile.stats.top_activities.length > 0" class="space-y-4">
                     <div v-for="(act, idx) in profile.stats.top_activities" :key="idx" class="flex items-center bg-[#fafafb] rounded-xl p-4">
                         <div class="w-10 h-10 rounded-full bg-orange-100 text-orange-600 flex items-center justify-center font-bold mr-4 shrink-0 shadow-sm border border-white">
                             #{{ idx + 1 }}
                         </div>
                         <div class="flex-1">
                             <h4 class="font-bold text-gray-800">{{ act.activity_name }}</h4>
                             <p class="text-xs font-semibold text-gray-400">{{ act.event_name }}</p>
                         </div>
                         <div class="text-right ml-4 shrink-0">
                             <div class="inline-flex items-center gap-1.5 bg-[#e8f7f5] text-[#1e9d8e] px-3.5 py-1.5 rounded-2xl border border-[#c6ece8] shadow-sm">
                                <span class="text-base font-extrabold">{{ act.count }}</span>
                                <span class="text-[10px] uppercase font-bold tracking-wider">veces</span>
                             </div>
                         </div>
                     </div>
                 </div>
                 <div v-else class="text-center py-8 text-gray-500 italic">
                     Este usuario aún no tiene asistencias registradas.
                 </div>
             </div>

             <!-- Recent History -->
             <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
                 <h3 class="text-[17px] font-extrabold text-[#1c2b42] mb-6">Últimas Asistencias</h3>
                 <div v-if="profile.stats.recent_history.length > 0">
                     <div class="border-l-2 border-orange-200 ml-4 space-y-8 relative pb-2 pt-2">
                        <div v-for="(rec, idx) in profile.stats.recent_history" :key="idx" class="relative pl-8">
                            <span class="absolute -left-[9px] top-1.5 w-4 h-4 rounded-full bg-orange-500 ring-4 ring-white shadow-sm"></span>
                            <div class="flex justify-between items-start">
                                <div>
                                    <h4 class="font-semibold text-gray-800">{{ rec.activity }}</h4>
                                    <p class="text-xs text-gray-500 pt-0.5">{{ rec.event }}</p>
                                </div>
                                <span class="text-[11px] font-bold text-gray-500 bg-gray-100 px-2.5 py-1 rounded shadow-sm border border-gray-200">{{ rec.date }}</span>
                            </div>
                        </div>
                     </div>
                 </div>
                 <div v-else class="text-center py-8 text-gray-500 italic">
                     No hay historial reciente.
                 </div>
             </div>

         </div>

     </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import apiClient from '../plugins/axios'

const router = useRouter()
const route = useRoute()

const loading = ref(true)
const profile = ref(null)

const userId = route.params.id

const initials = computed(() => {
    if(!profile.value) return '';
    return (profile.value.first_name.charAt(0) + profile.value.last_name.charAt(0)).toUpperCase();
})

const fetchProfile = async () => {
    try {
        const res = await apiClient.get(`reports/beneficiary-profile/${userId}/`)
        profile.value = res.data
    } catch (e) {
        console.error("Error fetching profile", e)
        alert("Usuario no encontrado")
        router.push('/beneficiaries')
    } finally {
        loading.value = false
    }
}

const logout = () => {
  localStorage.removeItem('access_token')
  localStorage.removeItem('refresh_token')
  router.push('/login')
}

onMounted(() => {
    fetchProfile()
})
</script>
