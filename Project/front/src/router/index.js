import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'
import MainView from '@/views/MainView.vue'
import ArticleView from '@/views/article/ArticleView.vue'
import ArticleCreateView from '@/views/article/ArticleCreateView.vue'
import ArticleDetailView from '@/views/article/ArticleDetailView.vue'
import ArticleUpdateView from '@/views/article/ArticleUpdateView.vue'
import CategoryCreateView from '@/views/article/CategoryCreateView.vue'
import ProfileView from '@/views/profile/ProfileView.vue'
import ProfileCreateView from '@/views/profile/ProfileCreateView.vue'
import ProfileUpdateView from '@/views/profile/ProfileUpdateView.vue'
import SignUpView from '@/views/user/SignUpView.vue'
import LogInView from '@/views/user/LogInView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    // article 관련
    {
      path: '/community',
      name: 'articles',
      component: ArticleView
    },
    {
      path: '/community/create',
      name: 'articleCreate',
      component: ArticleCreateView
    },
    {
      path: '/community/:id',
      name: 'articleDetail',
      component: ArticleDetailView
    },
    {
      path: '/community/:id/update',
      name: 'articleUpdate',
      component: ArticleUpdateView
    },
    {
      path: '/category/create',
      name: 'categoryCreate',
      component: CategoryCreateView
    },
    // user 관련
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/profile/create/',
      name: 'profileCreate',
      component: ProfileCreateView
    },
		{
      path: '/profile/update/',
      name: 'profileUpdate',
      component: ProfileUpdateView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView
    },
  ]
})


// router.beforeEach((to, from) => {
//   const store = useUserStore()
//   if (to.name === 'ArticleView' && !store.isLogin) {
//     window.alert('로그인이 필요합니다.')
//     return { name: 'LogInView' }
//   }
//   if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
//     window.alert('이미 로그인 했습니다.')
//     return { name: 'ArticleView' }
//   }
// })


// beforeEnter: (to, from) => {
//   const store = useArticleStore()
//   if (store.isSignin) {
//     return { name: 'home' }
//   }
// }

export default router