<template>
  <Disclosure as="nav" class="bg-gray-800" v-slot="{ open }">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="relative flex h-16 items-center justify-between">
        <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
          <!-- 모바일 메뉴 버튼 -->
          <DisclosureButton
            class="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
          >
            <span class="absolute -inset-0.5" />
            <span class="sr-only">Open main menu</span>
            <Bars3Icon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
            <XMarkIcon v-else class="block h-6 w-6" aria-hidden="true" />
          </DisclosureButton>
        </div>
        <div
          class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start"
        >
          <!-- 로고 -->
          <div class="flex flex-shrink-0 items-center">
            <i class="fa-solid fa-hotel text-white text-2xl"></i>
          </div>

          <!-- 메인 메뉴 -->
          <div class="hidden sm:ml-6 sm:block">
            <div class="flex space-x-4">
              <div
                v-for="item in navigation"
                :key="item.name"
                :class="[
                  item.current
                    ? 'bg-gray-900 text-white'
                    : 'text-gray-300 hover:bg-gray-700 hover:text-white',
                  'rounded-md px-3 py-2 text-md font-medium cursor-pointer',
                ]"
                :aria-current="item.current ? 'page' : undefined"
              >
                <RouterLink :to="{ name: item.router }">{{
                  item.name
                }}</RouterLink>
              </div>
            </div>
          </div>
        </div>

        <div
          class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0"
        >
          <!-- 로그인 버튼 -->
          <RouterLink v-if="!authStore.login_status" :to="{ name: 'login' }">
            <button
              type="button"
              class="inline-flex items-center rounded-md bg-blue-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-blue-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-300"
            >
              시작하기
            </button>
          </RouterLink>

          <!-- 유저 메뉴 -->
          <Menu v-if="authStore.login_status" as="div" class="relative ml-3">
            <div>
              <MenuButton
                class="relative flex rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800"
              >
                <span class="absolute -inset-1.5" />
                <span class="sr-only">Open user menu</span>
                <img
                  class="h-8 w-8 rounded-full bg-white"
                  src="/user.png"
                  alt=""
                />
              </MenuButton>
            </div>

            <transition
              enter-active-class="transition ease-out duration-100"
              enter-from-class="transform opacity-0 scale-95"
              enter-to-class="transform opacity-100 scale-100"
              leave-active-class="transition ease-in duration-75"
              leave-from-class="transform opacity-100 scale-100"
              leave-to-class="transform opacity-0 scale-95"
            >
              <MenuItems
                class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
              >
                <MenuItem v-slot="{ active }">
                  <div
                    :class="[
                      active ? 'bg-gray-100' : '',
                      'block px-4 py-2 text-sm text-gray-700',
                    ]"
                    @click="logout"
                  >
                    로그아웃
                  </div>
                </MenuItem>
              </MenuItems>
            </transition>
          </Menu>
        </div>
      </div>
    </div>

    <!-- 모바일 메뉴 -->
    <DisclosurePanel class="sm:hidden">
      <div class="space-y-1 px-2 pb-3 pt-2">
        <DisclosureButton
          v-for="item in navigation"
          :key="item.name"
          as="a"
          :class="[
            item.current
              ? 'bg-gray-900 text-white'
              : 'text-gray-300 hover:bg-gray-700 hover:text-white',
            'block rounded-md px-3 py-2 text-md font-medium cursor-pointer',
          ]"
          :aria-current="item.current ? 'page' : undefined"
        >
          <RouterLink :to="{ name: item.router }">{{ item.name }}</RouterLink>
        </DisclosureButton>
      </div>
    </DisclosurePanel>
  </Disclosure>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth';
import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
} from '@headlessui/vue';
import { Bars3Icon, XMarkIcon } from '@heroicons/vue/24/outline';
import http from '@/services/http';
import router from '@/router';

const authStore = useAuthStore();

const navigation = [
  { name: '홈', router: 'home', current: false },
  { name: '펜션', router: 'pension', current: false },
  { name: '예약', router: 'reservation', current: false },
];

const logout = async () => {
  const token_state = await authStore.checkToken();

  if (token_state) {
    const response = await http.post(
      '/accounts/logout/',
      { refresh: authStore.refresh },
      {
        headers: { Authorization: `Bearer ${authStore.access}` },
      }
    );

    authStore.removeTokens();
  }

  authStore.login_status = false;
  router.push({ name: 'home' });
};
</script>
