export interface EventDetails {
  title: string;
  when: string;
  description?: string;
  location?: string;
}

export interface EventItem extends EventDetails {
  id: number;
}
