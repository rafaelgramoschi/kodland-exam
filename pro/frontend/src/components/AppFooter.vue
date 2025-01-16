<script setup>
import { ref } from 'vue';
const name = ref()
name.value = "Gramoschi Rafael"
</script>

<template>
    <v-footer class="bg-black justify-center">
        Dev: [[ name ]]
    </v-footer>
</template>