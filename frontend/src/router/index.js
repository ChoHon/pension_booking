import { useAuthStore } from '@/stores/auth';
import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/accounts/LoginView.vue'),
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('../views/accounts/SignupView.vue'),
    },
    {
      path: '/pension',
      name: 'pension',
      component: () => import('../views/pensions/PensionView.vue'),
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/reservation',
      name: 'reservation',
      component: () => import('../views/reservations/ReservationView.vue'),
      meta: {
        requiresAuth: true,
      },
    },
  ],
});

router.beforeEach(async (to, from) => {
  const authStore = useAuthStore();

  const isAuthenticated =
    authStore.access && authStore.refresh
      ? await authStore.checkToken()
      : false;

  authStore.login_status = isAuthenticated;

  if (to.meta?.requiresAuth) {
    if (isAuthenticated) {
      return true;
    } else {
      return { name: 'login' };
    }
  } else {
    return true;
  }
});

export default router;
