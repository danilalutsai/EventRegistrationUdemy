<script setup lang="ts">
import BaseCard from './BaseCard.vue';
import ButtonEvent from './ButtonEvent.vue';
import type { EventDetails } from '../EventTypes';

defineProps<EventDetails>();
defineEmits(['register', 'delete']);
</script>

<template>
  <!-- Fills the grid cell on narrow screens, capped so it stays readable on wide ones. -->
  <BaseCard class="w-full max-w-xl text-gray-500">
    <h3 class="p-4 text-gray-600 font-medium text-xl border-b border-gray-200">{{ title }}</h3>
    <p class="p-4 pb-0">{{ description }}</p>
    <p class="px-4 pb-4 pt-4 text-gray-400 border-b border-gray-200">{{ when }}</p>
    <!-- justify-between puts delete on the left edge and register on the right. -->
    <div class="flex flex-wrap items-center justify-between gap-3 p-4">
      <button
        class="cursor-pointer rounded border border-red-200 bg-red-50 px-3 py-1 text-sm font-medium text-red-700 transition duration-100 ease-in-out hover:border-red-300 hover:bg-red-100"
        @click="$emit('delete')"
      >delete</button>
      <ButtonEvent @click="$emit('register')">register</ButtonEvent>
    </div>
  </BaseCard>
</template>

<style scoped>
</style>
