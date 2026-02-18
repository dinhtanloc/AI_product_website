<template>
  <div class="bg-white p-8 rounded-2xl shadow-2xl max-w-lg w-full flex flex-col items-center">
    <img src="https://img.icons8.com/fluency/96/video.png" alt="Video Detection" class="w-20 h-20 mb-4" />
    <h2 class="text-2xl font-extrabold text-purple-700 mb-2">Video Detection</h2>
    <p class="text-gray-500 mb-6">Detect objects or scenes in your videos using AI.</p>
    <input type="file" accept="video/*" class="mb-4" />
    <button class="w-full bg-gradient-to-r from-purple-500 to-pink-500 text-white py-2 rounded-xl shadow hover:from-purple-600 hover:to-pink-600 active:scale-95 transition-all font-semibold">
      Detect
    </button>
    <div class="mt-6 w-full flex flex-col items-center">
      <!-- Detection results preview here -->
      <div class="text-gray-400">No video analyzed yet.</div>
    </div>
  </div>
</template>
