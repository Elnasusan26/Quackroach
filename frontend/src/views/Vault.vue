<script setup>
// In the future, this data will come from your Django backend!
const vaultItems = [
  { id: 1, title: 'Chase Savings', type: 'Bank', details: '•••• 4829', value: '$24,500', icon: 'business-outline' },
  { id: 2, title: 'Life Insurance', type: 'Insurance', details: 'Policy #••••91', value: '$500,000', icon: 'shield-half-outline' },
  { id: 3, title: 'Bitcoin Wallet', type: 'Crypto', details: 'bc1q••••x8f2', value: '1.42 BTC', icon: 'logo-bitcoin' },
  { id: 4, title: 'Netflix', type: 'Subscription', details: 'Monthly', value: '$15.99/mo', icon: 'card-outline' },
]
</script>

<template>
  <div>
    <div class="flex justify-between items-start mb-12">
      <header>
        <h2 class="text-4xl font-serif font-bold mb-2">Your Vault</h2>
        <p class="text-gray-400 text-lg">Securely store your important assets.</p>
      </header>
      
      <button class="bg-[#E5B869] hover:bg-[#d0a75d] text-black font-semibold py-3 px-6 rounded-xl flex items-center space-x-2 transition-transform hover:scale-105 shadow-lg">
        <ion-icon name="add-outline" class="text-xl"></ion-icon>
        <span>Add New</span>
      </button>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      
      <div v-for="item in vaultItems" :key="item.id" class="bg-[#12141c] border border-gray-800 rounded-2xl p-6 shadow-lg flex flex-col justify-between h-40 hover:border-gray-700 transition-colors">
        
        <div class="flex items-start space-x-4">
          <div class="bg-[#1A1C23] p-3 rounded-xl text-[#E5B869]">
            <ion-icon :name="item.icon" class="text-2xl"></ion-icon>
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
</template>