<script setup>
const links = [
    { name: 'Home', icon: 'mdi-home' },
    { name: 'Quiz', icon: 'mdi-pencil-outline' },
    { name: 'Rank', icon: 'mdi-chevron-triple-up' },
    { name: 'Login/Signup', icon: 'mdi-login' },
];

const userStore = { isLoggedin: false }
</script>

<template>
    <v-app-bar
      class="px-3"
      density="compact"
      flat
    >
      <v-avatar
        class="hidden-md-and-up"
        color="grey-darken-1"
        size="32"
      ></v-avatar>

      <v-spacer></v-spacer>

      <v-tabs
        color="grey-darken-2"
        centered
      >
        <v-tab
          key="Home"
          text="Home"
          prepend-icon="mdi-home"
          :to="{ path: '/'}"
        ></v-tab>

        <v-tab v-if="userStore.isLoggedin"
          key="Quiz"
          text="Quiz"
          prepend-icon="mdi-pencil-outline"
          :to="{ path: '/quiz'}"
        ></v-tab>

        <v-tab v-if="userStore.isLoggedin"
          key="Rank"
          text="Rank"
          prepend-icon="mdi-chevron-triple-up"
          :to="{ path: '/rank'}"
        ></v-tab>

        <v-tab
          key="Login/Signup"
          text="Login/Signup"
          prepend-icon="mdi-login"
          :to="{ path: '/login'}"
        ></v-tab>
      </v-tabs>
      <v-spacer></v-spacer>

      <v-avatar v-if="userStore.isLoggedin"
        class="hidden-sm-and-down"
        color="grey-darken-1"
        size="32"
      ></v-avatar>
    </v-app-bar>
</template>