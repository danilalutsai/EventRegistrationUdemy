export interface EventDetails {
  title: string;
  when: string;
  description?: string;
}

export interface EventItem extends EventDetails {
  id: number;
}
