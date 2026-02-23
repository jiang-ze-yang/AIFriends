import HomePageIcon from '@/components/navbar/icons/HomepageIcon.vue'
import CreateIndex from '@/views/create/CreateIndex.vue'
import NotFoundIndex from '@/views/error/NotFoundIndex.vue'
import FriendIndex from '@/views/friend/FriendIndex.vue'
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
      component: HomePageIcon,
      name: 'homepage-index',  
    },
    {
      path: '/create/',
      component: CreateIndex,
      name: 'create-index',  
    },
    {
      path: '/error/',
      component: NotFoundIndex,
      name: '404-index',  
    },
    {
      path: '/friend/',
      component: FriendIndex,
      name: 'friend-index',  
    },
    {
      path: '/user/profile/',
      component: ProfileIndex,
      name: 'user-profile-index',  
    },
    {
      path: '/user/account/login/',
      component: LoginIndex,
      name: 'login-index',  
    },
    {
      path: '/user/account/register/',
      component: RegisterIndex,
      name: 'register-index',  
    },
    {
      path: '/user/space/:user_id/',
      component: SpaceIndex,
      name: 'user-space-index',  
    },
    {
      path:'/:pathMatch(.*)*',
      component: NotFoundIndex,
      name: 'not-found',
    },
  ],
})

export default router
