// Utilities
import router from '@/router';
import { defineStore } from 'pinia'
import { reactive } from 'vue'

export const useUserStore = defineStore('user', () => {
  const session = reactive({
    id: 1, // user_id
    score: null,
    reset: () => {
      session.id = null;
      session.score = null;
      router.push({ path: '/login' });
    }
  })

  return {
    session
  }
})
