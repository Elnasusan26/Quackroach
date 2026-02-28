<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-[#0B0D14] text-white px-4 font-sans">
    
    <div class="text-center mb-8">
      <h1 class="text-5xl font-bold text-[#E5B869] mb-2 font-serif tracking-wide">Endura</h1>
      <p class="text-gray-400 text-sm font-medium">Your Digital Legacy Vault</p>
    </div>

    <div class="bg-[#13151A] border border-gray-800 rounded-2xl w-full max-w-md p-6 shadow-2xl">
      
      <div class="flex bg-[#0B0D14] rounded-xl p-1 mb-8">
        <button class="flex-1 py-2.5 text-sm font-semibold rounded-lg bg-[#E5B869] text-black shadow-sm">
          Sign In
        </button>
        <button class="flex-1 py-2.5 text-sm font-semibold rounded-lg text-gray-500 hover:text-gray-300 transition-colors">
          Sign Up
        </button>
      </div>

      <form @submit.prevent="handleLogin" class="space-y-5">
        
        <div>
          <label class="block text-xs font-semibold text-gray-400 mb-2 ml-1">Email Address</label>
          <input 
            type="email" 
            v-model="email" 
            placeholder="you@example.com" 
            class="w-full bg-[#0B0D14] border border-gray-700 rounded-xl px-4 py-3 text-sm text-gray-200 placeholder-gray-500 focus:outline-none focus:border-[#E5B869] focus:ring-1 focus:ring-[#E5B869] transition-all" 
          />
        </div>

        <div>
          <label class="block text-xs font-semibold text-gray-400 mb-2 ml-1">Password</label>
          <input 
            type="password" 
            v-model="password" 
            placeholder="••••••••" 
            class="w-full bg-[#0B0D14] border border-gray-700 rounded-xl px-4 py-3 text-sm text-gray-200 placeholder-gray-500 focus:outline-none focus:border-[#E5B869] focus:ring-1 focus:ring-[#E5B869] transition-all" 
          />
        </div>

        <div class="flex justify-end pt-1">
          <a href="#" class="text-xs text-[#E5B869] hover:text-[#f3cd85] transition-colors">Forgot password?</a>
        </div>

        <button 
          type="submit" 
          class="w-full bg-[#E5B869] hover:bg-[#d6a858] text-black font-bold py-3.5 rounded-xl transition-all mt-4"
        >
          Sign In
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const email = ref('')
const password = ref('')

const handleLogin = () => {
  console.log("Attempting login with:", email.value)
  // Here we will eventually connect to your Django backend using Axios
}
</script>