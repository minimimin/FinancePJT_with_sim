<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="logIn">
      <div class="select-box">
        <label style="margin: 10px;" for="username">아이디 : </label>
        <input class="select-style" type="text" id="username" v-model.trim="username"><br>
      </div>
      <div>
        <label style="margin: 5px;"  for="password">패스워드 : </label>
        <input class="select-style"  type="password" id="password" v-model.trim="password"><br>
      </div>
      <div v-if="store.errors && store.errors.non_field_errors">
        <p v-for="error in store.errors.non_field_errors" :key="error">{{ error }}</p>
      </div>
      <input class="btn submit-btn" type="submit" value="로그인">
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
