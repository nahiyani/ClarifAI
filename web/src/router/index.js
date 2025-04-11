import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import Transcribe from '../pages/Transcribe.vue'
import Summarize from '../pages/Summarize.vue'
import Contact from '../pages/Contact.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/transcribe', name: 'Transcribe', component: Transcribe },
  { path: '/summarize', name: 'Summarize', component: Summarize },
  { path: '/contact', name: 'Contact', component: Contact },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router