<script setup lang="ts">
import { ref, onMounted } from 'vue';

import EventCard from './components/EventCard.vue';
import LoadingEventCard from './components/LoadingEventCard.vue';
import BookingCard from './components/BookingCard.vue';
import AddBooking from './components/AddBooking.vue';

import type { EventItem, EventDetails } from './EventTypes';

const events = ref<EventItem[]>([]);
const bookings = ref<EventItem[]>([]);

const eventsLoading = ref(false);

async function fetchEvents(): Promise<void> {
  eventsLoading.value = true;

  try {
    const response = await fetch('http://localhost:3001/events');

    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    events.value = await response.json();

  } catch (error) {
    console.log(`Somethig went wrong ${error}`)

  } finally {
    eventsLoading.value = false;
  }
}

// We only start fetching data after our whole app mounts(loads) so we use onMounted
onMounted(() => {
  fetchEvents();
});


function addEvent(details: EventDetails): void {
  events.value.push({ id: events.value.length + 1, ...details });
}

function bookEvent(event: EventItem): void {
  // Ignore second click on the same card.
  if (bookings.value.some(b => b.id === event.id)) return;
  bookings.value.push(event);
}

function deleteEvent(id: number) {
  events.value = events.value.filter(event => event.id !== id);
}

function cancelBooking(id: number): void {
  bookings.value = bookings.value.filter(b => b.id !== id);
}
</script>

<template>
  <div class="min-h-screen">
    <main class="container mx-auto my-8 space-y-8 px-4">
      <h1 class="text-4xl font-medium pl-5">Event booking App</h1>
      <p v-if="!eventsLoading && events.length === 0" class="text-gray-500 ml-5">No events yet.</p>
      <!-- One column by default, two once there's room for both cards. -->
      <!-- Skeletons live in the same grid so nothing shifts when data lands. -->
      <section class="grid grid-cols-1 md:grid-cols-2 justify-items-center gap-8">
        <template v-if="eventsLoading">
          <LoadingEventCard v-for="i in 4" :key="`skeleton-${i}`" />
        </template>

        <EventCard
          v-else
          v-for="event in events"
          :key="event.id"
          :title="event.title"
          :when="event.when"
          :description="event.description"
          @register="bookEvent(event)"
          @delete="deleteEvent(event.id)"
        />
      </section>
        <AddBooking @add="addEvent" />
      <h2 class="text-2xl font-medium pl-5">Your bookings</h2>
      <!-- pl-5 matches the headings so the card's left edge lines up with them. -->
      <section class="grid gap-4 pl-5">
        <p v-if="bookings.length === 0" class="text-gray-500">No bookings yet.</p>

        <BookingCard
          v-for="booking in bookings"
          :key="booking.id"
          :title="booking.title"
          :when="booking.when"
          :description="booking.description"
          @cancel="cancelBooking(booking.id)"
        />
      </section>
    </main>
  </div>
</template>

<style scoped>
</style>
