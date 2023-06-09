import { createRouter, createWebHistory } from 'vue-router'
import CA from '../views/CA_Generate-Key.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/front/Home.vue')
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/front/About.vue')
    },
    // {
    //   path: '/sign',
    //   name: 'sign',
    //   component: () => import('../views/CA_Digital-Sign.vue')
    // },
    {
      path: '/validator',
      name: 'validator',
      component: () => import('../views/Validator.vue')
    },
    {
      path: '/generate',
      name: 'generate',
      component: () => import('../views/GenerateKey.vue')
    },
    {
      path: '/ds',
      name: 'ds',
      component: () => import('../views/DigitalSign.vue')
    },
    // {
    //   path: '/coba',
    //   name: 'coba',
    //   component: () => import('../views/coba.vue')
    // },
    // {
    //   path: '/generate',
    //   name: 'generate',
    //   component: () => import('../views/CA_Generate-Key.vue')
    // }
  ]
})

export default router
