<script setup>
import { onMounted } from 'vue';


const ranks = ref([]);

onMounted(async()=> {
  const response = await fetch(`/ranks`);
  const result = await response.json();
  ranks.value = result?.data?.ranks;
});

</script>

<template>
  <v-container>
    <v-data-table :items="ranks">

    </v-data-table>
  </v-container>
</template>

