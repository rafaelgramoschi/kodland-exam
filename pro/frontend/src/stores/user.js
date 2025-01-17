// Utilities
import router from '@/router';
import { defineStore } from 'pinia'
import { reactive } from 'vue'

export const useUserStore = defineStore('user', () => {
  const session = reactive({
    // id: 1,
    id: parseInt(localStorage.getItem('session_id')) || 0,
    score: parseInt(localStorage.getItem('score')) || 0,
    reset: () => {
      localStorage.removeItem('session_id')
      localStorage.removeItem('score')
      session.id = null;
      session.score = null;
      router.push({ path: '/login' });
    }
  })

  return {
    session
  }
})
