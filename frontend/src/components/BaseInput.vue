<script setup lang="ts">
defineProps(['modelValue', 'placeholder', 'type'])
defineEmits(['update:modelValue'])
</script>

<template>
  <input
    :type="type || 'text'"
    :placeholder="placeholder"
    class="w-full border border-gray-300 rounded-xl px-4 py-2 shadow-sm focus:ring-2 focus:ring-blue-400 focus:border-blue-400 outline-none transition-all duration-200 bg-white text-gray-800 placeholder-gray-400"
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
  />
</template>
