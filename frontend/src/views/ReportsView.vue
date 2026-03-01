<template>
  <div class="min-h-screen bg-gray-50">

    <!-- Main Content -->
    <div class="max-w-[1400px] mx-auto p-6 md:p-8 flex flex-col md:flex-row gap-8">
      
      <!-- Sidebar Menu -->
      <div class="w-full md:w-64 shrink-0 bg-white rounded-xl shadow-sm border border-gray-100 p-4">
          <h2 class="text-sm font-bold text-gray-400 uppercase tracking-wider mb-4 px-3">Tipos de Reporte</h2>
          <nav class="space-y-1">
              <button @click="selectedReport = 'attendance'" 
                      :class="['w-full flex items-center justify-between px-3 py-3 rounded-lg text-sm font-medium transition-colors', 
                              selectedReport === 'attendance' ? 'bg-orange-50 text-orange-700' : 'text-gray-600 hover:bg-gray-50']">
                  <span>Asistencias por Día</span>
                  <svg v-if="selectedReport === 'attendance'" class="w-5 h-5 text-orange-500" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
              </button>
              
              <button @click="selectedReport = 'activities'" 
                      :class="['w-full flex items-center justify-between px-3 py-3 rounded-lg text-sm font-medium transition-colors', 
                              selectedReport === 'activities' ? 'bg-orange-50 text-orange-700' : 'text-gray-600 hover:bg-gray-50']">
                  <span>Actividades más visitadas</span>
                  <svg v-if="selectedReport === 'activities'" class="w-5 h-5 text-orange-500" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
              </button>

              <button @click="selectedReport = 'events'" 
                      :class="['w-full flex items-center justify-between px-3 py-3 rounded-lg text-sm font-medium transition-colors', 
                              selectedReport === 'events' ? 'bg-orange-50 text-orange-700' : 'text-gray-600 hover:bg-gray-50']">
                  <span>Por Evento</span>
                  <svg v-if="selectedReport === 'events'" class="w-5 h-5 text-orange-500" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
              </button>
          </nav>
      </div>

      <div class="flex-1 space-y-6">
        
        <div class="flex justify-between items-end">
            <div>
                <h2 class="text-2xl font-bold text-gray-800">
                    {{ selectedReport === 'attendance' ? 'Reporte de Asistencia' : selectedReport === 'activities' ? 'Actividades con más asistencias' : selectedReport === 'events' ? 'Reporte por Evento' : 'Historial de Asistencias por Día' }}
                </h2>
                <p class="text-gray-500 mt-1">Filtra y exporta el historial.</p>
            </div>
            
            <div class="flex gap-3">
                <button @click="exportToPDF" :disabled="!currentRecords.length" class="flex flex-row items-center gap-2 px-4 py-2 bg-red-50 text-red-600 rounded-md hover:bg-red-100 font-medium disabled:opacity-50">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="size-5">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z" />
                    </svg>
                    PDF
                </button>
                <button @click="exportToExcel" :disabled="!currentRecords.length" class="flex flex-row items-center gap-2 px-4 py-2 bg-green-50 text-green-700 rounded-md hover:bg-green-100 font-medium disabled:opacity-50">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="size-5">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z" />
                    </svg>
                    Excel
                </button>
            </div>
        </div>

        <!-- Filters -->
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-100 mb-6">
            <div class="flex flex-wrap items-end gap-6 mb-6">
                <div class="flex-1 min-w-[160px]">
                    <label class="block text-sm font-medium text-gray-500 mb-2">Fecha de Inicio</label>
                    <input type="date" v-model="filters.start_date" class="block w-full border-0 border-b-2 border-gray-200 focus:ring-0 focus:border-orange-600 bg-transparent py-2 px-0 text-gray-700 transition-colors">
                </div>
                <div class="flex-1 min-w-[160px]">
                    <label class="block text-sm font-medium text-gray-500 mb-2">Fecha Final</label>
                    <input type="date" v-model="filters.end_date" class="block w-full border-0 border-b-2 border-gray-200 focus:ring-0 focus:border-orange-600 bg-transparent py-2 px-0 text-gray-700 transition-colors">
                </div>
                <template v-if="selectedReport === 'attendance'">
                    <div class="flex-1 min-w-[130px]">
                        <label class="block text-sm font-medium text-gray-500 mb-2">Hora de Inicio</label>
                        <input type="time" v-model="filters.start_time" class="block w-full border-0 border-b-2 border-gray-200 focus:ring-0 focus:border-orange-600 bg-transparent py-2 px-0 text-gray-700 transition-colors">
                    </div>
                    <div class="flex-1 min-w-[130px]">
                        <label class="block text-sm font-medium text-gray-500 mb-2">Hora Final</label>
                        <input type="time" v-model="filters.end_time" class="block w-full border-0 border-b-2 border-gray-200 focus:ring-0 focus:border-orange-600 bg-transparent py-2 px-0 text-gray-700 transition-colors">
                    </div>
                </template>
                <button @click="fetchReport" class="px-8 py-2.5 bg-orange-600 text-white font-bold rounded shadow hover:bg-orange-700 transition-colors uppercase text-sm tracking-wider">
                    BUSCAR
                </button>
            </div>

            <!-- Quick Actions -->
            <div class="flex flex-wrap gap-4 mt-8 justify-start">
                <button @click="setQuickFilter('hoy')" class="w-16 h-16 rounded-full bg-orange-600 text-white font-bold text-xs shadow-md hover:bg-orange-700 hover:-translate-y-1 flex items-center justify-center transition-all duration-200">
                    Hoy
                </button>
                <button @click="setQuickFilter('ayer')" class="w-16 h-16 rounded-full bg-orange-600 text-white font-bold text-xs shadow-md hover:bg-orange-700 hover:-translate-y-1 flex items-center justify-center transition-all duration-200">
                    Ayer
                </button>
                <button @click="setQuickFilter('semana')" class="w-16 h-16 rounded-full bg-orange-600 text-white font-bold text-xs shadow-md hover:bg-orange-700 hover:-translate-y-1 flex items-center justify-center transition-all duration-200">
                    Semana
                </button>
                <button @click="setQuickFilter('semana_pasada')" class="w-16 h-16 rounded-full bg-orange-600 text-white font-bold text-xs text-center leading-tight shadow-md hover:bg-orange-700 hover:-translate-y-1 flex items-center justify-center transition-all duration-200">
                    Semana<br>pasada
                </button>
                <button @click="setQuickFilter('mes')" class="w-16 h-16 rounded-full bg-orange-600 text-white font-bold text-xs shadow-md hover:bg-orange-700 hover:-translate-y-1 flex items-center justify-center transition-all duration-200">
                    Mes
                </button>
                <button @click="setQuickFilter('mes_pasado')" class="w-16 h-16 rounded-full bg-orange-600 text-white font-bold text-xs text-center leading-tight shadow-md hover:bg-orange-700 hover:-translate-y-1 flex items-center justify-center transition-all duration-200">
                    Mes<br>pasado
                </button>
            </div>
        </div>

        <!-- Tables area -->
        <div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">

          <!-- Prompt before first search -->
          <div v-if="!hasSearched && !loading" class="flex flex-col items-center justify-center py-20 text-gray-400 gap-3">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-12 h-12 text-orange-200">
              <path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
            </svg>
            <p class="text-sm font-medium">Selecciona un rango de fechas y presiona <strong class="text-orange-600">BUSCAR</strong></p>
          </div>

          <!-- Loading -->
          <div v-else-if="loading" class="flex items-center justify-center py-20 text-gray-400">
            <svg class="animate-spin h-6 w-6 mr-2 text-orange-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"></path>
            </svg>
            Cargando datos...
          </div>

          <template v-else>
            <transition name="fade-slide" mode="out-in" appear>
              <div :key="selectedReport">
              <!-- Table: Attendance History -->
            <table v-if="selectedReport === 'attendance'" class="min-w-full divide-y divide-gray-200">
                <thead class="bg-gray-50">
                    <tr>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Fecha</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Hora</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Uarsuio</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Cédula</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actividad</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Evento / Detalles</th>
                    </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                    <tr v-for="record in attendanceRecords" :key="record.id" class="hover:bg-gray-50">
                        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ record.date }}</td>
                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 font-mono">{{ record.time }}</td>
                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">{{ record.beneficiary_name }}</td>
                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ record.beneficiary_ci }}</td>
                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">{{ record.activity_name }}</td>
                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ record.event_name }}</td>
                    </tr>
                    <tr v-if="attendanceRecords.length === 0">
                        <td colspan="6" class="px-6 py-10 text-center text-gray-400">Sin resultados para el rango seleccionado.</td>
                    </tr>
                </tbody>
            </table>

            <!-- Table: Top Activities -->
            <table v-if="selectedReport === 'activities'" class="min-w-full divide-y divide-gray-200">
                <thead class="bg-gray-50">
                    <tr>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actividad</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Evento / Detalles</th>
                        <th class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Nº de Asistentes Únicos</th>
                        <th class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider w-16">Detalle</th>
                    </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                    <tr v-for="(record, idx) in activityRecords" :key="idx" class="hover:bg-gray-50">
                        <td class="px-6 py-4 whitespace-nowrap text-sm font-bold text-gray-900">{{ record.activity_name }}</td>
                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">{{ record.event_name }}</td>
                        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-center text-orange-600 bg-orange-50">{{ record.attendees }}</td>
                        <td class="px-6 py-4 whitespace-nowrap text-center">
                            <button
                              @click="openAttendeesModal(record)"
                              class="w-7 h-7 rounded-full bg-orange-600 text-white hover:bg-orange-700 transition-all flex items-center justify-center mx-auto font-bold text-base shadow-sm"
                              title="Ver asistentes"
                            >+</button>
                        </td>
                    </tr>
                    <tr v-if="activityRecords.length === 0">
                        <td colspan="4" class="px-6 py-10 text-center text-gray-400">Sin resultados para el rango seleccionado.</td>
                    </tr>
                </tbody>
            </table>

            <!-- Table: Por Evento -->
            <table v-if="selectedReport === 'events'" class="min-w-full divide-y divide-gray-200">
                <thead class="bg-gray-50">
                    <tr>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Evento</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actividad</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Fecha Evento</th>
                        <th class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Asistentes Únicos</th>
                        <th class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider w-16">Detalle</th>
                    </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                    <tr v-for="(record, idx) in eventRecords" :key="idx" class="hover:bg-gray-50">
                        <td class="px-6 py-4 whitespace-nowrap text-sm font-bold text-gray-900">{{ record.event_name }}</td>
                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">{{ record.activity_name }}</td>
                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ record.event_date }}</td>
                        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-center text-orange-600 bg-orange-50">{{ record.attendees }}</td>
                        <td class="px-6 py-4 whitespace-nowrap text-center">
                            <button
                              @click="openAttendeesModal(record)"
                              class="w-7 h-7 rounded-full bg-orange-600 text-white hover:bg-orange-700 transition-all flex items-center justify-center mx-auto font-bold text-base shadow-sm"
                              title="Ver asistentes"
                            >+</button>
                        </td>
                    </tr>
                    <tr v-if="eventRecords.length === 0">
                        <td colspan="5" class="px-6 py-10 text-center text-gray-400">Sin resultados para el rango seleccionado.</td>
                    </tr>
                </tbody>
            </table>
              </div>
            </transition>
          </template>
        </div>

      </div>
    </div>
  </div>

  <!-- ===== Attendees Detail Modal ===== -->
  <div v-if="showAttendeesModal" class="fixed inset-0 bg-black/50 z-50 flex items-center justify-center p-4" @click.self="showAttendeesModal = false">
    <div class="bg-white rounded-2xl shadow-2xl w-full max-w-3xl max-h-[85vh] flex flex-col overflow-hidden">

      <!-- Modal Header -->
      <div class="flex items-center justify-between px-6 py-4 border-b border-gray-100">
        <div>
          <h2 class="text-lg font-extrabold text-gray-800">Asistentes: {{ modalRecord?.activity_name }}</h2>
          <p class="text-sm text-gray-400 mt-0.5">{{ modalRecord?.event_name }} · {{ filters.start_date }} – {{ filters.end_date }}</p>
        </div>
        <button @click="showAttendeesModal = false" class="text-gray-400 hover:text-gray-600 transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>
      </div>

      <!-- Export buttons -->
      <div class="flex items-center gap-3 px-6 py-3 border-b border-gray-100 bg-gray-50">
        <button @click="exportAttendeesExcel" :disabled="!attendeesList.length" class="flex items-center gap-1.5 px-3 py-1.5 bg-green-50 text-green-700 rounded-md hover:bg-green-100 font-semibold text-sm transition-colors disabled:opacity-40">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z" /></svg>
          Excel
        </button>
        <button @click="exportAttendeesPDF" :disabled="!attendeesList.length" class="flex items-center gap-1.5 px-3 py-1.5 bg-red-50 text-red-600 rounded-md hover:bg-red-100 font-semibold text-sm transition-colors disabled:opacity-40">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z" /></svg>
          PDF
        </button>
        <span class="ml-auto text-xs text-gray-400">{{ attendeesList.length }} asistente{{ attendeesList.length !== 1 ? 's' : '' }}</span>
      </div>

      <!-- Table -->
      <div class="overflow-y-auto flex-1">
        <div v-if="modalLoading" class="flex items-center justify-center py-16 text-gray-400">
          <svg class="animate-spin h-6 w-6 mr-2 text-orange-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"></path>
          </svg>
          Cargando...
        </div>
        <table v-else class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50 sticky top-0">
            <tr>
              <th class="px-5 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">#</th>
              <th class="px-5 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Fecha</th>
              <th class="px-5 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Hora</th>
              <th class="px-5 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Nombre</th>
              <th class="px-5 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Cédula</th>
              <th class="px-5 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Sector</th>
              <th class="px-5 py-3 text-center text-xs font-semibold text-gray-500 uppercase tracking-wider">Visitas</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-100">
            <tr v-for="(a, i) in attendeesList" :key="i" class="hover:bg-orange-50 transition-colors">
              <td class="px-5 py-3 text-sm text-gray-400">{{ i + 1 }}</td>
              <td class="px-5 py-3 text-sm font-semibold text-gray-800">{{ a.ultima_asistencia }}</td>
              <td class="px-5 py-3 text-sm font-semibold text-orange-600">{{ a.ultima_hora || '—' }}</td>
              <td class="px-5 py-3 text-sm text-gray-800">{{ a.nombre }}</td>
              <td class="px-5 py-3 text-sm text-gray-500">{{ a.cedula }}</td>
              <td class="px-5 py-3 text-sm text-gray-500">{{ a.sector }}</td>
              <td class="px-5 py-3 text-sm text-center">
                <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-orange-100 text-orange-700 font-bold text-xs">{{ a.total_visitas }}</span>
              </td>
            </tr>
            <tr v-if="!modalLoading && attendeesList.length === 0">
              <td colspan="7" class="px-5 py-10 text-center text-gray-400">No hay asistentes registrados en este período.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import apiClient from '../plugins/axios'
