<script setup>
import router from '@/router';
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { reactive } from 'vue';

const userStore = useUserStore();

class Quiz {
  constructor(question, options, correctOptionIndex) {
    this.question = question;
    this.options = options;
    this.correctOptionIndex = correctOptionIndex;
  }
}

const exam = [
  new Quiz(
    "Cosa significa ML?", 
    ['Motivational Learning', 'Modern Learning', 'Mass Learning', 'Machine Learning',], 
    3
  ),
  new Quiz(
    "Quale linguaggio è comunemente usato per l'implementazione di algoritmi di ML?", 
    ['Java', 'C#', 'Python', 'Ruby'], 
    2
  ),
  new Quiz(
    "Cosa rappresenta un 'dataset' in ML?", 
    ['Un insieme di algoritmi', 'Un insieme di dati', 'Un modello di apprendimento', 'Un tipo di rete neurale'], 
    1
  ),
  new Quiz(
    "Qual è la differenza principale tra supervised e unsupervised learning?", 
    ['La quantità di dati', 'La presenza di etichette nei dati', 'La complessità degli algoritmi', 'Il tipo di modello'], 
    1
  ),
  new Quiz(
    "Quale libreria Python è molto utilizzata per il machine learning?", 
    ['Pandas', 'NumPy', 'Scikit-learn', 'Matplotlib'], 
    2
  ),
  new Quiz(
    "Cosa fa un algoritmo di regressione?", 
    ['Classifica i dati', 'Predice valori continui', 'Identifica cluster', 'Riduce la dimensionalità'], 
    1
  ),
  new Quiz(
    "Cosa rappresenta il termine 'overfitting'?", 
    ['Modello troppo semplice', 'Modello troppo complesso', 'Dati non sufficienti', 'Dati sbagliati'], 
    1
  ),
  new Quiz(
    "Quale metodo è usato per migliorare le prestazioni di un modello ML?", 
    ['Standardizzazione', 'Normalizzazione', 'Cross-validation', 'Tutte le precedenti'], 
    3
  ),
  new Quiz(
    "Cosa rappresenta una rete neurale?", 
    ['Un tipo di algoritmo di regressione', 'Un modello ispirato al cervello umano', 'Un metodo di clustering', 'Un dataset di immagini'], 
    1
  ),
  new Quiz(
    "Qual è una tecnica comune per la riduzione della dimensionalità?", 
    ['K-means', 'PCA', 'Decision Trees', 'Random Forests'], 
    1
  ),
  new Quiz(
    "Cosa significa 'feature' in un dataset?", 
    ['Un\'osservazione', 'Una variabile', 'Un\'istanza', 'Un modello'], 
    1
  ),
  new Quiz(
    "Cosa fa un algoritmo di clustering?", 
    ['Classifica i dati', 'Predice valori continui', 'Identifica gruppi simili nei dati', 'Riduce la dimensionalità'], 
    2
  ),
  new Quiz(
    "Quale di questi è un algoritmo di apprendimento supervisionato?", 
    ['K-means', 'SVM', 'PCA', 'DBSCAN'], 
    1
  ),
  new Quiz(
    "Cosa significa 'deep learning'?", 
    ['Apprendimento superficiale', 'Apprendimento tramite reti neurali profonde', 'Apprendimento senza dati', 'Apprendimento rapido'], 
    1
  ),
  new Quiz(
    "Qual è uno degli scopi principali del pre-processing dei dati?", 
    ['Aumentare la dimensione del dataset', 'Ridurre il rumore e migliorare la qualità dei dati', 'Creare nuovi algoritmi', 'Aumentare la complessità del modello'], 
    1
  ),
  new Quiz(
    "Cosa si intende per 'bias' in un modello ML?", 
    ['Errore sistematico', 'Errore casuale', 'Dati non rappresentativi', 'Sovraccarico di dati'], 
    0
  ),
  new Quiz(
    "Quale libreria è nota per l'implementazione di reti neurali in Python?", 
    ['Scikit-learn', 'TensorFlow', 'Pandas', 'Matplotlib'], 
    1
  ),
  new Quiz(
    "Cosa significa 'reinforcement learning'?", 
    ['Apprendimento tramite supervisione', 'Apprendimento tramite tentativi ed errori', 'Apprendimento senza dati', 'Apprendimento supervisionato'], 
    1
  ),
  new Quiz(
    "Qual è uno degli utilizzi comuni del machine learning?", 
    ['Calcolo delle radici quadrate', 'Riconoscimento facciale', 'Amministrazione di database', 'Scrittura di codice'], 
    1
  ),
];

async function saveScore() {
  const res = await axios.post(`/score`, {
    id: userStore.session.id,
    score: userStore.session.score
  });
  const result = await res.json();
  console.log(result)
}

const explorer = reactive({
  showScore: false,
  index: 0,
  done: 1,
  score: 0,
  question: null,
  options: [],
  correctOptionIndex: null,
  userChoice: null,
  next: async () => {
    if (explorer.done < exam.length) {
      if (explorer.index < exam.length) {
        explorer.index += 1;
      } else {
        explorer.index = 0;
      }
      explorer.done += 1;
      explorer.userChoice = null;
      explorer.question = exam[explorer.index].question
      explorer.options = exam[explorer.index].options
      explorer.correctOptionIndex = exam[explorer.index].correctOptionIndex
    } else {
      userStore.session.score += explorer.score;
      explorer.showScore = true;
      console.log("fatti tutti")
      await saveScore();
    }
  },
  check: async () => {
    if (explorer.userChoice == explorer.correctOptionIndex) {
      explorer.score += 10;
      console.log("Corretto!")
    } else {
      console.log("tu hai detto: ", explorer.options[explorer.userChoice])
      console.log("Sbagliato, la risposta corretta: ", explorer.options[explorer.correctOptionIndex])
    }
    await explorer.next();
  }
});

explorer.index = Math.ceil(Math.random() * (exam.length-1))
explorer.question = exam[explorer.index].question
explorer.options = exam[explorer.index].options
explorer.correctOptionIndex = exam[explorer.index].correctOptionIndex
</script>

<template>
  <v-container class="d-flex justify-center">
    <v-card v-if="!explorer.showScore" class="w-50">
      <v-card-title>Domanda [[explorer.done]]/[[exam.length]]</v-card-title>
      <v-card-text>
        <p>[[ explorer.question ]]</p>
        <v-radio-group v-model="explorer.userChoice">
          <v-radio v-for="option, i in explorer.options" :label="option" :value="i"></v-radio>
        </v-radio-group>
      </v-card-text>
      <v-card-actions>
        <v-btn @click="explorer.check()">Ok</v-btn>
      </v-card-actions>
    </v-card>
    <v-card else title="Punteggio Utente">
      <v-card-text class="text-error text-center">
        [[ explorer.score ]]/[[ exam.length*10 ]]
      </v-card-text>
    </v-card>
  </v-container>
</template>

