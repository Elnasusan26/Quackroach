import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'

// 1. Create the application instance FIRST
const app = createApp(App)

// 2. Add the router to the app instance
app.use(router)

// 3. Mount it to the DOM LAST
app.mount('#app')