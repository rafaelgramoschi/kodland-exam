<script setup>
const props = defineProps(['title', 'subtitle', 'weather', 'tempDay', 'tempNight'])
const weatherTypes = {
    sunny: 'mdi-weather-sunny',
    cloudy: 'mdi-weather-cloudy',
    foggy: 'mdi-weather-fog',
    rainy: 'mdi-weather-pouring',
    snowy: 'mdi-weather-snowy',
}
</script>

<template>
    <v-card :title="title" :subtitle="subtitle" min-height="250" class="align-content-center">
        <v-card-text>
        <v-row align="center" no-gutters>
            <v-col
            class="text-h4"
            cols="5"
            >
            [[ weather ]]
            </v-col>

            <v-col class="text-right" cols="7">
            <v-icon
                color="white"
                :icon="weatherTypes[weather]"
                size="90"
            ></v-icon>
                <v-row>
                    <v-col cols="6">
                        <v-icon color="yellow">mdi-sun-clock</v-icon>
                        [[ tempDay ]] °C
                    </v-col>
                    <v-col cols="6">
                        <v-icon color="blue">mdi-weather-night</v-icon>
                        [[ tempNight ]] °C
                    </v-col>
                </v-row>
            </v-col>
        </v-row>
        </v-card-text>
    </v-card>
</template>