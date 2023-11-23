import { createRouter, createWebHistory } from 'vue-router'
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
import CalculatorView from '@/views/calculator/CalculatorView.vue'
import ExchangeView from '@/views/calculator/ExchangeView.vue'
import MapView from '@/views/map/MapView.vue'
import financialProductView from '@/views/financialproduct/financialProductView.vue'
import depositproduct from '@/components/financialProduct/depositproduct.vue'
import DepositproductDetail from '@/components/financialProduct/DepositproductDetail.vue'
import savingproduct from '@/components/financialProduct/savingproduct.vue'
import SavingproductDetail from '@/components/financialProduct/SavingproductDetail.vue'
import loanhome from '@/components/financialProduct/loanhome.vue'
import LoanhomeDetail from '@/components/financialProduct/LoanhomeDetail.vue'
import financialProductRecommendView from '@/views/financialproduct/financialProductRecommendView.vue'

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
      path: '/profile/',
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
    // calculator 관련
    {
      path: '/calculator',
      name: 'calculator',
      component: CalculatorView
    },
    {
      path: '/calculator/exchange/',
      name: 'exchange',
      component: ExchangeView
    },
    // map 관련
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    // financial_product 관련
    {
      path: '/financialproduct/',
      name: 'financialProduct',
      component: financialProductView
    },
    {
      path: '/financialproduct/deposit/',
      name: 'depositProduct',
      component: depositproduct
    },
    {
      path: '/financialproduct/deposit/:deposit_id/',
      name: 'depositProductDetail',
      component: DepositproductDetail
    },
    {
      path: '/financialproduct/saving/',
      name: 'savingProduct',
      component: savingproduct
    },
    {
      path: '/financialproduct/saving/:saving_id/',
      name: 'savingProductDetail',
      component: SavingproductDetail
    },
    {
      path: '/financialproduct/loanhome/',
      name: 'loanhome',
      component: loanhome
    },
    {
      path: '/financialproduct/loanhome/:loan_id/',
      name: 'loanhomeDetail',
      component: LoanhomeDetail
    },
    {
      path: '/financialproduct/recommend/',
      name: 'recommend',
      component: financialProductRecommendView
    },
  ]
})


export default router