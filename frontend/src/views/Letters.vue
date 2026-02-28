<script setup>
// Mock data matching your screenshot
const legacyLetters = [
  { id: 1, recipient: 'Sarah Morrison', date: 'Jan 15, 2026', preview: "My dearest Sarah, if you're reading this..." },
  { id: 2, recipient: 'David Morrison', date: 'Dec 3, 2025', preview: "Son, there are things I never told you..." },
  { id: 3, recipient: 'Emma Chen', date: 'Nov 20, 2025', preview: "To my trusted friend and partner..." },
]
</script>

<template>
  <div>
    <div class="flex justify-between items-start mb-12">
      <header>
        <h2 class="text-4xl font-serif font-bold mb-2 text-white">Legacy Letters</h2>
        <p class="text-gray-400 text-lg">Words that will live beyond you.</p>
      </header>
      
      <button class="bg-[#E5B869] hover:bg-[#d0a75d] text-black font-semibold py-3 px-6 rounded-xl flex items-center space-x-2 transition-transform hover:scale-105 shadow-lg">
        <ion-icon name="create-outline" class="text-xl"></ion-icon>
        <span>Write a Letter</span>
      </button>
    </div>

    <div class="space-y-4">
      
      <div 
        v-for="letter in legacyLetters" 
        :key="letter.id" 
        class="bg-[#12141c] border border-gray-800 rounded-2xl p-6 shadow-sm hover:border-gray-700 transition-colors flex items-center justify-between cursor-pointer group"
      >
        <div class="flex items-center space-x-6">
          <div class="relative flex items-center justify-center w-12 h-12 rounded-full bg-red-900/30 border border-red-900/50 group-hover:bg-red-900/50 transition-colors">
            <div class="w-4 h-4 rounded-full bg-red-500 shadow-[0_0_10px_rgba(239,68,68,0.5)]"></div>
          </div>
          
          <div>
            <h3 class="text-lg font-bold text-white mb-1">{{ letter.recipient }}</h3>
            <p class="text-sm text-gray-500">{{ letter.preview }}</p>
          </div>
        </div>

        <div class="text-sm text-gray-500 font-medium">
          {{ letter.date }}
        </div>
      </div>

    </div>
  </div>
</template>