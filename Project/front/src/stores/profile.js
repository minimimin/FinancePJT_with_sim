import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRoute } from 'vue-router'
import { useUserStore } from './user'

export const useProfileStore = defineStore('profile', () => {
  const bank = ref([
    // 장고에서 은행 가지고 오기!
    // {name:'국민은행', id:1 }, 
    // {name:'신한은행', id:2 }, 
    // {name:'카카오뱅크', id:3 }, 
    // {name:'토스', id:4 }, 
    // {name:'하나은행', id:5 }
  ])

  // const API_URL = 'http://127.0.0.1:8000'
  const route = useRoute()
  const profile = ref([])
  const store = useUserStore()
  // const token = store.token.value

// stores/User 에서 token이랑 인증키랑 isLogin 받아와야할 거 같은데..!??!
// const token = ref(키 값 필 요)

// 일단 그냥 만들고 추가해야하면 추가하자!

// DRF에 profile 조회 요청을 보내는 action
const getProfile = function() {
  axios({
    method: 'get',
    url: `${store.API_URL}/profile/${route.params.user_pk}/`,
    // 장고 주소 입력하는 곳인데 어떻게 유저 pk를 가지고 와서 입력할지??
    headers:{
      Authorization: `Token ${store.token.value}`
    }
    // 장고한테 인증받기위해서 토큰도 같이 보내기
  })
    .then((res) =>{
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

  return { API_URL, bank, profile, token, postProfile, getProfile }
})