<script setup lang="ts">
import type { EventDetails } from '../EventTypes';
import BaseCard from './BaseCard.vue';

defineProps<Partial<EventDetails> & { loading?: boolean }>();
defineEmits(['cancel']);
</script>

<template>
  <BaseCard class="flex w-full flex-wrap items-center justify-between gap-4 px-4 py-3">
    <p class="font-medium text-gray-900">{{ title }}</p>
    <button class="cursor-pointer rounded border border-red-200 bg-red-50 px-3 py-1 text-sm font-medium text-red-700 transition duration-100 ease-in-out hover:border-red-300 hover:bg-red-100" @click="$emit('cancel')">Cancel</button>
  </BaseCard>
</template>

<style scoped>
</style>
