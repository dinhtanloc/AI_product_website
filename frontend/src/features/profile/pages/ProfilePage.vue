<script setup>
import { ref } from 'vue'

const name = ref('Tan Loc')
const phone = ref('')
</script>

<template>
  <div class="bg-white p-8 rounded-2xl shadow-2xl max-w-lg w-full flex flex-col items-center">
    <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" alt="Avatar" class="w-20 h-20 rounded-full border-4 border-blue-200 mb-4" />
    <h2 class="text-2xl font-extrabold text-blue-700 mb-2">Edit Profile</h2>
    <p class="text-gray-500 mb-6">Update your personal information</p>

    <div class="space-y-4 w-full">
      <input v-model="name" class="border border-gray-300 rounded-xl px-4 py-2 w-full shadow-sm focus:ring-2 focus:ring-blue-400 outline-none transition-all" placeholder="Name" />
      <input v-model="phone" class="border border-gray-300 rounded-xl px-4 py-2 w-full shadow-sm focus:ring-2 focus:ring-blue-400 outline-none transition-all" placeholder="Phone" />

      <button class="w-full bg-gradient-to-r from-green-500 to-emerald-500 text-white py-2 rounded-xl shadow hover:from-green-600 hover:to-emerald-600 active:scale-95 transition-all font-semibold">
        Save
      </button>
    </div>
  </div>
</template>
