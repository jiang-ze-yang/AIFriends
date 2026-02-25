
import { useUserStore } from '@/stores/user'
import CreateIndex from '@/views/create/CreateIndex.vue'
import NotFoundIndex from '@/views/error/NotFoundIndex.vue'
import FriendIndex from '@/views/friend/FriendIndex.vue'
import HomepageIndex from '@/views/homepage/HomepageIndex.vue'
import ProfileIndex from '@/views/profile/ProfileIndex.vue'
import LoginIndex from '@/views/user/account/LoginIndex.vue'
import RegisterIndex from '@/views/user/account/RegisterIndex.vue'
import SpaceIndex from '@/views/user/space/SpaceIndex.vue'
import { createRouter, createWebHistory } from 'vue-router'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: HomepageIndex,
      name: 'homepage-index',  
      meta:{
        needLogin: false,
      },
    },
    {
      path: '/create/',
      component: CreateIndex,
      name: 'create-index',  
        meta:{ 
        needLogin: true,
      },
    },
    {
      path: '/error/',
      component: NotFoundIndex,
      name: '404-index',
        meta:{ 
        needLogin: false,
      },  
    },
    {
      path: '/friend/',
      component: FriendIndex,
      name: 'friend-index',  
      meta:{
        needLogin: true,
      },
    },
    {
      path: '/user/profile/',
      component: ProfileIndex,
      name: 'user-profile-index',  
      meta:{
        needLogin: true,
      },
    },
    {
      path: '/user/account/login/',
      component: LoginIndex,
      name: 'login-index',  
      meta:{
        needLogin: false,
      },
    },
    {
      path: '/user/account/register/',
      component: RegisterIndex,
      name: 'register-index',  
      meta:{
        needLogin: false,
      },
    },
    {
      path: '/user/space/:user_id/',
      component: SpaceIndex,
      name: 'user-space-index',  
      meta:{
        needLogin: false,
      },
    },
    {
      path:'/:pathMatch(.*)*',
      component: NotFoundIndex,
      name: 'not-found',
      meta:{
        needLogin: false,
      },
    },
  ],
})

router.beforeEach((to, from) => {
  const user = useUserStore()
  if(to.meta.needLogin && user.hasPulledUserInfo && !user.isLogin()){
    return {
      name: 'login-index'
    }
  }
  return true
})

export default router
