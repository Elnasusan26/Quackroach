<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

// --- UI State Variables ---
const isLocked = ref(true)
const isInitializing = ref(false)
const vaultPassword = ref('')
const errorMessage = ref('')
const vaultItems = ref([])

// Raw encrypted data from Django
const encryptedPayload = ref(null)

// --- Safe Base64 Helpers (Prevents Call Stack Limits on Large Decryptions) ---
function bufferToBase64(buffer) {
  let binary = ''
  const bytes = new Uint8Array(buffer)
  for (let i = 0; i < bytes.byteLength; i++) {
    binary += String.fromCharCode(bytes[i])
  }
  return window.btoa(binary)
}

function base64ToBuffer(base64) {
  const binary_string = window.atob(base64)
  const len = binary_string.length
  const bytes = new Uint8Array(len)
  for (let i = 0; i < len; i++) {
    bytes[i] = binary_string.charCodeAt(i)
  }
  return bytes
}

// --- Web Crypto API Functions ---
async function deriveKey(password, salt) {
  const enc = new TextEncoder()
  const keyMaterial = await crypto.subtle.importKey(
    "raw",
    enc.encode(password),
    "PBKDF2",
    false,
    ["deriveKey"]
  )

  return crypto.subtle.deriveKey(
    {
      name: "PBKDF2",
      salt: salt,
      iterations: 250000,
      hash: "SHA-256",
    },
    keyMaterial,
    { name: "AES-GCM", length: 256 },
    false,
    ["encrypt", "decrypt"]
  )
}

async function encryptVault(password, dataObj) {
  const enc = new TextEncoder()
  const iv = crypto.getRandomValues(new Uint8Array(12))
  const salt = crypto.getRandomValues(new Uint8Array(16))

  const key = await deriveKey(password, salt)
  const encrypted = await crypto.subtle.encrypt(
    { name: "AES-GCM", iv },
    key,
    enc.encode(JSON.stringify(dataObj))
  )

  return {
    ciphertext: bufferToBase64(encrypted),
    iv: bufferToBase64(iv),
    salt: bufferToBase64(salt),
  }
}

async function decryptVault(password, encryptedObj) {
  const dec = new TextDecoder()
  const iv = base64ToBuffer(encryptedObj.iv)
  const salt = base64ToBuffer(encryptedObj.salt)
  const ciphertext = base64ToBuffer(encryptedObj.ciphertext)

  const key = await deriveKey(password, salt)
  const decrypted = await crypto.subtle.decrypt(
    { name: "AES-GCM", iv },
    key,
    ciphertext
  )

  return JSON.parse(dec.decode(decrypted))
}

// --- Vault Logic ---

// 1. Fetch vault state on load
onMounted(async () => {
  const token = localStorage.getItem('access_token')
  if (!token) {
    router.push('/login')
    return
  }

  try {
    const response = await axios.get('http://127.0.0.1:8000/api/vault/', {
      headers: { Authorization: `Bearer ${token}` }
    })

    if (response.data.message === "Vault not initialized") {
      isInitializing.value = true
    } else {
      encryptedPayload.value = response.data
    }
  } catch (error) {
    if (error.response?.status === 401) router.push('/login')
    console.error("Failed to fetch vault status:", error)
  }
})

// 2. Unlock an existing vault
const handleUnlock = async () => {
  errorMessage.value = ''
  try {
    const decryptedData = await decryptVault(vaultPassword.value, encryptedPayload.value)
    
    // Assign decrypted data to our reactive array
    vaultItems.value = decryptedData.items || []
    
    isLocked.value = false
    vaultPassword.value = '' // Clear password from memory immediately
  } catch (error) {
    errorMessage.value = 'Incorrect Vault Password or corrupted data.'
    console.error("Decryption failed:", error)
  }
}

// 3. Initialize a brand new vault
const handleSetup = async () => {
  errorMessage.value = ''
  if (vaultPassword.value.length < 8) {
    errorMessage.value = 'Password must be at least 8 characters long.'
    return
  }

  try {
    const initialData = {
      items: [
        { id: 1, title: 'Chase Savings', type: 'Bank', details: '•••• 4829', value: '$24,500', icon: 'business-outline' },
        { id: 2, title: 'Life Insurance', type: 'Insurance', details: 'Policy #••••91', value: '$500,000', icon: 'shield-half-outline' }
      ]
    }

    const encryptedPackage = await encryptVault(vaultPassword.value, initialData)
    const token = localStorage.getItem('access_token')

    await axios.post('http://127.0.0.1:8000/api/vault/', encryptedPackage, {
      headers: { Authorization: `Bearer ${token}` }
    })

    vaultItems.value = initialData.items
    isInitializing.value = false
    isLocked.value = false
    vaultPassword.value = '' // Clear password from memory
  } catch (error) {
    errorMessage.value = 'Failed to setup vault. Please try again.'
    console.error("Encryption/Save failed:", error)
  }
}
</script>

