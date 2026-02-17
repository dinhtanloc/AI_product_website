import { createRouter, createWebHistory } from 'vue-router'

import Login from '@/features/auth/pages/Login.vue'
import Register from '@/features/auth/pages/Register.vue'
import Home from '@/features/home/pages/Home.vue'
import Chat from '@/features/chat/pages/Chat.vue'
import Profile from '@/features/profile/pages/ProfilePage.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/login', component: Login },
    { path: '/register', component: Register },
    {
      path: '/',
      component: Home,
      children: [
        { path: '', component: Chat },
        { path: 'profile', component: Profile }
      ]
    }
  ]
})

router.beforeEach((to) => {
  const token = localStorage.getItem('token')
  if (!token && to.path !== '/login' && to.path !== '/register') {
    return '/login'
  }
})

export default router
