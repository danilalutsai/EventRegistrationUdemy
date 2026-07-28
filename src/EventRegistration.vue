<script setup lang="ts">
import EventCard from './components/EventCard.vue';

</script>

<template>
  <div class="min-h-screen">
    <main class="container mx-auto my-8 space-y-8 px-4">
      <h1 class="text-4xl font-medium">Event booking App</h1>
      <h2 class="text-2xl font-medium">All Events</h2>
      <!-- We can also iterate with numbers -->
      <section class="grid grid-cols-2 justify-items-center gap-8">
        <EventCard v-for="i in 8" :key="i" title="Vue conference 2026" when="2026-04-02" description="Conference about Vue and JavaScript"/>
      </section>
      <h2 class="text-2xl font-medium">Your bookings</h2>
    </main>
  </div>
</template>

<style scoped>
</style>
