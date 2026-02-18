<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getSecureData } from '@/utils/api'
import { useRouter } from 'vue-router'
const router = useRouter()

const secureMessage = ref('')
const secureError = ref('')

onMounted(async () => {
  try {
    secureMessage.value = await getSecureData()
  } catch (e: any) {
    secureError.value = e?.message || 'Failed to fetch secure data.'
  }
})

const logout = () => {
  localStorage.removeItem('token')
  router.push('/login')
}
</script>

<template>
  <div class="flex min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
    <aside class="w-64 bg-white shadow-2xl p-7 flex flex-col items-center space-y-8 rounded-tr-3xl rounded-br-3xl">
      <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" alt="Logo" class="w-14 h-14 mb-2" />
      <h2 class="text-2xl font-extrabold text-blue-700 tracking-wide mb-6">Assistant</h2>

      <nav class="flex flex-col gap-3 w-full">
        <router-link to="/" class="flex items-center gap-2 px-4 py-2 rounded-lg text-blue-700 font-medium hover:bg-blue-50 transition">
          <span class="text-xl">💬</span> Chat
        </router-link>
        <router-link to="/image-generation" class="flex items-center gap-2 px-4 py-2 rounded-lg text-blue-700 font-medium hover:bg-blue-50 transition">
          <span class="text-xl">🖼️</span> Image Generation
        </router-link>
        <router-link to="/image-segmentation" class="flex items-center gap-2 px-4 py-2 rounded-lg text-blue-700 font-medium hover:bg-blue-50 transition">
          <span class="text-xl">🔳</span> Image Segmentation
        </router-link>
        <router-link to="/speech-recognition" class="flex items-center gap-2 px-4 py-2 rounded-lg text-blue-700 font-medium hover:bg-blue-50 transition">
          <span class="text-xl">🎤</span> Speech Recognition
        </router-link>
        <router-link to="/video-detection" class="flex items-center gap-2 px-4 py-2 rounded-lg text-blue-700 font-medium hover:bg-blue-50 transition">
          <span class="text-xl">🎬</span> Video Detection
        </router-link>
        <router-link to="/profile" class="flex items-center gap-2 px-4 py-2 rounded-lg text-blue-700 font-medium hover:bg-blue-50 transition">
          <span class="text-xl">👤</span> Profile
        </router-link>
      </nav>

      <button class="mt-auto w-full bg-red-100 text-red-600 font-semibold py-2 rounded-lg hover:bg-red-200 transition flex items-center justify-center gap-2" @click="logout">
        <span class="text-lg">⎋</span> Logout
      </button>
    </aside>

    <main class="flex-1 flex flex-col items-center justify-center p-10">
      <div class="mb-6">
        <div v-if="secureMessage" class="text-green-700 font-semibold">{{ secureMessage }}</div>
        <div v-if="secureError" class="text-red-600">{{ secureError }}</div>
      </div>
      <router-view />
    </main>
  </div>
</template>
