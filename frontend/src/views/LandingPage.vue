<template>
  <div class="min-h-screen w-full flex flex-col bg-[#0B0D14] text-white">
    
    <nav class="w-full flex justify-between items-center p-6 border-b border-gray-800">
      <div class="text-2xl font-bold text-[#E5B869] font-serif tracking-wide">Endura</div>
      <button @click="goToLogin" class="text-sm font-semibold hover:text-[#E5B869] transition-colors">
        Sign In
      </button>
    </nav>

    <main class="flex-1 flex flex-col items-center justify-center px-6 text-center">
      <div class="max-w-3xl space-y-6 animate-fade-in">
        
        <h1 class="text-5xl md:text-7xl font-extrabold tracking-tight text-white font-serif">
          Secure Your <span class="text-[#E5B869]">Digital Legacy</span>
        </h1>
        
        <p class="text-lg md:text-xl text-gray-400 max-w-2xl mx-auto">
          The ultimate vault for managing, protecting, and automating your most important digital assets.
        </p>

        <div class="pt-8">
          <button 
            @click="goToLogin"
            class="px-8 py-4 text-lg font-bold rounded-full bg-[#E5B869] hover:bg-[#d6a858] text-black transition-transform hover:scale-105 shadow-lg shadow-[#E5B869]/20"
          >
            Enter the Vault
          </button>
        </div>

      </div>
    </main>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

// Initialize the router inside this component
const router = useRouter()

const goToLogin = () => {
  // Pushes the user to the /login URL we defined in step 2
  router.push('/login')
}
</script>

<style scoped>
.animate-fade-in {
  animation: fadeIn 1s ease-out forwards;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>