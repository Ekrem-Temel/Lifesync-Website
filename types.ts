import { LucideIcon } from 'lucide-react';

export interface Feature {
  title: string;
  description: string;
  icon: LucideIcon;
}

export interface NavLink {
  label: string;
  href: string;
}

export type Theme = 'light' | 'dark';