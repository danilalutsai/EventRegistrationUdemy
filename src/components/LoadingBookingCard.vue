<script setup lang="ts">
import BaseCard from './BaseCard.vue';
</script>

<template>
  <BaseCard
    class="flex w-full flex-wrap items-center justify-between gap-4 px-4 py-3 bg-gray-100! animate-pulse"
    aria-hidden="true"
  >
    <div class="h-6 w-40 rounded bg-gray-300"></div>
    <div class="h-7.5 w-20 rounded bg-gray-300"></div>
  </BaseCard>
</template>
