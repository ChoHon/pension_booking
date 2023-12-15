import { defineStore } from 'pinia';
import { ref } from 'vue';
import http from '@/services/http';

export const useAuthStore = defineStore('auth', () => {
  const access = ref(localStorage.getItem('access'));
  const refresh = ref(localStorage.getItem('refresh'));

  const setTokens = (access, refresh) => {
    localStorage.setItem('access', access);
    localStorage.setItem('refresh', refresh);
  };

  const checkToken = async () => {
    try {
      const response = await http.post('/accounts/verify/', {
        token: access.value,
      });
      return true;
    } catch (error) {
      if (error.response.data.code !== 'token_not_valid') {
        return false;
      }
    }

    try {
      const response = await http.post('/accounts/refresh/', {
        refresh: refresh.value,
      });
      localStorage.setItem('access', response.data.access);
      return true;
    } catch (error) {
      return false;
    }
  };

  return { access, refresh, setTokens, checkToken };
});
