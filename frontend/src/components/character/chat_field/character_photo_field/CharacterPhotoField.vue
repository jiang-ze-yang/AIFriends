<script setup>
    defineProps(['character'])
</script>

<template>
    <div class="absolute left-2 right-22 top-6 h-8 w-fit rounded-full bg-black/50 flex items-center gap-2 pr-3">
        <div class="avatar">
            <div class="w-8 h-8 rounded-full"> <img :src="character.photo" alt="avatar" class="object-cover w-full h-full">
            </div>
        </div>
        <div class="text-white text-sm line-clamp-1 break-all">
            {{ character.name }}    
        </div>
    </div>
</template>

<style scoped>

</style>