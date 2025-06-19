<!-- src/components/vue/FiltroAutores.vue -->
<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  items: {
    type: Array,
    default: () => []
  }
})

const query = ref('')
// Nueva reactividad para la inicial
const initial = ref('')

const resultados = computed(() =>
  props.items
    .filter(autor =>
      autor.data.name.toLowerCase().includes(query.value.toLowerCase())
    )
    .filter(autor =>
      // si no hay inicial seleccionada, todo pasa; si hay, chequea la primera letra
      !initial.value ||
      autor.data.name.charAt(0).toLowerCase() === initial.value.toLowerCase()
    )
)

function clear() {
  query.value = ''
  initial.value = ''
}
</script>

<template>
  <div class="p-4">
    <div class="flex gap-4 mb-4">
      <!-- Filtro de texto -->
      <input
        v-model="query"
        placeholder="Buscar autores…"
        class="flex-1 border p-2 rounded"
      />
      <!-- Nuevo filtro por inicial -->
      <select v-model="initial" class="border p-2 rounded">
        <option value="">Todas</option>
        <!-- Genera A–Z -->
        <option
          v-for="letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('')"
          :key="letra"
          :value="letra"
        >
          {{ letra }}
        </option>
      </select>
      <button @click="clear" class="text-sm">Limpiar</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
      <div v-for="autor in resultados" :key="autor.data.id">
        <a :href="`/autores/${autor.data.id}`">
          <article
            class="rounded-xl border shadow hover:shadow-lg transition bg-white overflow-hidden p-4 text-center"
          >
            <img
              v-if="autor.data.image"
              :src="autor.data.image"
              :alt="`Imagen de ${autor.data.name}`"
              class="w-full h-48 object-cover rounded-md mb-4"
            />
            <h2 class="text-lg font-semibold text-gray-900">
              {{ autor.data.name }}
            </h2>
          </article>
        </a>
      </div>
      <p v-if="resultados.length === 0" class="col-span-full text-center">
        No se encontró ningún autor.
      </p>
    </div>
  </div>
</template>