import * as XLSX from 'xlsx'
import { jsPDF } from 'jspdf'
import autoTable from 'jspdf-autotable'

const loading = ref(false)
const hasSearched = ref(false)

// --- Attendees Modal ---
const showAttendeesModal = ref(false)
const modalLoading = ref(false)
const modalRecord = ref(null)
const attendeesList = ref([])

const openAttendeesModal = async (record) => {
    modalRecord.value = record
    showAttendeesModal.value = true
    modalLoading.value = true
    attendeesList.value = []
    try {
        const params = new URLSearchParams()
        params.append('activity_name', record.activity_name)
        params.append('event_name', record.event_name)
        if (filters.value.start_date) params.append('start_date', filters.value.start_date)
        if (filters.value.end_date) params.append('end_date', filters.value.end_date)
        const res = await apiClient.get(`reports/event-attendees/?${params.toString()}`)
        attendeesList.value = res.data
    } catch (e) {
        console.error('Error fetching attendees', e)
    } finally {
        modalLoading.value = false
    }
}

const exportAttendeesExcel = () => {
    const ws = XLSX.utils.json_to_sheet(attendeesList.value.map((a, i) => ({
        '#': i + 1,
        'Fecha': a.ultima_asistencia,
        'Hora': a.ultima_hora || '',
        'Nombre': a.nombre,
        'Cédula': a.cedula,
        'Sector': a.sector,
        'Total Visitas': a.total_visitas,
    })))
    const wb = XLSX.utils.book_new()
    XLSX.utils.book_append_sheet(wb, ws, 'Asistentes')
    XLSX.writeFile(wb, `Asistentes_${modalRecord.value?.activity_name}_${modalRecord.value?.event_name}_${getLocalISODate()}.xlsx`)
}

