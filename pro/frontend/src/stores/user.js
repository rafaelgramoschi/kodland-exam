// Utilities
import router from '@/router';
import { defineStore } from 'pinia'
import { reactive } from 'vue'

export const useUserStore = defineStore('user', () => {
  const session = reactive({
    // id: 1,
    id: localStorage.getItem('session_id'),
    score: localStorage.getItem('score'),
    reset: () => {
      localStorage.setItem('session_id', '')
      localStorage.setItem('score', '')
      session.id = null;
      session.score = null;
      router.push({ path: '/login' });
    }
  })

  return {
    session
  }
})
