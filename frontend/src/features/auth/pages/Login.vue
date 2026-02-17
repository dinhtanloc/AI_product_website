<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import BaseInput from '@/components/BaseInput.vue'
import BaseButton from '@/components/BaseButton.vue'

const email = ref('')
const password = ref('')
const router = useRouter()

const login = () => {
  localStorage.setItem('token', 'demo')
  router.push('/')
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-100 via-indigo-100 to-blue-200">
    <div class="bg-white p-8 rounded-2xl shadow-2xl w-96 space-y-6 flex flex-col items-center">
      <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" alt="Logo" class="w-16 h-16 mb-2" />
      <h2 class="text-3xl font-extrabold text-blue-700 mb-2 tracking-wide">Welcome Back</h2>
      <p class="text-gray-500 text-sm mb-4">Sign in to your account</p>

      <BaseInput v-model="email" placeholder="Email" />
      <BaseInput v-model="password" type="password" placeholder="Password" />

      <BaseButton @click="login">Login</BaseButton>

      <router-link to="/register" class="text-blue-600 text-sm text-center block hover:underline mt-2">
        Create account
      </router-link>
    </div>
  </div>
</template>