const exportAttendeesPDF = () => {
    const doc = new jsPDF()
    const title = `Asistentes: ${modalRecord.value?.activity_name} - ${modalRecord.value?.event_name}`
    doc.text(title, 14, 15)
    doc.setFontSize(9)
    doc.setTextColor(120)
    doc.text(`Período: ${filters.value.start_date} – ${filters.value.end_date}`, 14, 22)
    autoTable(doc, {
        head: [['#', 'Fecha', 'Hora', 'Nombre', 'Cédula', 'Sector', 'Visitas']],
        body: attendeesList.value.map((a, i) => [i + 1, a.ultima_asistencia, a.ultima_hora || '', a.nombre, a.cedula, a.sector, a.total_visitas]),
        startY: 27,
        theme: 'grid',
        headStyles: { fillColor: [234, 88, 12] }
    })
    doc.save(`Asistentes_${modalRecord.value?.activity_name}_${getLocalISODate()}.pdf`)
}
// --- END Modal ---

const selectedReport = ref('attendance') // 'attendance', 'activities', or 'events'
const attendanceRecords = ref([])
const activityRecords = ref([])
const eventRecords = ref([])

const filters = ref({
    start_date: '',
    end_date: '',
    start_time: '',
    end_time: ''
})

const currentRecords = computed(() => {
    if (selectedReport.value === 'attendance') return attendanceRecords.value
    if (selectedReport.value === 'activities') return activityRecords.value
    return eventRecords.value
})

