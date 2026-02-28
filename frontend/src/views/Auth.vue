<script setup>
import { ref } from 'vue'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'

// Form state
const loginEmail = ref('')
const loginPassword = ref('')

const signupName = ref('')
const signupEmail = ref('')
const signupPassword = ref('')

const handleLogin = () => {
  console.log("Logging in with:", loginEmail.value)
  // Axios POST to Django /api/login/
}

const handleSignup = () => {
  console.log("Signing up:", signupName.value, signupEmail.value)
  // Axios POST to Django /api/register/
}
</script>

<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-[#0d0e15] text-white px-4 font-sans">
    
    <div class="text-center mb-8">
      <h1 class="text-5xl font-bold text-[#e1b86e] mb-2 font-serif tracking-wide">Endura</h1>
      <p class="text-gray-400 text-sm font-medium">Your Digital Legacy Vault</p>
    </div>

    <div class="bg-[#12141c] border border-gray-800 rounded-2xl w-full max-w-md p-6 shadow-2xl">
      
      <Tabs defaultValue="signin" class="w-full">
        
        <TabsList class="grid w-full grid-cols-2 bg-[#090a0f] rounded-xl p-1 mb-8">
          <TabsTrigger 
            value="signin" 
            class="rounded-lg py-2.5 text-sm font-semibold data-[state=active]:bg-[#e1b86e] data-[state=active]:text-black text-gray-500 transition-all"
          >
            Sign In
          </TabsTrigger>
          <TabsTrigger 
            value="signup" 
            class="rounded-lg py-2.5 text-sm font-semibold data-[state=active]:bg-[#e1b86e] data-[state=active]:text-black text-gray-500 transition-all"
          >
            Sign Up
          </TabsTrigger>
        </TabsList>

        <TabsContent value="signin">
          <form @submit.prevent="handleLogin" class="space-y-5">
            <div class="space-y-2">
              <Label for="email" class="text-xs font-semibold text-gray-400 ml-1">Email Address</Label>
              <Input 
                id="email" 
                type="email" 
                v-model="loginEmail" 
                placeholder="you@example.com" 
                class="bg-[#12141c] border-gray-800 focus-visible:ring-1 focus-visible:ring-[#e1b86e] focus-visible:border-[#e1b86e] text-gray-200 h-12 rounded-xl"
              />
            </div>

            <div class="space-y-2">
              <Label for="password" class="text-xs font-semibold text-gray-400 ml-1">Password</Label>
              <Input 
                id="password" 
                type="password" 
                v-model="loginPassword" 
                placeholder="••••••••" 
                class="bg-[#12141c] border-gray-800 focus-visible:ring-1 focus-visible:ring-[#e1b86e] focus-visible:border-[#e1b86e] text-gray-200 h-12 rounded-xl"
              />
            </div>

            <div class="flex justify-end pt-1">
              <a href="#" class="text-xs text-[#e1b86e] hover:text-[#f2ce8a] transition-colors">Forgot password?</a>
            </div>

            <Button type="submit" class="w-full bg-[#e1b86e] hover:bg-[#d0a75d] text-black font-bold h-12 rounded-xl mt-4 text-base">
              Sign In
            </Button>
          </form>
        </TabsContent>

        <TabsContent value="signup">
          <form @submit.prevent="handleSignup" class="space-y-5">
            <div class="space-y-2">
              <Label for="name" class="text-xs font-semibold text-gray-400 ml-1">Full Name</Label>
              <Input 
                id="name" 
                type="text" 
                v-model="signupName" 
                placeholder="James Morrison" 
                class="bg-[#12141c] border-gray-800 focus-visible:ring-1 focus-visible:ring-[#e1b86e] focus-visible:border-[#e1b86e] text-gray-200 h-12 rounded-xl"
              />
            </div>

            <div class="space-y-2">
              <Label for="signup-email" class="text-xs font-semibold text-gray-400 ml-1">Email Address</Label>
              <Input 
                id="signup-email" 
                type="email" 
                v-model="signupEmail" 
                placeholder="you@example.com" 
                class="bg-[#12141c] border-gray-800 focus-visible:ring-1 focus-visible:ring-[#e1b86e] focus-visible:border-[#e1b86e] text-gray-200 h-12 rounded-xl"
              />
            </div>

            <div class="space-y-2">
              <Label for="signup-password" class="text-xs font-semibold text-gray-400 ml-1">Password</Label>
              <Input 
                id="signup-password" 
                type="password" 
                v-model="signupPassword" 
                placeholder="••••••••" 
                class="bg-[#12141c] border-gray-800 focus-visible:ring-1 focus-visible:ring-[#e1b86e] focus-visible:border-[#e1b86e] text-gray-200 h-12 rounded-xl"
              />
            </div>

            <Button type="submit" class="w-full bg-[#e1b86e] hover:bg-[#d0a75d] text-black font-bold h-12 rounded-xl mt-2 text-base">
              Create Account
            </Button>

            <p class="text-center text-[11px] text-gray-500 mt-4">
              By creating an account, you agree to our Terms of Service
            </p>
          </form>
        </TabsContent>

      </Tabs>
    </div>
  </div>
</template>