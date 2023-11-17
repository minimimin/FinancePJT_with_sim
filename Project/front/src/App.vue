<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'main' }">Main</RouterLink> |
      <RouterLink :to="{ name: 'articles' }">Community</RouterLink> |
      <RouterLink :to="{ name: 'profile' }">Profile</RouterLink> |
      <RouterLink :to="{ name: 'signup' }">SignUp</RouterLink> |
      <RouterLink :to="{ name: 'login' }">LogIn</RouterLink> |
      <button @click="store.logOut">LogOut</button> |
      <RouterLink :to="{ name: 'categoryCreate' }">CategoryCreate</RouterLink> |
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useUserStore } from '@/stores/user'

const store = useUserStore()

</script>

<style scoped>
</style>

<style>
/* 모든 파일에 적용할 CSS */
</style>