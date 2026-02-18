import { API_URL } from '@/constants/env';

export async function register(email: string, password: string): Promise<string> {
  console.log('Registering with email:', email);
  console.log('API URL:', API_URL);
  const res = await fetch(`${API_URL}/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  });
  if (!res.ok) throw new Error('Registration failed');
  const token: string = await res.json();
  localStorage.setItem('jwt', token);
  return token;
}

export async function login(email: string, password: string): Promise<string> {
  const res = await fetch(`${API_URL}/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  });
  if (!res.ok) throw new Error('Login failed');
  const token: string = await res.json();
  localStorage.setItem('jwt', token);
  return token;
}

export function logout(): void {
  localStorage.removeItem('jwt');
}
