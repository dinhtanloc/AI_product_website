<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-pink-100 via-purple-100 to-pink-200">
    <div class="bg-white p-8 rounded-2xl shadow-2xl w-96 space-y-6 flex flex-col items-center">
      <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" alt="Logo" class="w-16 h-16 mb-2" />
      <h2 class="text-3xl font-extrabold text-purple-700 mb-2 tracking-wide">Create Account</h2>
      <p class="text-gray-500 text-sm mb-4">Sign up to get started</p>

      <BaseInput placeholder="Email" />
      <BaseInput type="password" placeholder="Password" />
      <BaseButton>Register</BaseButton>

      <router-link to="/login" class="text-sm text-blue-600 text-center block hover:underline mt-2">
        Back to login
      </router-link>
    </div>
  </div>
</template>

<script setup>
import BaseInput from '@/components/BaseInput.vue'
import BaseButton from '@/components/BaseButton.vue'
</script>
