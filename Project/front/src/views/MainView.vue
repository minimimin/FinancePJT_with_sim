<template>
  <div>
    <h1>메인 페이지</h1>
    <h2 v-if="store.isLogin">{{ store.userName }}님 안녕하세요!</h2>
    <h2 v-else>로그인이 필요합니다.</h2>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user'

const store = useUserStore()

// onMounted(() => {
//   store.getUserInfo()
// })
</script>

<style scoped>

</style>