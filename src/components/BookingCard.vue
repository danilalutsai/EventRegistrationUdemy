<script setup lang="ts">
import type { EventDetails } from '../EventTypes';

defineProps<EventDetails>();
defineEmits(['cancel']);
</script>

<template>
  <!-- justify-between pushes the name to the left edge and the button to the right. -->
    <div
      class="flex w-full items-center justify-between gap-4 rounded-md border border-gray-200 bg-white px-4 py-3 shadow-sm shadow-gray-300"
    >
    <p class="font-medium text-gray-900">{{ title }}</p>

      <button class="cursor-pointer rounded border border-red-200 bg-red-50 px-3 py-1 text-sm font-medium text-red-700 transition duration-100 ease-in-out hover:border-red-300 hover:bg-red-100" @click="$emit('cancel')">Cancel</button>
    </div>
</template>

<style scoped>
</style>
