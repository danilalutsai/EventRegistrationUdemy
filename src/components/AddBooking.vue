<script setup lang="ts">
import { ref } from 'vue';
import type { EventDetails } from '../EventTypes';

const emit = defineEmits<{ add: [details: EventDetails] }>();

const newTitle = ref("");
const newDate = ref("");
const newDescription = ref("");

function submit(): void {
  if (newTitle.value.trim() === "") return;

  emit('add', {
    title: newTitle.value,
    when: newDate.value,
    description: newDescription.value,
  });

  newTitle.value = "";
  newDate.value = "";
  newDescription.value = "";
}

</script>

<template>
      <section>
        <h2 class="text-2xl font-medium pl-5">Add Event</h2>
        <!-- Spacing lives on the form (gap + pl-5), not on each child, so
             everything shares one left edge with the headings. -->
        <form @submit.prevent="submit" class="mt-3 flex flex-wrap items-center gap-3 pl-5">
          <input
            v-model="newTitle"
            type="text"
            name="title"
            placeholder="Add event title"
            class="w-full min-w-0 sm:w-auto sm:flex-1 rounded-md border border-gray-300 bg-white px-3 py-2 focus:border-blue-500 focus:outline-none"
          >
          <input
            v-model="newDate"
            type="date"
            placeholder="Add event date"
            name="when"
            class="w-full shrink-0 sm:w-44 rounded-md border border-gray-300 bg-white px-3 py-2 focus:border-blue-500 focus:outline-none"
          >
          <input
            v-model="newDescription"
            type="text"
            name="description"
            placeholder="Add event description"
            class="w-full min-w-0 sm:w-auto sm:flex-[2] rounded-md border border-gray-300 bg-white px-3 py-2 focus:border-blue-500 focus:outline-none"
          >
          <button
            type="submit"
            class="w-full shrink-0 sm:w-auto cursor-pointer rounded-md border border-blue-600 bg-blue-600 px-5 py-2 font-medium text-white transition duration-100 ease-in-out hover:border-blue-700 hover:bg-blue-700 active:translate-y-px"
          >
            Add
          </button>
        </form>
  </section>
</template>

<style>
</style>
