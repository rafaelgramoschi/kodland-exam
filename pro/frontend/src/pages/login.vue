<script setup>
import { reactive } from 'vue';

const loginForm = reactive({
  isValid: false,
  username: '',
  password: '',
  login: async () => {
    if(!loginForm.isValid) return false;
    
  }
})

const signupForm = reactive({
  isValid: false,
  username: '',
  password: '',
  repeatPassword: '',
  signup: async() => {
    if(!signupForm.isValid) return false;
  }
})
</script>

<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="6">
        <v-card class="text-center h-100">
          <v-form v-model="loginForm.isValid" @submit.prevent="loginForm.login()" class="d-flex flex-column h-100">
            <v-card-title>Login</v-card-title>
            <v-card-text class="mx-8">
              <v-text-field density="comfortable"
                label="Username"
                v-model="loginForm.username"
                :rules="[(v)=>!!v || 'obbligatorio']"
              ></v-text-field>
              <v-text-field density="comfortable"
                label="Password"
                v-model="loginForm.password"
                :rules="[(v)=>!!v || 'obbligatorio']"
              ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn type="submit">Login</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-form>
        </v-card> 
      </v-col>
      <v-col cols="12" sm="6">
        <v-card class="text-center">
          <v-form v-model="signupForm.isValid" @submit.prevent="signupForm.signup()">
            <v-card-title>Registrati</v-card-title>
            <v-card-text class="mx-8">
              <v-text-field density="comfortable"
                label="Username"
                v-model="signupForm.username"
                :rules="[(v)=>!!v || 'obbligatorio']"
              ></v-text-field>
              <v-text-field density="comfortable"
                label="Password" type="password"
                v-model="signupForm.password"
                :rules="[(v)=>!!v || 'obbligatorio']"
              ></v-text-field>
              <v-text-field density="comfortable"
                label="Ripeti Password" type="password"
                v-model="signupForm.repeatPassword"
                :rules="[(v)=> v==signupForm.password || 'Le password sono diverse']"
              ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn type="submit">Registrati</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
