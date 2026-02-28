<template>
  <nav class="w-full bg-[#0B0D14]/80 backdrop-blur-md border-b border-gray-800 fixed top-0 z-50">
    <div class="max-w-7xl mx-auto px-6 h-20 flex justify-between items-center">
      
      <router-link to="/" class="text-2xl font-bold text-[#E5B869] font-serif tracking-wide">
        Endura
      </router-link>

      <div class="flex items-center space-x-8">
        
        <router-link 
          to="/" 
          class="text-sm font-medium text-gray-400 hover:text-white transition-colors"
          exact-active-class="text-[#E5B869] hover:text-[#E5B869]"
        >
          Home
        </router-link>

        <router-link 
          to="/dashboard" 
          class="text-sm font-medium text-gray-400 hover:text-white transition-colors"
          active-class="text-[#E5B869] hover:text-[#E5B869]"
        >
          Dashboard
        </router-link>

        <div class="h-6 w-px bg-gray-800"></div>

        <template v-if="isLoggedIn">
          <button 
            @click="handleLogout" 
            class="text-sm font-medium text-gray-400 hover:text-red-400 flex items-center space-x-2 transition-colors"
          >
            <ion-icon name="log-out-outline" class="text-lg"></ion-icon>
            <span>Logout</span>
          </button>
        </template>
        
        <template v-else>
          <router-link 
            to="/login" 
            class="bg-[#E5B869] hover:bg-[#d0a75d] text-black text-sm font-bold py-2.5 px-6 rounded-xl transition-transform hover:scale-105 shadow-lg shadow-[#E5B869]/10"
          >
            Sign In
          </router-link>
        </template>

      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// This is a temporary simulation. 
// Later, this will check your Vuex/Pinia store or localStorage for a Django JWT token.
const isLoggedIn = ref(false)

// A quick helper to check if the user has a token in their browser
onMounted(() => {
  const token = localStorage.getItem('access_token')
  if (token) {
    isLoggedIn.value = true
  }
})

const handleLogout = () => {
  // Clear the token and update the state
  localStorage.removeItem('access_token')
  isLoggedIn.value = false
  
  console.log("User logged out successfully.")
  
  // Kick them back to the landing page
  router.push('/')
}
</script>