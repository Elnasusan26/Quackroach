import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../views/LandingPage.vue'
import Auth from '../views/Auth.vue'
import MainLayout from '../layouts/MainLayout.vue'
import Dashboard from '../views/Dashboard.vue'
import Vault from '../views/Vault.vue'
import Letters from '../views/Letters.vue' // 1. Import the new view

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: LandingPage },
    { path: '/login', name: 'login', component: Auth },
    
    {
      path: '/',
      component: MainLayout,
      children: [
        { path: 'dashboard', name: 'dashboard', component: Dashboard },
        { path: 'vault', name: 'vault', component: Vault },
        { path: 'letters', name: 'letters', component: Letters } // 2. Add the route
      ]
    }
  ]
})

export default router