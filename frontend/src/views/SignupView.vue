<template>
  <div
    class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8"
  >
    <!-- 타이틀 -->
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <h2
        class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900"
      >
        회원가입
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
              v-model="new_user.email"
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
              v-model="new_user.password"
              id="password"
              name="password"
              type="password"
              autocomplete="current-password"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <!-- 비밀번호 확인 -->
        <div>
          <div class="flex items-center justify-between">
            <label
              for="confirm_password"
              class="block text-md font-medium leading-6 text-gray-900"
            >
              비밀번호 확인
            </label>
          </div>
          <div class="mt-2">
            <input
              v-model="new_user.confirm_password"
              id="confirm_password"
              name="confirm_password"
              type="password"
              autocomplete="current-confirm_password"
              required
              :class="[
                new_user.password === new_user.confirm_password ||
                new_user.confirm_password === ''
                  ? 'bg-white'
                  : 'bg-red-100',
                'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',
              ]"
            />
          </div>
        </div>

        <!-- 로그인 버튼 -->
        <div>
          <button
            type="button"
            class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
            @click="signup"
          >
            회원가입
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue';
import http from '@/services/http.js';
import router from '@/router';

const new_user = reactive({
  email: '',
  password: '',
  confirm_password: '',
});

const signup = async () => {
  try {
    const response = await http.post('/accounts/signup/', new_user);
    alert('회원가입이 완료되었습니다.');
    router.push('/login');

    return response;
  } catch (error) {
    console.log(error.response);
  }
};
</script>
