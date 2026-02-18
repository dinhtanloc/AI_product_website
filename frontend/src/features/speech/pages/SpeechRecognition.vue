<template>
  <div class="bg-white p-8 rounded-2xl shadow-2xl max-w-lg w-full flex flex-col items-center">
    <img src="https://img.icons8.com/fluency/96/voice-presentation.png" alt="Speech Recognition" class="w-20 h-20 mb-4" />
    <h2 class="text-2xl font-extrabold text-blue-700 mb-2">Speech Recognition</h2>
    <p class="text-gray-500 mb-6">Transcribe or generate text from speech using AI.</p>
    <input type="file" accept="audio/*" class="mb-4" />
    <button class="w-full bg-gradient-to-r from-blue-500 to-indigo-500 text-white py-2 rounded-xl shadow hover:from-blue-600 hover:to-indigo-600 active:scale-95 transition-all font-semibold">
      Recognize
    </button>
    <div class="mt-6 w-full flex flex-col items-center">
      <!-- Speech recognition result preview here -->
      <div class="text-gray-400">No speech recognized yet.</div>
    </div>
  </div>
</template>
