<template>
  <header>
    <nav class="border-gray-200 px-4 lg:px-6 py-2.5 bg-gray-800 shadow-lg">
      <div
        class="flex flex-wrap justify-between items-center mx-auto max-w-screen-xl text-white"
      >
        <!-- 로고 -->
        <RouterLink :to="{ name: 'home' }">
          <div class="flex items-center">
            <i class="fa-solid fa-hotel px-2 text-xl"></i>
            <span class="self-center text-xl font-semibold whitespace-nowrap">
              펜션 관리
            </span>
          </div>
        </RouterLink>

        <div>
          <RouterLink :to="{ name: 'home' }">
            <span class="text-lg px-2 cursor-pointer hover:text-primary-400">
              홈
            </span>
          </RouterLink>

          <RouterLink :to="{ name: 'pension' }">
            <span class="text-lg px-2 cursor-pointer hover:text-primary-400">
              펜션
            </span>
          </RouterLink>
        </div>

        <div class="flex items-center lg:order-2">
          <!-- 로그인 -->
          <RouterLink :to="{ name: 'login' }">
            <div
              class="text-white focus:ring-4 font-medium rounded-lg text-md px-4 lg:px-5 py-2 lg:py-2.5 mr-2 hover:bg-gray-700 focus:outline-none focus:ring-gray-800 cursor-pointer"
            >
              로그인
            </div>
          </RouterLink>

          <!-- 회원가입 -->
          <RouterLink :to="{ name: 'signup' }">
            <div
              class="text-white focus:ring-4 font-medium rounded-lg text-md px-4 lg:px-5 py-2 lg:py-2.5 mr-2 bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-primary-800"
            >
              시작하기
            </div>
          </RouterLink>

          <!-- 모바일 메뉴 버튼 -->
          <!-- <button
            data-collapse-toggle="mobile-menu-2"
            type="button"
            class="inline-flex items-center p-2 ml-1 text-sm rounded-lg lg:hidden focus:outline-none focus:ring-2 text-gray-400 hover:bg-gray-700 focus:ring-gray-600"
            aria-controls="mobile-menu-2"
            aria-expanded="false"
          >
            <span class="sr-only">모바일 메뉴</span>
            <i class="fa-solid fa-bars text-xl w-6 h-6"></i>
          </button> -->
        </div>

        <!-- 모바일 메뉴 -->
        <!-- <div
          class="hidden justify-between items-center w-full lg:flex lg:w-auto lg:order-1"
          id="mobile-menu-2"
        >
          <ul
            class="flex flex-col mt-4 font-medium lg:flex-row lg:space-x-8 lg:mt-0"
          >
            <li>
              <a
                href="#"
                class="block py-2 pr-4 pl-3 text-white rounded bg-primary-700 lg:bg-transparent lg:text-primary-700 lg:p-0 dark:text-white"
                aria-current="page"
                >Home</a
              >
            </li>
            <li>
              <a
                href="#"
                class="block py-2 pr-4 pl-3 text-gray-700 border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-primary-700 lg:p-0 dark:text-gray-400 lg:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white lg:dark:hover:bg-transparent dark:border-gray-700"
                >Company</a
              >
            </li>
            <li>
              <a
                href="#"
                class="block py-2 pr-4 pl-3 text-gray-700 border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-primary-700 lg:p-0 dark:text-gray-400 lg:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white lg:dark:hover:bg-transparent dark:border-gray-700"
                >Marketplace</a
              >
            </li>
            <li>
              <a
                href="#"
                class="block py-2 pr-4 pl-3 text-gray-700 border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-primary-700 lg:p-0 dark:text-gray-400 lg:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white lg:dark:hover:bg-transparent dark:border-gray-700"
                >Features</a
              >
            </li>
            <li>
              <a
                href="#"
                class="block py-2 pr-4 pl-3 text-gray-700 border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-primary-700 lg:p-0 dark:text-gray-400 lg:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white lg:dark:hover:bg-transparent dark:border-gray-700"
                >Team</a
              >
            </li>
            <li>
              <a
                href="#"
                class="block py-2 pr-4 pl-3 text-gray-700 border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-primary-700 lg:p-0 dark:text-gray-400 lg:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white lg:dark:hover:bg-transparent dark:border-gray-700"
                >Contact</a
              >
            </li>
          </ul>
        </div> -->
      </div>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>
