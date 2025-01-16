<script setup>

const ranks = [
  { id: 1, username: 'rafa' , score: 100 },
  { id: 2, username: 'mario' , score: 50 },
  { id: 3, username: 'edo' , score: 20 },
]
</script>

<template>
  <v-container>
    <v-data-table :items="ranks">

    </v-data-table>
  </v-container>
</template>

