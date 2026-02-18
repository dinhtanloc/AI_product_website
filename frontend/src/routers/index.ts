import { createRouter, createWebHistory } from 'vue-router'

import Login from '@/features/auth/pages/Login.vue'
import Register from '@/features/auth/pages/Register.vue'
import Home from '@/features/home/pages/Home.vue'
import Chat from '@/features/chat/pages/Chat.vue'
import Profile from '@/features/profile/pages/ProfilePage.vue'
import ImageGeneration from '@/features/image/pages/ImageGeneration.vue'
import VideoDetection from '@/features/video/pages/VideoDetection.vue'
import ImageSegmentation from '@/features/image/pages/ImageSegmentation.vue'
import SpeechRecognition from '@/features/speech/pages/SpeechRecognition.vue'

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
        { path: 'profile', component: Profile },
        { path: 'image-generation', component: ImageGeneration },
        { path: 'image-segmentation', component: ImageSegmentation },
        { path: 'speech-recognition', component: SpeechRecognition },
        { path: 'video-detection', component: VideoDetection }
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
