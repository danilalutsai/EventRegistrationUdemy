<script setup lang="ts">
import ButtonEvent from './ButtonEvent.vue';
import type { EventDetails } from '../EventTypes.ts';

defineProps<EventDetails>();
defineEmits(['register', 'delete']);

</script>

<template>
  <div class="w-xl text-gray-500 border border-gray-200 bg-white rounded-md shadow-sm shadow-gray-300">
    <h3 class="p-4 text-gray-600 font-medium text-xl border-b border-gray-200">{{ title }} </h3>
    <p class="p-4 pb-0">{{ description }}</p>
    <p class="px-4 pb-4 pt-4 text-gray-400 border-b border-gray-200">{{ when }}</p>
    <ButtonEvent class="register-button" @register="$emit('register')">Register</ButtonEvent>
    <button class="cursor-pointer rounded border border-red-200 bg-red-50 px-3 py-1 m-4 text-sm font-medium text-red-700 transition duration-100 ease-in-out hover:border-red-300 hover:bg-red-100" @click="$emit('delete')">Delete</button>
  </div>
</template>

<style scoped>
.register-button {
  transition: ease-in-out 0.1s;
}
</style>
