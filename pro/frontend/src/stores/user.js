// Utilities
import { defineStore } from 'pinia'
import { reactive } from 'vue'

export const useUserStore = defineStore('user', () => {
  const session = reactive({
    id: '', // user_id
    score: 0,
  })

  return {
    session
  }
})
