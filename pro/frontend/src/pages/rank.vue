<script setup>
import { onMounted } from 'vue';


const ranks = ref([]);

onMounted(async()=> {
  const response = await fetch(`/ranks`);
  console.log("RESPONSE ranks:", response)
  const result = await response.json();
  console.log("JSON: ", result)
  ranks.value = result?.ranks;
});

</script>

<template>
  <v-container>
    <v-data-table :items="ranks">

    </v-data-table>
  </v-container>
</template>