// Reset results when switching report type, require a new search
watch(selectedReport, () => {
    hasSearched.value = false
    attendanceRecords.value = []
    activityRecords.value = []
    eventRecords.value = []
    filters.value.start_time = ''
    filters.value.end_time = ''
})

const fetchReport = async () => {
    if (!filters.value.start_date && !filters.value.end_date) return
    loading.value = true
    hasSearched.value = true
    try {
        const params = new URLSearchParams()
        if (filters.value.start_date) params.append('start_date', filters.value.start_date)
        if (filters.value.end_date) params.append('end_date', filters.value.end_date)
        if (filters.value.start_time) params.append('start_time', filters.value.start_time)
        if (filters.value.end_time) params.append('end_time', filters.value.end_time)
        
        if (selectedReport.value === 'attendance') {
            const res = await apiClient.get(`reports/attendance/?${params.toString()}`)
            attendanceRecords.value = res.data
        } else if (selectedReport.value === 'activities') {
            const res = await apiClient.get(`reports/activity-attendance/?${params.toString()}`)
            activityRecords.value = res.data
        } else {
            const res = await apiClient.get(`reports/event-report/?${params.toString()}`)
            eventRecords.value = res.data
        }
    } catch (e) {
        console.error("Error fetching report", e)
    } finally {
        loading.value = false
    }
}

