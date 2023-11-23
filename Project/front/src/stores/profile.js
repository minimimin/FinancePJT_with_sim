import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useUserStore } from '@/stores/user'
import axios from 'axios'

export const useProfileStore = defineStore('profile', () => {
  const userStore = useUserStore()
  const banks = ref([
    {name: '우리은행', id: 1}, 
    {name: '한국스탠다드차타드은행', id: 2}, 
    {name: '대구은행', id: 3}, 
    {name: '부산은행', id: 4}, 
    {name: '광주은행', id: 5}, 
    {name: '제주은행', id: 6}, 
    {name: '전북은행', id: 7}, 
    {name: '경남은행', id: 8}, 
    {name: '중소기업은행', id: 9}, 
    {name: '한국산업은행', id: 10}, 
    {name: '국민은행', id: 11}, 
    {name: '신한은행', id: 12}, 
    {name: '농협은행주식회사', id: 13}, 
    {name: '하나은행', id: 14}, 
    {name: '주식회사 케이뱅크', id: 15}, 
    {name: '수협은행', id: 16}, 
    {name: '주식회사 카카오뱅크', id: 17}, 
    {name: '토스뱅크 주식회사', id: 18}]
    // 장고에서 은행 가지고 오기!
    )
  const profile = ref(null)

  const getProfile = function () {
    axios({
      method: 'get',
      url: `${userStore.API_URL}/users/profile/${userStore.userPk}/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
      .then((res) =>{
        // console.log(res.data)
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
}, { persist: true })