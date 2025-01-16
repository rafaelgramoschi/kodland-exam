<script setup>
import WeatherCard from '@/components/WeatherCard.vue';
import { onMounted, reactive, ref } from 'vue';

/* Home page:
Un campo di immissione per il nome della città
Una tabella con le previsioni del tempo per 3 giorni (oggi, domani e dopodomani):
La pagina web dovrebbe fornire la data, compreso il nome del giorno (lunedì, martedì, ecc.)

La home page dovrebbe anche informare l'utente della temperatura diurna e di quella notturna.
*/
class DatePrinter {
  DAYS = {
    1: 'Lunedì',
    2: 'Martedì',
    3: 'Mercoledì',
    4: 'Giovedì',
    5: 'Venerdì',
    6: 'Sabato',
    7: 'Domenica',
  }
  constructor() {
    this.date = new Date()
    this.dayName = this.DAYS[this.date.getDay()]
    this.day = this.date.getDate()
    this.month = this.date.getMonth() + 1
    this.year = this.date.getFullYear()
  }

  print() {
    return `${this.dayName} ${this.day}.${this.month}.${this.year}`
  }
}

const datePrinter = new DatePrinter()
const city = ref("Roma")
const forecasting = reactive({
  yesterday: {
    date: '',
    weather: 'sole',
    temperature: {
      day: 9,
      night: 5,
    },
  },
  today: {
    date: '',
    weather: 'sole',
    temperature: {
      day: 14,
      night: 3,
    },
  },
  tomorrow: {
    date: '',
    weather: 'nebbia',
    temperature: {
      day: 11,
      night: 2,
    },
  },
});

function weatherCodeToString(code) {
  if (code == 1) return 'sole'
  if (9 <= code <= 22) return 'nuvole'
  if (23 <= code <= 28) return 'pioggia'
  if (29 <= code <= 35) return 'neve'
}

async function getCityLatLon() {
  let res = await fetch(`https://nominatim.openstreetmap.org/search.php?q=${city.value}&format=jsonv2`)
  res = await res.json()
  console.log("city lat lon:", res)
  const lat = res[0]?.lat
  const lon = res[0]?.lon
  return [lat, lon]
}

async function fetchForecast() {
  const [lat, lon] = await getCityLatLon()
  let res = await fetch(`https://my.meteoblue.com/packages/basic-day?apikey=gbAE1SpKPoIJ6qzG&lat=${lat}&lon=${lon}&format=json&history_days=1&forecast_days=2`)
  res = await res.json()
  
  forecasting.yesterday.weather = weatherCodeToString(res.data_day.pictocode[0])
  forecasting.yesterday.date = res.data_day.time[0]
  forecasting.yesterday.temperature.day = res.data_day.temperature_max[0]
  forecasting.yesterday.temperature.night = res.data_day.temperature_min[0]

  forecasting.today.weather = weatherCodeToString(res.data_day.pictocode[1])
  forecasting.today.date = res.data_day.time[1]
  forecasting.today.temperature.day = res.data_day.temperature_max[1]
  forecasting.today.temperature.night = res.data_day.temperature_min[1]

  forecasting.tomorrow.weather = weatherCodeToString(res.data_day.pictocode[2])
  forecasting.tomorrow.date = res.data_day.time[2]
  forecasting.tomorrow.temperature.day = res.data_day.temperature_max[2]
  forecasting.tomorrow.temperature.night = res.data_day.temperature_min[2]
}


onMounted(async() => {
  await fetchForecast()
  console.log(forecasting)
});
</script>

<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12" class="text-h3">Meteo</v-col>
      <v-col cols="12" class="text-h5">[[ datePrinter.print() ]]</v-col>
    </v-row>
    
    <v-row class="justify-center">
      <v-col cols="3">
        <v-text-field density="comfortable"
          v-model="city" variant="solo-filled"
          placeholder="Cerca il nome di una città..."
        ></v-text-field>
      </v-col>
      <v-col cols="1">
        <v-btn icon="mdi-magnify" @click="fetchForecast()"></v-btn>
      </v-col>
    </v-row>

    <v-row class="text-center align-center">
      <v-col cols="4">
        <WeatherCard
          title="Ieri"
          :subtitle="forecasting.yesterday.date"
          :weather="forecasting.yesterday.weather"
          :temp-day="forecasting.yesterday.temperature.day"
          :temp-night="forecasting.yesterday.temperature.night"
        ></WeatherCard>
      </v-col>
      <v-col cols="4">
        <WeatherCard
          :title="`${city} Oggi`"
          :subtitle="forecasting.today.date"
          :weather="forecasting.today.weather"
          :temp-day="forecasting.today.temperature.day"
          :temp-night="forecasting.today.temperature.night"
        ></WeatherCard>
      </v-col>
      <v-col cols="4">
        <WeatherCard
          title="Domani"
          :subtitle="forecasting.tomorrow.date"
          :weather="forecasting.tomorrow.weather"
          :temp-day="forecasting.tomorrow.temperature.day"
          :temp-night="forecasting.tomorrow.temperature.night"
        ></WeatherCard>
      </v-col>
    </v-row>
  </v-container>
</template>

