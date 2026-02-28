<template>
  <aside class="w-64 bg-[#090A0F] border-r border-gray-800 flex flex-col justify-between">
    <div>
      <div class="p-8">
        <h1 class="text-3xl font-bold text-[#E5B869] font-serif tracking-wide">Endura</h1>
      </div>
      
      <nav class="space-y-2 px-4">
        <router-link 
          to="/dashboard" 
          class="flex items-center space-x-3 px-4 py-3 rounded-xl transition-colors text-gray-400 hover:text-white hover:bg-[#12141c]"
          exact-active-class="bg-[#1A1A1A] text-[#E5B869] hover:text-[#E5B869]"
        >
          <ion-icon name="grid-outline" class="text-xl"></ion-icon>
          <span class="font-medium text-sm">Dashboard</span>
        </router-link>
        
        <router-link 
          to="/vault" 
          class="flex items-center space-x-3 px-4 py-3 rounded-xl transition-colors text-gray-400 hover:text-white hover:bg-[#12141c]"
          exact-active-class="bg-[#1A1A1A] text-[#E5B869] hover:text-[#E5B869]"
        >
          <ion-icon name="shield-outline" class="text-xl"></ion-icon>
          <span class="font-medium text-sm">Vault</span>
        </router-link>

        <router-link 
          to="/letters" 
          class="flex items-center space-x-3 px-4 py-3 rounded-xl transition-colors text-gray-400 hover:text-white hover:bg-[#12141c]"
          exact-active-class="bg-[#1A1A1A] text-[#E5B869] hover:text-[#E5B869]"
        >
          <ion-icon name="mail-outline" class="text-xl"></ion-icon>
          <span class="font-medium text-sm">Letters</span>
        </router-link>
        
        <a href="#" class="flex items-center space-x-3 text-gray-400 hover:text-white hover:bg-[#12141c] px-4 py-3 rounded-xl transition-colors">
          <ion-icon name="person-outline" class="text-xl"></ion-icon>
          <span class="font-medium text-sm">Executor</span>
        </a>
      </nav>
    </div>

    <div class="p-4 mb-4">
      <router-link to="/login" class="flex items-center space-x-3 text-gray-500 hover:text-white px-4 py-3 transition-colors">
        <ion-icon name="log-out-outline" class="text-xl"></ion-icon>
        <span class="font-medium text-sm">Sign Out</span>
      </router-link>
    </div>
  </aside>
</template>

<script setup>
// No logic needed here right now!
</script>