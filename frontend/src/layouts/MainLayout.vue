<template>
  <div class="flex h-screen bg-[#0B0D14] text-white font-sans overflow-hidden">
    <AppSidebar />
    
    <main class="flex-1 p-12 overflow-y-auto">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import AppSidebar from '@/components/AppSidebar.vue'
</script>