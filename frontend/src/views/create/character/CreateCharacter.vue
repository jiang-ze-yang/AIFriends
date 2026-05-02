<script setup>
import { useTemplateRef, ref, onMounted } from 'vue';
import BackgroundImage from './components/BackgroundImage.vue';
import Name from './components/Name.vue';
import Photo from './components/Photo.vue';
import Profile from './components/Profile.vue';
import { base64ToFile } from '@/js/utils/base64_to_file';
import api from '@/js/http/api.js';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';
import Voice from './components/Voice.vue';

const user = useUserStore()
const router = useRouter()

const photoRef = useTemplateRef('photo-ref')
const nameRef = useTemplateRef('name-ref')
const voiceRef = useTemplateRef('voice-ref')
const profileRef = useTemplateRef('profile-ref')
const backgroundImageRef = useTemplateRef('background-image-ref')
const errorMessage = ref('')

const voices = ref([])
const curVoiceId = ref(null)

onMounted(async () => {
    try{
        const res = await api.get('/api/create/character/voice/get_list/', {})
        const data = res.data
        if(data.result === 'success'){
            voices.value = data.voices
            curVoiceId.value = data.voices[0].id
        }
    }
    catch(err){
        console.error('Failed to fetch voices:', err)
    }
})

async function handleCreate(){
    const photo = photoRef.value.myPhoto
    const name = nameRef.value.myName?.trim()
    const voice = voiceRef.value.myVoice
    const profile = profileRef.value.myProfile?.trim()
    const backgroundImage = backgroundImageRef.value.myBackgroundImage
    errorMessage.value = ''
    if(!photo){
        errorMessage.value = '请上传角色照片'
        return
    }else if(!name){
        errorMessage.value = '请输入角色名称'
        return
    }else if(!voice){
        errorMessage.value = '请选择角色音色'
        return
    }
    else if(!profile){
        errorMessage.value = '请输入角色简介' 
    }else if(!backgroundImage){
        errorMessage.value = '请上传角色背景图'
    }else{
        const formData = new FormData()
        formData.append('name', name)
        formData.append('voice_id', voice)
        formData.append('profile', profile)
        formData.append('photo', base64ToFile(photo, 'photo.png'))
        formData.append('background_image', base64ToFile(backgroundImage, 'background_image.png'))
        try{
            const res = await api.post('/api/create/character/create/', formData)
            const data = res.data
            if(data.result === 'success'){
                await router.push({
                    name: 'user-space-index',
                    params: { 
                        user_id: user.id,
                    }
                })
            }else{
                errorMessage.value = data.result
            }
        }
        catch(err){
        }
    }
}

</script>

<template>
    <div class="flex justify-center">
        <div class="card w-120 bg-base-200 shadow-sm mt-16">
            <div class="card-body">
                <h3 class="text-lg font-bold my-4">创建角色</h3>
                <Photo ref="photo-ref" />
                <Name ref="name-ref" />
                <Voice ref="voice-ref" :voices="voices" :curVoiceId="curVoiceId" />
                <Profile ref="profile-ref" />
                <BackgroundImage ref="background-image-ref" />

                <p v-if="errorMessage" class="text-sm text-red-500">{{ errorMessage }}</p>

                <div class="flex justify-center">
                    <button @click="handleCreate" class="btn btn-neutral w-60 mt-2">创建角色</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>