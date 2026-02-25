<script setup>
import { onMounted } from 'vue';
import NavBar from './components/navbar/NavBar.vue';
import { useUserStore } from './stores/user';
import api from '@/js/http/api.js';
import { useRoute, useRouter } from 'vue-router';

const user = useUserStore();
const route = useRoute();
const router = useRouter();

onMounted(async () => {
    try{
        const res = await api.get("/api/user/account/get_user_info/");
        const data = res.data;
        if(data.result == 'success'){
            user.setUserInfo(data);
        }
    }catch(error){
        //console.log(error)
    }finally{
        user.setHasPulledUserInfo(true);

        if(route.meta.needLogin && !user.isLogin()){
            await router.replace({
                name: 'login-index',

            })
        }
    }
});

</script>

<template>
<NavBar>
    <router-view></router-view>
</NavBar>
</template>

<style scoped>

</style>
