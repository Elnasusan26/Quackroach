<script setup>
import { ref, computed } from 'vue'

// Mock data for the dashboard
// Eventually, this will be fetched from your Django backend!
const userName = ref('James')
const completionPercentage = ref(72)

// Math for the SVG circle (circumference = 2 * pi * r)
const radius = 80
const circumference = 2 * Math.PI * radius

// Using 'computed' so the circle automatically animates if the percentage changes
const dashoffset = computed(() => {
  return circumference - (completionPercentage.value / 100) * circumference
})
</script>

<template>
  <div>
    <header class="mb-12">
      <h2 class="text-4xl font-serif font-bold mb-2">Welcome back, {{ userName }}</h2>
      <p class="text-gray-400 text-lg">Your legacy is {{ completionPercentage }}% secured.</p>
    </header>

    <div class="flex justify-center my-16">
      <div class="relative flex items-center justify-center">
        <svg class="transform -rotate-90 w-56 h-56">
          <circle cx="112" cy="112" :r="radius" stroke="#1f222e" stroke-width="12" fill="none" />
          <circle 
            cx="112" cy="112" :r="radius" 
            stroke="#E5B869" 
            stroke-width="12" 
            fill="none" 
            stroke-linecap="round"
            :stroke-dasharray="circumference"
            :stroke-dashoffset="dashoffset"
            class="transition-all duration-1000 ease-out"
          />
        </svg>
        <div class="absolute text-center">
          <span class="text-4xl font-serif font-bold text-[#E5B869]">{{ completionPercentage }}%</span>
          <p class="text-xs text-gray-400 mt-1">Complete</p>
        </div>
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
      
      <div class="bg-[#12141c] border border-gray-800 rounded-2xl p-6 shadow-lg hover:border-gray-700 transition-colors">
        <div class="flex items-center space-x-2 text-gray-400 mb-4">
          <ion-icon name="shield-checkmark-outline"></ion-icon>
          <span class="text-sm font-medium">Vault Items</span>
        </div>
        <div class="text-3xl font-serif font-bold text-white">12</div>
      </div>
      
      <div class="bg-[#12141c] border border-gray-800 rounded-2xl p-6 shadow-lg hover:border-gray-700 transition-colors">
        <div class="flex items-center space-x-2 text-gray-400 mb-4">
          <ion-icon name="document-text-outline"></ion-icon>
          <span class="text-sm font-medium">Letters Written</span>
        </div>
        <div class="text-3xl font-serif font-bold text-white">3</div>
      </div>

      <div class="bg-[#12141c] border border-gray-800 rounded-2xl p-6 shadow-lg hover:border-gray-700 transition-colors">
        <div class="flex items-center space-x-2 text-gray-400 mb-4">
          <ion-icon name="person-add-outline"></ion-icon>
          <span class="text-sm font-medium">Executor Assigned</span>
        </div>
        <div class="text-3xl font-serif font-bold text-white">Yes</div>
      </div>

      <div class="bg-[#12141c] border border-gray-800 rounded-2xl p-6 shadow-lg hover:border-gray-700 transition-colors">
        <div class="flex items-center space-x-2 text-gray-400 mb-4">
          <ion-icon name="time-outline"></ion-icon>
          <span class="text-sm font-medium">Last Check-in</span>
        </div>
        <div class="text-3xl font-serif font-bold text-white">2 days ago</div>
      </div>
      
    </div>
  </div>
</template>