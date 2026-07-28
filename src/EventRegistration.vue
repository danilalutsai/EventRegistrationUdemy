<script setup lang="ts">
import { ref } from 'vue';

import EventCard from './components/EventCard.vue';
import BookingCard from './components/BookingCard.vue';
import AddBooking from './components/AddBooking.vue';

import type { EventItem, EventDetails } from './EventTypes';

const bookings = ref<EventItem[]>([]);

let eventsDetails: EventDetails[] = ([
  {
    title: "Rails conference 2024",
    when: "2024-04-20",
    description: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, ",
  },
  {
    title: "Vue presentation 2026",
    when: "2026-07-25",
    description: "Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets. It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged. ",
  },
  {
    title: "TypeScript conference 2020",
    when: "2020-01-18",
    description: "It was popularised thanks to these sheets and more recently with desktop publishing software like Aldus PageMaker and Microsoft Word including versions of Lorem Ipsum.",
  },
  {
    title: "JavaScript presentation 2022",
    when: "2022-02-28",
    description: "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum",
  },
  {
    title: "Python Crash Course 2023",
    when: "2023-04-18",
    description: "Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32.",
  },
  {
    title: "Rust Mega Course 2026",
    when: "2026-12-08",
    description: "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. ",
  },
]);

const events = ref<EventItem[]>(
  eventsDetails.map((details, index) => ({ id: index + 1, ...details }))
);

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
      <h2 class="text-2xl font-medium pl-5">All Events</h2>
      <p v-if="events.length === 0" class="text-gray-500 ml-5">No events yet.</p>
      <section class="grid grid-cols-2 justify-items-center gap-8">
        <EventCard 
          v-for="event in events" 
          :key="event.id" 
          :id="event.id" 
          :title="event.title" 
          :when="event.when" 
          :description="event.description" 
          @register="bookEvent(event)";
          @delete="deleteEvent(event.id)"
          " />
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