<template>
  <div class="container mx-auto px-4 py-8 mt-9 max-w-5xl">
    
    <div v-if="isLocked" class="flex flex-col items-center justify-center mt-20">
      <div class="bg-card border shadow-xl rounded-2xl p-8 max-w-md w-full text-center">
        
        <div class="bg-primary/10 text-primary w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-6">
          <ion-icon name="lock-closed-outline" class="text-3xl"></ion-icon>
        </div>

        <h2 class="text-2xl font-bold mb-2">
          {{ isInitializing ? 'Create Vault Password' : 'Vault Locked' }}
        </h2>
        <p class="text-muted-foreground mb-6 text-sm">
          {{ isInitializing 
            ? 'This password encrypts your data. We CANNOT recover it if you lose it.' 
            : 'Enter your zero-knowledge password to decrypt your assets locally.' 
          }}
        </p>

        <form @submit.prevent="isInitializing ? handleSetup() : handleUnlock()" class="space-y-4">
          <input 
            v-model="vaultPassword" 
            type="password" 
            :placeholder="isInitializing ? 'Create a strong password' : 'Enter vault password'"
            required
            class="w-full p-3 border rounded-md bg-background text-foreground text-center tracking-widest"
          />
          
          <p v-if="errorMessage" class="text-red-500 text-sm font-medium">{{ errorMessage }}</p>
          
          <button type="submit" class="w-full bg-primary text-primary-foreground p-3 rounded-md hover:bg-primary/90 transition font-semibold">
            {{ isInitializing ? 'Encrypt & Initialize Vault' : 'Decrypt & Unlock' }}
          </button>
        </form>
      </div>
    </div>

    <div v-else>
      <div class="flex justify-between items-start mb-12 border-b border-gray-800 pb-6">
        <header>
          <h2 class="text-4xl font-serif font-bold mb-2">Your Vault</h2>
          <p class="text-gray-400 text-lg">Securely store your important assets.</p>
        </header>
        
        <div class="flex items-center gap-4">
          <ion-icon name="lock-closed"></ion-icon>
          <button @click="isLocked = true" class="text-lg font-medium text-red-400 hover:text-red-300 transition-colors">
            Lock Vault
          </button>
          <button @click="router.push('/addvault')" class="bg-[#E5B869] hover:bg-[#d0a75d] text-black font-semibold py-3 px-6 rounded-xl flex items-center space-x-2 transition-transform hover:scale-105 shadow-lg">
            <ion-icon name="add-outline" class="text-xl"></ion-icon>
            <span>Add New</span>
          </button>
        </div>
      </div>

      <div v-if="vaultItems.length === 0" class="text-center py-20 text-muted-foreground">
        No assets found. Click "Add New" to securely encrypt your first item.
      </div>

      <div v-else class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div v-for="item in vaultItems" :key="item.id" class="bg-[#12141c] border border-gray-800 rounded-2xl p-6 shadow-lg flex flex-col justify-between h-40 hover:border-gray-700 transition-colors">
          
          <div class="flex items-start space-x-4">
            <div class="bg-[#1A1C23] p-3 rounded-xl text-[#E5B869] flex items-center justify-center">
              <ion-icon v-if="item.icon" :name="item.icon" class="text-2xl"></ion-icon>
              <ion-icon v-else name="folder-outline" class="text-2xl"></ion-icon>
            </div>
            
            <div>
              <h3 class="text-lg font-bold text-white">{{ item.title }}</h3>
              <p class="text-sm text-gray-500">{{ item.type }}</p>
            </div>
          </div>

          <div class="flex justify-between items-end mt-4">
            <p class="text-sm text-gray-400 font-mono">{{ item.details }}</p>
            <p class="text-lg font-bold text-[#E5B869]">{{ item.value }}</p>
          </div>
          
        </div>
      </div>
    </div>

  </div>
</template>