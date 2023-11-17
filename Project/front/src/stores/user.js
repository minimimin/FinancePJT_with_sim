import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()
  const isSignUp = ref(false)
  const userPk = ref(null)
  const userName = ref(null)

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const singUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2,
      },
    })
      .then((res) => {
        const password = password1
        isSignUp.value = true
        logIn({ username, password, isSignUp })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = function (payload) {
    const { username, password, isSignUp } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password,
      }
    })
      .then((res) => {
        token.value = res.data.key
        if (isSignUp) {
          isSignUp.value = false
          router.push({ name: 'main' })
        } else {
          history.back()
        }
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        token.value = null
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getUserPk = function () {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/user/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        userPk.value = res.data.pk
        userName.value = res.data.username
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { API_URL, token, isLogin, userPk, userName, singUp, logIn, logOut, getUserPk }
}, { persist: true })