<template>
  <div>
    <h1>프로필</h1>
    <!--pk번 유저의 프로필로 이동!-->
    <button @click="goProfileCreate()">프로필 생성하기</button>
  
  </div>
  <RouterView />
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goProfileCreate = function() {
  router.push({ name:'profileCreate' })
}

</script>

<style scoped>

</style>