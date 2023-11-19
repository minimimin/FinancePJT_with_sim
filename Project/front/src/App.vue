<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'main' }">Main</RouterLink> |
      <RouterLink :to="{ name: 'articles' }">Community</RouterLink> |
      
      <div v-show="!userStore.isLogin"> 
        <RouterLink :to="{ name: 'signup' }">SignUp</RouterLink> |
        <RouterLink :to="{ name: 'login' }">LogIn</RouterLink> |
        <RouterLink :to="{ name: 'profile' }">Profile</RouterLink> |
        <RouterLink :to="{ name: 'categoryCreate' }">CategoryCreate</RouterLink> |
      </div>
      <div v-show="userStore.isLogin">
        <button @click="userStore.logOut">LogOut</button> |
      </div>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

</script>

<style scoped>
</style>

<style>
/* 모든 파일에 적용할 CSS */
</style>