const getLocalISODate = (date = new Date()) => {
    const y = date.getFullYear();
    const m = String(date.getMonth() + 1).padStart(2, '0');
    const d = String(date.getDate()).padStart(2, '0');
    return `${y}-${m}-${d}`;
};

const setQuickFilter = (type) => {
    const today = new Date();
    
    let start, end;
    
    switch(type) {
        case 'hoy':
            start = end = today;
            break;
        case 'ayer':
            const yesterday = new Date(today);
            yesterday.setDate(today.getDate() - 1);
            start = end = yesterday;
            break;
        case 'semana': {
            // Monday = start of week (adjust: getDay() 0=Sun, so Mon = (getDay()+6)%7 days ago)
            const dayOfWeek = (today.getDay() + 6) % 7; // 0=Mon, 6=Sun
            start = new Date(today);
            start.setDate(today.getDate() - dayOfWeek);
            end = today;
            break;
        }
        case 'semana_pasada': {
            const dayOfWeek2 = (today.getDay() + 6) % 7;
            end = new Date(today);
            end.setDate(today.getDate() - dayOfWeek2 - 1); // Last Sunday
            start = new Date(end);
            start.setDate(end.getDate() - 6); // Last Monday
            break;
        }
        case 'mes':
            start = new Date(today.getFullYear(), today.getMonth(), 1);
            end = today;
            break;
        case 'mes_pasado':
            start = new Date(today.getFullYear(), today.getMonth() - 1, 1);
            end = new Date(today.getFullYear(), today.getMonth(), 0);
            break;
    }
    
    filters.value.start_date = getLocalISODate(start);
    filters.value.end_date = getLocalISODate(end);
    fetchReport();
}

