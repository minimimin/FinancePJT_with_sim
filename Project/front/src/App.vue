<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'main' }">Main</RouterLink> |
      <RouterLink :to="{ name: 'articles' }">Community</RouterLink> |
      <RouterLink :to="{ name: 'calculator' }">Calculator</RouterLink> |
      <RouterLink :to="{ name: 'map' }">Map</RouterLink> |
      <RouterLink :to="{ name: 'financialProduct' }">Financial Product</RouterLink> |
      
      <div v-if="!userStore.isLogin"> 
        <RouterLink :to="{ name: 'signup' }">SignUp</RouterLink> |
        <RouterLink :to="{ name: 'login' }">LogIn</RouterLink> |
        
      </div>
      <div v-if="userStore.isLogin">
        <button @click="userStore.logOut">LogOut</button> |
        <RouterLink :to="{ name: 'profile' }">Profile</RouterLink> |
        <div v-if="userStore.isLogin && userStore.loginUser.is_superuser">
          <RouterLink :to="{ name: 'categoryCreate' }">CategoryCreate</RouterLink> |
        </div>
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