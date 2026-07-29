<script setup lang="ts">
import BaseCard from './BaseCard.vue';
</script>

<template>
  <BaseCard class="w-full max-w-xl bg-gray-100! animate-pulse" aria-hidden="true">
    <div class="p-4 border-b border-gray-200">
      <div class="h-7 w-3/5 rounded bg-gray-300"></div>
    </div>
    <div class="p-4 pb-0 space-y-2">
      <div class="h-6 w-full rounded bg-gray-300"></div>
      <div class="h-6 w-4/5 rounded bg-gray-300"></div>
    </div>
    <div class="px-4 pb-4 pt-4 border-b border-gray-200">
      <div class="h-6 w-32 rounded bg-gray-300"></div>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-3 p-4">
      <div class="h-7.5 w-20 rounded bg-gray-300"></div>
      <div class="h-7.5 w-24 rounded bg-gray-300"></div>
    </div>
  </BaseCard>
</template>
