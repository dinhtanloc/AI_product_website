<script setup lang="ts">
import { ref } from 'vue'

const messages = ref<string[]>([])
const input = ref('')

const send = () => {
  if (!input.value) return
  messages.value.push(input.value)
  input.value = ''
}
</script>

<template>
  <div class="flex flex-col h-full w-full">
    <div class="flex-1 bg-white p-6 rounded-2xl shadow-lg overflow-y-auto space-y-4 mb-4 w-full">
      <div
        v-for="(m,i) in messages"
        :key="i"
        class="flex items-end gap-3"
      >
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" class="w-8 h-8 rounded-full border border-blue-200" />
        <div class="bg-blue-100 px-4 py-2 rounded-2xl text-gray-800 shadow-sm max-w-xs">
          {{ m }}
        </div>
      </div>
      <div v-if="messages.length === 0" class="text-gray-400 text-center py-10">No messages yet. Start the conversation!</div>
    </div>

    <div class="flex gap-2 mt-auto bg-white p-3 rounded-xl shadow-md w-full">
      <input
        v-model="input"
        class="flex-1 border border-gray-300 rounded-xl px-4 py-2 shadow-sm focus:ring-2 focus:ring-blue-400 outline-none transition-all"
        @keyup.enter="send"
        placeholder="Type your message..."
      />
      <button
        class="bg-gradient-to-r from-blue-500 to-indigo-500 text-white px-6 py-2 rounded-xl shadow hover:from-blue-600 hover:to-indigo-600 active:scale-95 transition-all font-semibold"
        @click="send"
      >
        Send
      </button>
    </div>
  </div>
</template>
