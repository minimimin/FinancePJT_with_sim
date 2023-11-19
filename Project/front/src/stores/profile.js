import { ref, computed } from 'vue'
// import { useRoute } from 'vue-router'
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

// back의 모델에 설정된 필드들! 이걸 가지고 던져줘야한다!
    // email = models.EmailField(max_length=254, null=True)
    // age = models.IntegerField(null=True)
    // money = models.IntegerField(null=True)
    // salary = models.IntegerField(null=True)
    // job = models.CharField(max_length=30, null=True)
    // main_bank = models.TextField(null=True)

    // # 유저 성향 관련 필드
    // stability = models.TextField(null=True)
    // banking_products = models.TextField(null=True)
    // card_products = models.TextField(null=True)

  return { banks, profile, getProfile, isValue }
})