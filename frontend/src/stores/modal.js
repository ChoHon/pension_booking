import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useModalStore = defineStore('modal', () => {
  const target_pension = ref([]);
  const target_room = ref([]);

  const setTargetPension = input => {
    target_pension.value = input;
  };

  const setTargetRoom = input => {
    target_room.value = input;
  };

  return { target_pension, target_room, setTargetPension, setTargetRoom };
});
