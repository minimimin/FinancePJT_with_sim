import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { defineStore } from 'pinia'
import { useUserStore } from '@/stores/user'
import axios from 'axios'

export const useProfileStore = defineStore('profile', () => {
  const userStore = useUserStore()
  const bank = ref([
    // 장고에서 은행 가지고 오기!
    // {name:'국민은행', id:1 }, 
    // {name:'신한은행', id:2 }, 
    // {name:'카카오뱅크', id:3 }, 
    // {name:'토스', id:4 }, 
    // {name:'하나은행', id:5 }
  ])
  const profile = ref([])

  // DRF에 profile 조회 요청을 보내는 action
  const getProfile = function () {
    axios({
      method: 'get',
      url: `${userStore.API_URL}/profile/${userStore.userPk}/`,
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

// back의 모델에 설정된 필드들! 이걸 가지고 던져줘야한다!
  // const postProfile = function (profileDetail) {
  //   const { user_pk, age, money, salary, job, main_bank, 
  //     stabillity, banking_products, card_products } = profileDetail
  //     // user_pk를 여기서 받아와도 되는지 모르겠지만,..!

  //   axios({
  //     method:'post',
  //     url:`${API_URL}/profile/${user_pk}/`,
  //     // user_pk를 우선 위에서 받아왔다고 치고, 입력해놓기,,!!
  //     data:{
  //       age, money, salary, job, main_bank, 
  //       stabillity, banking_products, card_products,
  //     }
  //   })
  //     .then((response) => {
  //       console.log(response.data)
  //       profile.value = response.data
        
  //     })
  //     .catch((error) => {
  //       console.log(error)
  //     })
  // }

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

// back에 설정된 url은 user_pk도 있기때문에 그걸 받아와서 보내야한다!

  return { bank, profile, getProfile }
})