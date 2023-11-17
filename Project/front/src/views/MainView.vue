<template>
  <div>
    <h1>메인 페이지</h1>
    <button @click="getUserInfo">test</button>
    <h2 v-if="store.isLogin">{{ store.userPk }} {{ store.userName }} 안녕하세요.</h2>
    <h2 v-else>로그인이 필요합니다.</h2>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'

const store = useUserStore()

const getUserInfo = function () {
  store.getUserInfo()
}

</script>

<style scoped>

</style>