import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LogIn from '../views/LogIn.vue'
import Register from '../views/register.vue'
import ActiveEmail from '../views/activeEmail.vue'
import forgetPass from '../views/forgetPass.vue'
import sendForgetPass from '../views/sendForgetPass.vue'
import ProductDetails from '../views/ProductDetails.vue'
import Search from '../views/Search.vue'
import Category from '../views/category.vue'
import postInfo from '../views/postInfo.vue'
import panelAdmin from '../views/panelAdmin.vue'
import phoneNumberPanelAdmin from '../views/phoneNumberPanelAdmin.vue'
import changePasswordPanelAdmin from '../views/changePasswordPanelAdmin.vue'

import Cart from '../views/cart.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },

  {
    path: '/log-in',
    name : 'LogIn',
    component: LogIn
  },
  {
    path: '/register',
    name : 'Register',
    component: Register
  },
  {
    path: '/sendForgetPass',
    name : 'sendForgetPass',
    component: sendForgetPass
  },
  {
    path: '/activate/:uid/:token/',
    name : 'ActiveEmail',
    component: ActiveEmail
  },
  {
    path: '/products/:product_id/:product_title/',
    name : 'ProductDetails',
    component: ProductDetails
  },
  {
    path: '/password/reset/confirm/:uid/:token/',
    name : 'forgetPass',
    component: forgetPass
  },
  {
    path: '/search',
    name : 'Search',
    component: Search
  },
  {
    path: '/cart',
    name : 'Cart',
    component: Cart
  },
  {
    path: '/category',
    name : 'Category',
    component: Category
  },
  {
    path: '/postInfo',
    name : 'postInfo',
    component: postInfo
  },
  {
    path: '/panelAdmin',
    name : 'panelAdmin',
    component: panelAdmin
  },
  {
    path: '/phoneNumberPanelAdmin',
    name : 'phoneNumberPanelAdmin',
    component: phoneNumberPanelAdmin
  },
  {
    path: '/changePasswordPanelAdmin',
    name : 'changePasswordPanelAdmin',
    component: changePasswordPanelAdmin
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
