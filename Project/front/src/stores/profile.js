import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useUserStore } from '@/stores/user'
import axios from 'axios'

export const useProfileStore = defineStore('profile', () => {
  const userStore = useUserStore()
  const banks = ref([
    // 장고에서 은행 가지고 오기!
    {name:'국민은행', id:1 }, 
    {name:'신한은행', id:2 }, 
    {name:'카카오뱅크', id:3 }, 
    {name:'토스', id:4 }, 
    {name:'하나은행', id:5 }
  ])
  const profile = ref([])

  const getProfile = function () {
    axios({
      method: 'get',
      url: `${userStore.API_URL}/users/profile/${userStore.userPk}/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
      .then((res) =>{
        console.log(res.data)
        profile.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const isValue = computed(() => {
    if (profile.value) {
      return true
    } else
      return false
    })

  return { banks, profile, getProfile, isValue }
})