<script setup lang="ts">
interface Props {
  title: string;
  when: string;
  description?: string;
}

defineProps<Props>();

</script>

<template>
  <div class="w-xl border border-gray-200 bg-white rounded-md shadow-sm">
    <h3 class="p-4 font-medium text-xl border-b border-gray-200">{{ title }} </h3>
    <p class="p-4 border-b border-gray-200">{{ when }}</p>
    <p class="p-4">{{ description }}</p>
    <button class="text-sm font-medium border border-gray-400 rounded-full px-3 py-1">Register</button>
  </div>
</template>
