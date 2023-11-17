<template>
  <div>
    <h1>메인 페이지</h1>
    <button @click="getUserPk">test</button>
    <h2 v-if="store.isLogin">안녕하세요.</h2>
    <h2 v-else>로그인이 필요합니다.</h2>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'

const store = useUserStore()

const getUserPk = function () {
  store.getUserPk()
}

</script>

<style scoped>

</style>