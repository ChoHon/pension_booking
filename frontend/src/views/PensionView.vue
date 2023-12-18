<template>
  <div class="flex items-center justify-between mb-5">
    <h2 class="text-2xl font-semibold leading-7 text-gray-900">펜션 목록</h2>
  </div>
  <ul
    role="list"
    class="grid grid-cols-1 gap-x-6 gap-y-8 md:grid-cols-3 lg:gap-x-8"
  >
    <li
      v-for="pension in pensions"
      :key="pension.id"
      class="overflow-hidden rounded-xl border border-gray-200"
    >
      <!-- 헤더 -->
      <div
        class="flex items-center gap-x-4 border-b border-gray-900/5 bg-gray-50 p-6"
      >
        <img
          :src="'/no_img.jpg'"
          :alt="pension.name"
          class="h-12 w-12 flex-none rounded-lg bg-white object-none ring-1 ring-gray-900/10"
        />
        <div class="text-lg font-medium leading-6 text-gray-900">
          {{ pension.name }}
        </div>
      </div>

      <!-- 본문 -->
      <dl class="-my-3 divide-y divide-gray-100 px-6 py-4 text-md leading-6">
        <!-- 주소 -->
        <div class="flex justify-between gap-x-4 py-3">
          <dt class="text-gray-500">주소</dt>
          <dd class="text-gray-700">
            {{ pension.address }}
          </dd>
        </div>
      </dl>
    </li>
  </ul>
</template>

<script setup lang="ts">
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
  });
</script>

<style scoped></style>
