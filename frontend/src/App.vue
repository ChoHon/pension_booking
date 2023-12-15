<template>
  <div class="flex flex-col min-h-screen font-sans bg-gray-50">
    <SiteNavigation />
    <RouterView />
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router';
import SiteNavigation from './components/SiteNavigation.vue';
</script>

<style>
body {
  -ms-overflow-style: none;
}

::-webkit-scrollbar {
  display: none;
}
</style>
