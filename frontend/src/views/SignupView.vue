<template>
  <section class="bg-gray-50">
    <div
      class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0"
    >
      <div
        class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0"
      >
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <!-- 헤더 -->
          <h1
            class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl"
          >
            회원가입
          </h1>

          <form class="space-y-4 md:space-y-6" action="#">
            <!-- 이메일 -->
            <div>
              <label
                for="email"
                class="block mb-2 text-md font-medium text-gray-900"
              >
                이메일
              </label>
              <input
                v-model="new_user.email"
                type="email"
                name="email"
                id="email"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"
                placeholder="name@company.com"
                required
              />
            </div>

            <!-- 비밀번호 -->
            <div>
              <label
                for="password"
                class="block mb-2 text-md font-medium text-gray-900"
              >
                비밀번호
              </label>
              <input
                v-model="new_user.password"
                type="password"
                name="password"
                id="password"
                placeholder="••••••••"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"
                required
              />
            </div>

            <!-- 비밀번호 확인 -->
            <div>
              <label
                for="confirm-password"
                class="block mb-2 text-md font-medium text-gray-900"
                >비밀번호 확인</label
              >
              <input
                v-model="new_user.confirm_password"
                type="password"
                name="confirm-password"
                id="confirm-password"
                placeholder="••••••••"
                :class="{
                  'bg-red-100':
                    new_user.password !== new_user.confirm_password &&
                    new_user.confirm_password.length > 0,
                }"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"
                required
              />
            </div>

            <!-- 회원가입 버튼 -->
            <button
              type="submit"
              class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-md px-5 py-2.5 text-center"
              @click.prevent="signup"
            >
              회원가입
            </button>

            <!-- 로그인 화면 이동 -->
            <p class="text-sm font-light text-gray-500">
              이미 회원이신가요?
              <RouterLink :to="{ name: 'login' }">
                <span
                  class="font-medium text-primary-600 hover:underline cursor-pointer"
                >
                  로그인
                </span>
              </RouterLink>
            </p>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { reactive } from 'vue';
import http from '@/services/http.js';

const new_user = reactive({
  email: '',
  password: '',
  confirm_password: '',
});

const signup = () => {
  const response = http
    .post('/accounts/signup/', new_user)
    .then(res => {
      console.log(res.data);
    })
    .catch(err => {
      console.log(err.response.data);
    });
  return response;
};
</script>

<style scoped></style>
