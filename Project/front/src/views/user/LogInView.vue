<template>
  <div>
    <h1>로그인 페이지</h1>
    <form @submit.prevent="logIn">
      <label for="username">아이디 : </label>
      <input type="text" id="username" v-model.trim="username"><br>
      <label for="password">패스워드 : </label>
      <input type="password" id="password" v-model.trim="password"><br>
      <div v-if="store.errors && store.errors.non_field_errors">
        <p v-for="error in store.errors.non_field_errors" :key="error">{{ error }}</p>
      </div>
      <input type="submit" value="로그인">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { onBeforeRouteLeave } from 'vue-router'
import { useUserStore } from '@/stores/user'

const store = useUserStore()
const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}

onBeforeRouteLeave((to, from) => {
  store.errors = null
})
</script>

<style>

</style>
