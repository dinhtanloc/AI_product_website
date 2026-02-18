<template>
  <div class="bg-white p-8 rounded-2xl shadow-2xl max-w-lg w-full flex flex-col items-center">
    <img src="https://img.icons8.com/fluency/96/image.png" alt="Image Generation" class="w-20 h-20 mb-4" />
    <h2 class="text-2xl font-extrabold text-blue-700 mb-2">Image Generation</h2>
    <p class="text-gray-500 mb-6">Generate creative images using AI.</p>
    <input type="text" class="border border-gray-300 rounded-xl px-4 py-2 w-full shadow-sm focus:ring-2 focus:ring-blue-400 outline-none transition-all mb-4" placeholder="Describe your image..." />
    <button class="w-full bg-gradient-to-r from-blue-500 to-indigo-500 text-white py-2 rounded-xl shadow hover:from-blue-600 hover:to-indigo-600 active:scale-95 transition-all font-semibold">
      Generate
    </button>
    <div class="mt-6 w-full flex flex-col items-center">
      <!-- Generated image preview here -->
      <div class="text-gray-400">No image generated yet.</div>
    </div>
  </div>
</template>
