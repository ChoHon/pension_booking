<template>
  <div
    class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8"
  >
    <!-- 타이틀 -->
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <h2
        class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900"
      >
        로그인
      </h2>
    </div>

    <!-- 폼 -->
    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6">
        <!-- 이메일 -->
        <div>
          <label
            for="email"
            class="block text-md font-medium leading-6 text-gray-900"
          >
            이메일
          </label>
          <div class="mt-2">
            <input
              v-model="user.email"
              id="email"
              name="email"
              type="email"
              autocomplete="email"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <!-- 비밀번호 -->
        <div>
          <div class="flex items-center justify-between">
            <label
              for="password"
              class="block text-md font-medium leading-6 text-gray-900"
            >
              비밀번호
            </label>
            <!-- <div class="text-sm">
              <a
                href="#"
                class="font-semibold text-indigo-600 hover:text-indigo-500"
              >
                Forgot password?
              </a>
            </div> -->
          </div>
          <div class="mt-2">
            <input
              v-model="user.password"
              id="password"
              name="password"
              type="password"
              autocomplete="current-password"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <!-- 로그인 버튼 -->
        <div>
          <button
            type="button"
            class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
            @click="login"
          >
            로그인
          </button>
        </div>
      </form>

      <p class="mt-10 text-center text-md text-gray-500">
        아직 회원이 아니신가요?
        <RouterLink :to="{ name: 'signup' }">
          <span
            class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500"
          >
            회원가입
          </span>
        </RouterLink>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue';
import { RouterLink } from 'vue-router';
import router from '@/router';
import http from '@/services/http';
import { useAuthStore } from '@/stores/auth';

const authStore = useAuthStore();

const user = reactive({
  email: '',
  password: '',
});

const login = async () => {
  try {
    const response = await http.post('/accounts/login/', user);
    const { access, refresh } = response.data;

    authStore.setAccessToken(access);
    authStore.setRefreshToken(refresh);

    router.push({ name: 'home' });
    return response;
  } catch (error) {
    alert(error.response.data.detail);
  }
};
</script>
