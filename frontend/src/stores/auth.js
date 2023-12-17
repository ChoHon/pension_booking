import { defineStore } from 'pinia';
import { ref } from 'vue';
import http from '@/services/http';

export const useAuthStore = defineStore('auth', () => {
  const access = ref(localStorage.getItem('access'));
  const refresh = ref(localStorage.getItem('refresh'));
  const login_status = ref(false);

  const setAccessToken = new_access => {
    localStorage.setItem('access', new_access);
    access.value = new_access;
  };

  const setRefreshToken = new_refresh => {
    localStorage.setItem('refresh', new_refresh);
    refresh.value = new_refresh;
  };

  const removeTokens = () => {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    access.value = null;
    refresh.value = null;
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
      setAccessToken(response.data.access);
      return true;
    } catch (error) {
      return false;
    }
  };

  return {
    access,
    refresh,
    login_status,
    setAccessToken,
    setRefreshToken,
    removeTokens,
    checkToken,
  };
});
