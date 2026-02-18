import { API_URL } from '@/constants/env';

// Helper to get token
function getToken() {
  return localStorage.getItem('jwt');
}

// Generic fetch wrapper for authenticated requests
export async function apiFetch(url: string, options: RequestInit = {}) {
  const token = getToken();
  const headers = {
    ...(options.headers || {}),
    ...(token ? { 'Authorization': `Bearer ${token}` } : {})
  };
  const res = await fetch(url, { ...options, headers });
  if (!res.ok) {
    const message = await res.text();
    // Throw an error object with status and message for better handling
    throw { status: res.status, message: message || 'API request failed' };
  }
  return res;
}

export async function getSecureData(): Promise<string> {
  const res = await apiFetch(`${API_URL}/secure`);
  return await res.text();
}
