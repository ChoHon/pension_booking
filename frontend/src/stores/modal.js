import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useModalStore = defineStore('modal', () => {
  const target_pension = ref([]);

  const setTargetPension = input => {
    target_pension.value = input;
  };

  return { target_pension, setTargetPension };
});
