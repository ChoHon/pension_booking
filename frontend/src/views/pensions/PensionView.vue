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
      >
        추가하기
      </button>
    </div>
  </div>

  <ul role="list" class="grid grid-cols-1 gap-x-6 gap-y-8 mt-5">
    <li
      v-for="pension in pensions"
      :key="pension.id"
      class="overflow-hidden rounded-xl border border-gray-200"
    >
      <!-- 펜션 -->
      <div
        class="flex items-center gap-x-4 border-b border-gray-900/5 bg-gray-50 p-6"
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
            class="-m-2.5 block p-2.5 text-gray-400 hover:text-gray-500"
          >
            <span class="sr-only">Open options</span>
            <EllipsisHorizontalIcon class="h-5 w-5" aria-hidden="true" />
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
              class="absolute right-0 z-10 mt-0.5 w-32 origin-top-right rounded-md bg-white py-2 shadow-lg ring-1 ring-gray-900/5 focus:outline-none"
            >
              <MenuItem v-slot="{ active }">
                <a
                  href="#"
                  :class="[
                    active ? 'bg-gray-50' : '',
                    'block px-3 py-1 text-sm leading-6 text-gray-900',
                  ]"
                >
                  View
                </a>
              </MenuItem>
              <MenuItem v-slot="{ active }">
                <a
                  href="#"
                  :class="[
                    active ? 'bg-gray-50' : '',
                    'block px-3 py-1 text-sm leading-6 text-gray-900',
                  ]"
                >
                  Edit
                </a>
              </MenuItem>
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
          {{ room.name }}
        </div>
        <div class="flex justify-between gap-x-4 py-3">
          <dt class="text-gray-500">주소</dt>
          <dd class="text-gray-700">
            {{ pension.address }}
          </dd>
        </div>
        <div class="flex justify-between gap-x-4 py-3">
          <dt class="text-gray-500">전화번호</dt>
          <dd class="flex items-start gap-x-2">
            <div class="font-medium text-gray-900">
              {{ pension.phone_number }}
            </div>
          </dd>
        </div>
      </dl>
    </li>
  </ul>
</template>

<script setup lang="ts">
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue';
import { EllipsisHorizontalIcon } from '@heroicons/vue/20/solid';
import http from '@/services/http';
import { useAuthStore } from '@/stores/auth';
import { ref } from 'vue';

const authStore = useAuthStore();
const pensions = ref({});

http
  .get('/pensions', {
    headers: {
      Authorization: `Bearer ${authStore.access}`,
    },
  })
  .then(res => {
    pensions.value = res.data;
    console.log(res.data);
  });
</script>

<style scoped></style>
