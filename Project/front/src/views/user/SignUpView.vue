<template>
  <div>
    <h1>회원가입 페이지</h1>
    <form @submit.prevent="signUp">
      <label for="username">아이디 : </label>
      <input type="text" id="username" v-model.trim="username">
      <div v-if="store.errors && store.errors.username">
        <p v-for="error in store.errors.username" :key="error">{{ error }}</p>
      </div>
      <br>

      <label for="password1">패스워드 : </label>
      <input type="password" id="password1" v-model.trim="password1">
      <div v-if="store.errors && store.errors.password1">
        <p v-for="error in store.errors.password1" :key="error">{{ error }}</p>
      </div>
      <br>

      <label for="password2">패스워드 확인 : </label>
      <input type="password" id="password2" v-model.trim="password2">
      <div v-if="store.errors && store.errors.non_field_errors">
        <p v-for="error in store.errors.non_field_errors" :key="error">{{ error }}</p>
      </div>
      <br>
      <input type="submit" value="회원가입">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { onBeforeRouteLeave } from 'vue-router'
import { useUserStore } from '@/stores/user'

const store = useUserStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.singUp(payload)
}

onBeforeRouteLeave((to, from) => {
  store.errors = null
})
</script>

<style>

</style>
