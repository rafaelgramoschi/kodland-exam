<script setup>
import { useUserStore } from '@/stores/user';

const userStore = useUserStore();

const links = [
    { name: 'Home', icon: 'mdi-home' },
    { name: 'Quiz', icon: 'mdi-pencil-outline' },
    { name: 'Rank', icon: 'mdi-chevron-triple-up' },
    { name: 'Login/Signup', icon: 'mdi-login' },
];
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

        <v-tab v-if="userStore.session?.id"
          key="Quiz"
          text="Quiz"
          prepend-icon="mdi-pencil-outline"
          :to="{ path: '/quiz'}"
        ></v-tab>

        <v-tab v-if="userStore.session?.id"
          key="Rank"
          text="Rank"
          prepend-icon="mdi-chevron-triple-up"
          :to="{ path: '/rank'}"
        ></v-tab>

        <v-tab v-if="!userStore.session?.id"
          key="Login/Signup"
          text="Login/Signup"
          prepend-icon="mdi-login"
          :to="{ path: '/login'}"
        ></v-tab>
      </v-tabs>
      <v-spacer></v-spacer>

      <div v-if="userStore.session?.id">
        <span>[[ userStore.session.score ]]</span>
        <v-avatar
          class="hidden-sm-and-down"
          color="grey-darken-1"
          size="32"
          
        ><v-icon>mdi-professional-hexagon</v-icon>
          <v-menu activator="parent" class="ma-3 pa-3">
            <v-btn @click="userStore.session.reset();">Logout</v-btn>
          </v-menu>
        </v-avatar>
      </div>
    </v-app-bar>
</template>