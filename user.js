import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()

  const token = ref(null)
  const userPk = ref(null)
  const userName = ref(null)
  const errors = ref(null)
  const isSignUp = ref(false) // 회원가입 후 바로 로그인하기 위한 플래그 변수

  const isLogin = computed(() => {
    if (token.value === null) {
      userPk.value = null
      userName.value = null
      return false
    } else {
      getUserInfo()
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
        errors.value = err.response.data
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
      .then((res) => {
        getUserProfile()
      })
      .catch((err) => {
        errors.value = err.response.data
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

  const getUserInfo = function () {
    axios({
      method: 'get',
      url: `${API_URL}/users/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        userPk.value = res.data.id
        userName.value = res.data.username
        // console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { API_URL, token, isLogin, userPk, userName, errors, singUp, logIn, logOut, getUserInfo }
}, { persist: true })