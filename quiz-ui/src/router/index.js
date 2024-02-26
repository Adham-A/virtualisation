// router.js

import { createRouter, createWebHistory } from 'vue-router';
import FadeTransition from '@/components/FadeTransition.vue'; // Adjust the import path based on your directory structure

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: FadeTransition,
      children: [{ path: '', name: 'HomePage', component: () => import('../views/user/HomePage.vue') }],
      meta: {
        transitionComponent: () => import('../views/user/HomePage.vue'),
      },
    },
    {
      path: '/new-quiz-page',
      component: FadeTransition,
      children: [{ path: '', name: 'NewQuizPage', component: () => import('../views/user/NewQuizPage.vue') }],
      meta: {
        transitionComponent: () => import('../views/user/NewQuizPage.vue'),
      },
    },
    {
      path: '/quiz-page',
      component: FadeTransition,
      children: [{ path: '', name: 'QuizPage', component: () => import('../views/user/QuizPage.vue') }],
      meta: {
        transitionComponent: () => import('../views/user/QuizPage.vue'),
      },
    },
    {
      path: '/result-page',
      component: FadeTransition,
      children: [{ path: '', name: 'ResultPage', component: () => import('../views/user/ResultPage.vue') }],
      meta: {
        transitionComponent: () => import('../views/user/ResultPage.vue'),
      },
    },
    {
      path: '/cgus',
      component: FadeTransition,
      children: [{ path: '', name: 'CGUs', component: () => import('../views/user/CGUs.vue') }],
      meta: {
        transitionComponent: () => import('../views/user/CGUs.vue'),
      },
    },
    {
      path: '/login',
      component: FadeTransition,
      children: [{ path: '', name: 'Login', component: () => import('../views/admin/LoginPage.vue') }],
      meta: {
        transitionComponent: () => import('../views/admin/LoginPage.vue'),
      },
    },
    {
      path: '/admin-page',
      component: FadeTransition,
      children: [{ path: '', name: 'admin-page', component: () => import('../views/admin/AdminPage.vue') }],
      meta: {
        transitionComponent: () => import('../views/admin/AdminPage.vue'),
      },
    },
    {
      path: '/question-list-page',
      component: FadeTransition,
      children: [
        { path: '', name: 'question-list-page', component: () => import('../views/admin/QuestionListPage.vue') },
      ],
      meta: {
        transitionComponent: () => import('../views/admin/QuestionListPage.vue'),
      },
    },
  ],
});

export default router;