const exportToExcel = () => {
    let ws;
    if (selectedReport.value === 'attendance') {
        ws = XLSX.utils.json_to_sheet(attendanceRecords.value.map(r => ({
            'Fecha': r.date,
            'Hora': r.time,
            'Usuario': r.beneficiary_name,
            'Cédula': r.beneficiary_ci,
            'Actividad': r.activity_name,
            'Evento': r.event_name
        })))
    } else {
        ws = XLSX.utils.json_to_sheet(activityRecords.value.map(r => ({
            'Actividad': r.activity_name,
            'Evento': r.event_name,
            'Nº de Asistentes Únicos': r.attendees
        })))
    }
    
    const wb = XLSX.utils.book_new()
    XLSX.utils.book_append_sheet(wb, ws, "Reporte")
    
    const filename = selectedReport.value === 'attendance' ? 'Reporte_Asistencia_Diaria_' : 'Reporte_Actividades_'
    XLSX.writeFile(wb, `${filename}${getLocalISODate()}.xlsx`)
}

const exportToPDF = () => {
    const doc = new jsPDF()
    
    let title = "Reporte - Centro Juvenil Las Mañanitas"
    let head = []
    let bodyData = []
    
    if (selectedReport.value === 'attendance') {
        title = "Reporte de Asistencia Diaria"
        head = [['Fecha', 'Hora', 'Usuario', 'Cédula', 'Actividad', 'Evento']]
        bodyData = attendanceRecords.value.map(r => [
            r.date, r.time, r.beneficiary_name, r.beneficiary_ci, r.activity_name, r.event_name
        ])
    } else {
        title = "Reporte de Actividades más Visitadas"
        head = [['Actividad', 'Evento / Detalles', 'Asistentes Únicos']]
        bodyData = activityRecords.value.map(r => [
            r.activity_name, r.event_name, r.attendees
        ])
    }
    
    doc.text(title, 14, 15)
    
    autoTable(doc, {
        head: head,
        body: bodyData,
        startY: 25,
        theme: 'grid',
        headStyles: { fillColor: [234, 88, 12] } // Orange-600
    })
    
    const filename = selectedReport.value === 'attendance' ? 'Asistencia_Diaria_' : 'Actividades_Top_'
    doc.save(`${filename}${getLocalISODate()}.pdf`)
}

onMounted(() => {
    // Don't auto-load: require user to apply a filter first
})

</script>

<style scoped>
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}
.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(15px);
}
</style>
