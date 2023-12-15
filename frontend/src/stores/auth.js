import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAuthStore = defineStore('auth', () => {
  const access = ref(localStorage.getItem('access'));
  const refresh = ref(localStorage.getItem('refresh'));

  const setTokens = (access, refresh) => {
    localStorage.setItem('access', access);
    localStorage.setItem('refresh', refresh);
  };

  return { setTokens };
});
