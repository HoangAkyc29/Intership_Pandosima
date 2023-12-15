import { createRouter, createWebHistory } from 'vue-router';
import Register from '../components/Register/Register.vue';

const routes = [
  // Other routes if any
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
];

const router = createRouter({ history: createWebHistory(), routes });

export default router;
