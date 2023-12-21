<template>
  <!-- 헤더 -->
  <div
    class="border-b border-gray-200 pb-5 sm:flex sm:items-center sm:justify-between"
  >
    <h3 class="text-2xl font-semibold leading-6 text-gray-900">펜션</h3>
    <div class="mt-3 sm:ml-4 sm:mt-0">
      <button
        type="button"
        class="inline-flex items-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
        @click="is_pension_add_modal_open = true"
      >
        추가하기
      </button>
    </div>
  </div>

  <ul role="list" class="grid grid-cols-1 gap-x-6 gap-y-8 mt-5">
    <li
      v-for="pension in pensions"
      :key="pension.id"
      class="rounded-xl border border-gray-200"
    >
      <!-- 펜션 -->
      <div
        class="flex items-center gap-x-4 rounded-t-xl border-b border-gray-900/5 bg-gray-50 p-6"
      >
        <div class="min-w-0 flex-auto">
          <p class="text-2xl font-semibold leading-6 text-gray-900 mb-3">
            {{ pension.name }}
          </p>
          <p class="mt-1 truncate text-md leading-5 text-gray-500">
            {{ pension.address }}
          </p>
        </div>

        <Menu as="div" class="relative ml-auto">
          <MenuButton
            class="-m-2.5 z-10 block p-2.5 text-gray-400 hover:text-gray-500"
          >
            <EllipsisHorizontalIcon class="h-8 w-8" aria-hidden="true" />
          </MenuButton>
          <transition
            enter-active-class="transition ease-out duration-100"
            enter-from-class="transform opacity-0 scale-95"
            enter-to-class="transform opacity-100 scale-100"
            leave-active-class="transition ease-in duration-75"
            leave-from-class="transform opacity-100 scale-100"
            leave-to-class="transform opacity-0 scale-95"
          >
            <MenuItems
              class="absolute right-0 z-20 mt-0.5 w-32 origin-top-right divide-y divide-gray-100 rounded-md bg-white py-2 shadow-lg ring-1 ring-gray-900/5 focus:outline-none"
            >
              <div class="py-1">
                <MenuItem v-slot="{ active }">
                  <div
                    :class="[
                      active ? 'bg-gray-50' : '',
                      'block px-3 py-1 text-sm leading-6 text-gray-900 cursor-pointer',
                    ]"
                  >
                    방 추가
                  </div>
                </MenuItem>
                <MenuItem v-slot="{ active }">
                  <div
                    :class="[
                      active ? 'bg-gray-50' : '',
                      'block px-3 py-1 text-sm leading-6 text-gray-900 cursor-pointer',
                    ]"
                  >
                    방 삭제
                  </div>
                </MenuItem>
              </div>
              <div class="py-1">
                <MenuItem v-slot="{ active }">
                  <div
                    :class="[
                      active ? 'bg-gray-50' : '',
                      'block px-3 py-1 text-sm leading-6 text-gray-900 cursor-pointer',
                    ]"
                    @click="openPensionModModal(pension)"
                  >
                    수정
                  </div>
                </MenuItem>
                <MenuItem v-slot="{ active }">
                  <div
                    :class="[
                      active ? 'bg-gray-50' : '',
                      'block px-3 py-1 text-sm leading-6 text-gray-900 cursor-pointer',
                    ]"
                    @click="removePension(pension.id)"
                  >
                    삭제
                  </div>
                </MenuItem>
              </div>
            </MenuItems>
          </transition>
        </Menu>
      </div>

      <!-- 방 -->
      <dl class="-my-3 divide-y divide-gray-100 px-6 py-4 text-sm leading-6">
        <div
          v-for="room in pension.rooms"
          class="flex justify-between gap-x-4 py-3"
        >
          <dt class="text-gray-500">{{ room.name }}</dt>
          <dd class="text-gray-700">
            <div>{{ room.capacity }}인실 - {{ room.price_peak_season }}원</div>
          </dd>
        </div>
      </dl>
    </li>
  </ul>

  <BaseModal
    :is_open="is_pension_add_modal_open"
    @close="is_pension_add_modal_open = false"
  >
    <template #header>펜션 추가</template>
    <template #body>
      <form class="space-y-6">
        <div>
          <label
            for="name"
            class="block text-sm font-medium leading-6 text-gray-900"
          >
            이름
          </label>
          <div class="mt-2">
            <input
              v-model="new_pension.name"
              id="name"
              name="name"
              type="text"
              autocomplete="name"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label
              for="address"
              class="block text-sm font-medium leading-6 text-gray-900"
            >
              주소
            </label>
          </div>
          <div class="mt-2">
            <input
              v-model="new_pension.address"
              id="address"
              name="address"
              type="text"
              autocomplete="address"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>
      </form>
    </template>
    <template #buttons>
      <button
        type="button"
        class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 sm:col-start-2"
        @click="addPension"
      >
        추가
      </button>
      <button
        type="button"
        class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:col-start-1 sm:mt-0"
        @click="is_pension_add_modal_open = false"
      >
        취소
      </button>
    </template>
  </BaseModal>

  <BaseModal
    :is_open="is_pension_mod_modal_open"
    @close="is_pension_mod_modal_open = false"
  >
    <template #header>펜션 수정</template>
    <template #body>
      <form class="space-y-6">
        <div>
          <label
            for="name"
            class="block text-sm font-medium leading-6 text-gray-900"
          >
            이름
          </label>
          <div class="mt-2">
            <input
              v-model="new_pension.name"
              id="name"
              name="name"
              type="text"
              :placeholder="modalStore.target_pension.name"
              autocomplete="name"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label
              for="address"
              class="block text-sm font-medium leading-6 text-gray-900"
            >
              주소
            </label>
          </div>
          <div class="mt-2">
            <input
              v-model="new_pension.address"
              id="address"
              name="address"
              type="text"
              :placeholder="modalStore.target_pension.address"
              autocomplete="address"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>
      </form>
    </template>
    <template #buttons>
      <button
        type="button"
        class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 sm:col-start-2"
        @click="modifyPension"
      >
        수정
      </button>
      <button
        type="button"
        class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:col-start-1 sm:mt-0"
        @click="is_pension_mod_modal_open = false"
      >
        취소
      </button>
    </template>
  </BaseModal>
