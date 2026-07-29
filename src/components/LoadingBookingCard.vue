<script setup lang="ts">
import BaseCard from './BaseCard.vue';
</script>

<template>
  <!-- Mirrors BookingCard's box: same flex layout and paddings,
       so the row doesn't shift when the real card arrives. -->
  <BaseCard
    class="flex w-full flex-wrap items-center justify-between gap-4 px-4 py-3 bg-gray-100! animate-pulse"
    aria-hidden="true"
  >
    <!-- h-6 = the title <p>'s text-base line-height. -->
    <div class="h-6 w-40 rounded bg-gray-300"></div>
    <!-- h-7.5 = Cancel button: text-sm (20px) + py-1 (8px) + border (2px). -->
    <div class="h-7.5 w-20 rounded bg-gray-300"></div>
  </BaseCard>
</template>
