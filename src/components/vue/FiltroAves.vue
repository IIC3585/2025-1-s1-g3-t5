<!-- src/components/vue/FiltroAves.vue -->
<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  items: {
    type: Array,
    default: () => []
  }
});

const query = ref('');
const initial = ref('');


const resultados = computed(() =>
  props.items
    .filter(ave =>
      ave.data.spanishName
        .toLowerCase()
        .includes(query.value.toLowerCase())
    )
    .filter(ave =>
      !initial.value ||
      ave.data.spanishName.charAt(0).toLowerCase() === initial.value.toLowerCase()
    )
);

function clear() {
  query.value = '';
  initial.value = '';
}
</script>

<template>
  <div class="p-4">
    <div class="flex gap-4 mb-4">
      <!-- Filtro de texto -->
      <input
        v-model="query"
        placeholder="Buscar aves…"
        class="flex-1 border p-2 rounded"
      />
      <!-- Filtro por inicial A–Z -->
      <select v-model="initial" class="border p-2 rounded">
        <option value="">Todas</option>
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
      <div v-for="ave in resultados" :key="ave.data.uid">
        <a :href="`/aves/${ave.data.uid}`">
          <article
            class="rounded-xl border shadow hover:shadow-lg transition bg-white overflow-hidden p-4 text-center"
          >
            <img
              v-if="ave.data.image"
              :src="ave.data.image"
              :alt="`Imagen de ${ave.data.spanishName}`"
              class="w-full h-48 object-cover rounded-md mb-4"
            />
            <h2 class="text-lg font-semibold text-gray-900">
              {{ ave.data.spanishName }}
            </h2>
          </article>
        </a>
      </div>
      <p v-if="resultados.length === 0" class="col-span-full text-center">
        No se encontró ninguna ave.
      </p>
    </div>
  </div>
</template>