</template>

<script setup lang="ts">
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue';
import { EllipsisHorizontalIcon } from '@heroicons/vue/20/solid';
import { reactive, ref } from 'vue';
import router from '@/router';
import http from '@/services/http';
import { useAuthStore } from '@/stores/auth';
import { useModalStore } from '@/stores/modal';
import BaseModal from '@/components/BaseModal.vue';

const authStore = useAuthStore();
const modalStore = useModalStore();

const is_pension_add_modal_open = ref(false);
const is_pension_mod_modal_open = ref(false);

const openPensionModModal = pension => {
  is_pension_mod_modal_open.value = true;
  modalStore.setTargetPension(pension);
};

// 펜션 목록 불러오기
const pensions = ref([]);
http
  .get('/pensions', {
    headers: {
      Authorization: `Bearer ${authStore.access}`,
    },
  })
  .then(res => {
    pensions.value = res.data;
  })
  .catch(err => {
    alert('데이터를 불러오는데 실패했습니다.');
  });

// 펜션 추가
const new_pension = reactive({
  name: '',
  address: '',
});

const addPension = async () => {
  try {
    const response = await http.post('/pensions/', new_pension, {
      headers: {
        Authorization: `Bearer ${authStore.access}`,
      },
    });
    alert('펜션이 추가되었습니다.');
  } catch (error) {
    console.log(error.response.data);
  }

  router.go(0);
  return null;
};

// 펜션 수정
const modifyPension = async () => {
  try {
    const request = {};
    new_pension.name ? (request['name'] = new_pension.name) : null;
    new_pension.address ? (request['address'] = new_pension.address) : null;

    const response = await http.patch(
      `pensions/${modalStore.target_pension.id}/`,
      request,
      {
        headers: {
          Authorization: `Bearer ${authStore.access}`,
        },
      }
    );
    alert('펜션이 수정되었습니다.');
  } catch (error) {
    console.log(error.response.data);
  }

  router.go(0);
  return null;
};

// 펜션 삭제
const removePension = async (pension_id: number) => {
  try {
    const response = await http.delete(`/pensions/${pension_id}/`, {
      headers: {
        Authorization: `Bearer ${authStore.access}`,
      },
    });
    alert('펜션이 삭제되었습니다.');
  } catch (error) {
    console.log(error.response.data);
  }

  router.go(0);
  return null;
};
</script>

<style scoped></style>
