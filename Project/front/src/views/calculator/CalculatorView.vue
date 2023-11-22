<template>
  <div>
    <h1>계산기 페이지</h1>
    <RouterLink :to="{ name: 'exchange' }">환율계산기</RouterLink>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'

</script>

<style scoped>

</style>