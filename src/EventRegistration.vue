<script setup lang="ts">
import { ref, onMounted } from 'vue';

import EventCard from './components/EventCard.vue';
import LoadingEventCard from './components/LoadingEventCard.vue';
import LoadingBookingCard from './components/LoadingBookingCard.vue';
import BookingCard from './components/BookingCard.vue';
import AddBooking from './components/AddBooking.vue';

import type { EventItem, EventDetails, NewBooking, BookingItem } from './Types';

const events = ref<EventItem[]>([]);
const bookings = ref<BookingItem[]>([]);

const eventsLoading = ref(false);
const bookingsLoading = ref(false);

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

async function handleRegistration(event: EventItem) {
  const newBooking: NewBooking = {
    id: crypto.randomUUID(),
    userId: 1,
    eventId: event.id,
    eventTitle: event.title,
  };

  try {
    const response = await fetch('http://localhost:3001/bookings', {
      method: 'POST',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify({
        ...newBooking,
        status: 'confirmed',
      }),
    })

    if (!response.ok) {
      console.error(`The response status: ${response.status}`);
    }

    await fetchBookings()

  } catch (error: unknown) {

    const message = error instanceof Error ? error.message : String(error);
    throw new Error(`Failed to register: ${message}`);
  }

}

async function fetchBookings(): Promise<void> {
  bookingsLoading.value = true;

  try {
    const response = await fetch('http://localhost:3001/bookings');

    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    bookings.value = await response.json();
    console.log(bookings.value)

  } catch (error) {
    console.log(`Somethig went wrong ${error}`)

  } finally {
    bookingsLoading.value = false;
  }
}

async function cancelBooking(id: string): Promise<void> {
  try {
    const response = await fetch(`http://localhost:3001/bookings/${id}`, {
      method: 'DELETE',
    });

    if (!response.ok) {
      console.error(`The response status: ${response.status}`)
    }

    bookings.value = bookings.value.filter(booking => booking.id !== id);

  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.log(`Failed to cancel booking ${message}`)
  }
}


// We only start fetching data after our whole app mounts(loads) so we use onMounted
onMounted(() => {
  fetchEvents();
  fetchBookings();
});


function addEvent(details: EventDetails): void {
  events.value.push({ id: events.value.length + 1, ...details });
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
          @register="handleRegistration(event)"
        />
      </section>
        <AddBooking @add="addEvent" />
      <h2 class="text-2xl font-medium pl-5">Your bookings</h2>
      <!-- pl-5 matches the headings so the card's left edge lines up with them. -->
      <section class="grid gap-4 pl-5">
        <template v-if="bookingsLoading">
          <LoadingBookingCard v-for="i in 2" :key="`skeleton-${i}`" />
        </template>

        <template v-else>
          <p v-if="bookings.length === 0" class="text-gray-500">No bookings yet.</p>

          <BookingCard
            v-for="booking in bookings"
            :key="booking.id"
            :title="booking.eventTitle"
            @cancel="cancelBooking(booking.id)"
          />
        </template>
      </section>
    </main>
  </div>
</template>

<style scoped>
</style>
