<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'main' }">Main</RouterLink> |
      <RouterLink :to="{ name: 'community' }">Community</RouterLink> |
      <RouterLink :to="{ name: 'profile' }">Profile</RouterLink> |
      <RouterLink :to="{ name: 'signup' }">SignUp</RouterLink> |
      <RouterLink :to="{ name: 'login' }">LogIn</RouterLink> |
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>
</style>
