import { API_URL } from '@/constants/env';

export async function getSecureData(): Promise<string> {
  const token = localStorage.getItem('jwt');
  if (!token) throw new Error('No token found');
  const res = await fetch(`${API_URL}/secure`, {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
  if (!res.ok) throw new Error('Unauthorized');
  return await res.text();
}
