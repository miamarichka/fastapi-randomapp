import { API_URL } from '../config';
import type { User } from './types';

const USERS_ENDPOINT = `${API_URL}/users`;

export async function getUsers(): Promise<User[]> {
  try {
    const res = await fetch(`${USERS_ENDPOINT}/`);
    return res.json();
  } catch (error) {
    console.error('Error fetching users:', error);
    return [];
  }
}

export async function addRandomUser(): Promise<User> {
  try {
    const res = await fetch(`${USERS_ENDPOINT}/random/save`, { method: 'POST' });
    return res.json();
  } catch (error) {
    console.error('Error adding random user:', error);
    return {} as User;
  }
}