export interface EventDetails {
  title: string;
  when: string;
  description?: string;
  location?: string;
}

export interface EventItem extends EventDetails {
  id: number;
}

export interface NewBooking {
  id: string;
  userId: number;
  eventId: number;
  eventTitle: string;
}

export interface BookingItem extends NewBooking {
  status: string;
}
