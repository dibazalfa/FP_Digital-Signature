import { createRouter, createWebHistory } from 'vue-router'
import CA from '../views/CA_Generate-Key.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'ca',
      component: CA
    },
    {
      path: '/sign',
      name: 'sign',
      component: () => import('../views/CA_Digital-Sign.vue')
    },
    {
      path: '/validator',
      name: 'validator',
      component: () => import('../views/Validator.vue')
    },
    {
      path: '/coba',
      name: 'coba',
      component: () => import('../views/coba.vue')
    }
  ]
})

export default router
