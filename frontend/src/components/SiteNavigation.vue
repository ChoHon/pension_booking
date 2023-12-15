<template>
  <nav class="bg-gray-900 shadow-lg text-white">
    <div
      class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4"
    >
      <!-- 로고 -->
      <RouterLink
        :to="{
          name: 'home',
        }"
      >
        <div
          class="flex items-center space-x-3 rtl:space-x-reverse text-2xl cursor-pointer"
        >
          <i class="fa-solid fa-hotel" />
          <span class="self-center font-semibold whitespace-nowrap">
            펜션 관리
          </span>
        </div>
      </RouterLink>

      <!-- 버튼 -->
      <div
        class="flex md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse text-sm"
      >
        <!-- 로그인 -->
        <button
          type="button"
          class="focus:ring-4 focus:outline-none font-medium rounded-lg px-4 py-2 text-center bg-blue-600 hover:bg-blue-700 focus:ring-blue-800"
        >
          시작하기
        </button>

        <!-- 접힌 메뉴 -->
        <button
          data-collapse-toggle="navbar-cta"
          type="button"
          class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm rounded-lg md:hidden focus:outline-none focus:ring-2 text-gray-400 hover:bg-gray-700 focus:ring-gray-600"
          aria-controls="navbar-cta"
          aria-expanded="false"
        >
          <span class="sr-only">메뉴 열기</span>
          <i class="fa-solid fa-bars text-2xl"></i>
        </button>
      </div>

      <!-- 메뉴 -->
      <div
        class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1"
        id="navbar-cta"
      >
        <ul
          class="flex flex-col font-medium p-4 md:p-0 mt-4 border rounded-lg md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 bg-gray-800 md:bg-gray-900 border-gray-700"
        >
          <!-- 홈 -->
          <li>
            <div
              class="block py-2 px-3 md:p-0 rounded md:hover:text-blue-500 text-white hover:bg-gray-700 hover:text-white md:hover:bg-transparent border-gray-700 cursor-pointer"
            >
              홈
            </div>
          </li>

          <!-- 예시 -->
          <li>
            <a
              href="#"
              class="block py-2 px-3 md:p-0 rounded md:hover:text-blue-500 text-white hover:bg-gray-700 hover:text-white md:hover:bg-transparent border-gray-700 cursor-pointer"
              >예시</a
            >
          </li>
        </ul>
      </div>
    </div>

    <BaseModal>
      <div class="relative p-4 w-full max-w-md max-h-full">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow">
          <!-- Modal header -->
          <div
            class="flex items-center justify-between p-4 md:p-5 border-b rounded-t"
          >
            <h3 class="text-xl font-semibold text-gray-900">로그인</h3>

            <button
              type="button"
              class="end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center"
            >
              <i class="fa-solid fa-xmark text-2xl"></i>
              <span class="sr-only">닫기</span>
            </button>
          </div>

          <!-- Modal body -->
          <div class="p-4 md:p-5">
            <form class="space-y-4">
              <!-- 이메일 -->
              <div>
                <label
                  for="email"
                  class="block mb-2 text-md font-medium text-gray-900"
                >
                  이메일
                </label>
                <input
                  type="email"
                  name="email"
                  id="email"
                  v-model="user.email"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
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
                  type="password"
                  name="password"
                  id="password"
                  v-model="user.password"
                  placeholder="••••••••"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                  required
                />
              </div>

              <!-- 로그인 버튼 -->
              <button
                type="submit"
                class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-bold rounded-lg text-md px-5 py-2.5 text-center"
                @click.prevent="login"
              >
                로그인
              </button>

              <!-- 회원가입 -->
              <div class="text-sm font-medium text-gray-500">
                회원이 아니신가요?
                <span class="text-blue-700 hover:underline">회원가입</span>
              </div>
            </form>
          </div>
        </div>
      </div>
    </BaseModal>
  </nav>
</template>

<script setup>
import axios from 'axios';
import { reactive } from 'vue';
import { RouterLink } from 'vue-router';
import BaseModal from './BaseModal.vue';

const user = reactive({
  email: '',
  password: '',
});

const login = async () => {
  const response = await axios.post(
    'http://localhost:8000/accounts/login/',
    user
  );
  console.log(response.data);
};
</script>
