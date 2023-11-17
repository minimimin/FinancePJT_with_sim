<template>
  <div>
    <h1>{{ username }}님의 프로필</h1>
    <!--프로필이 있다면 보여주기 + 수정하기 페이지로 이동할 수 있도록 만들기-->
    <button @click="updateprofile()">프로필 수정하기</button>
    <p>나이 : {{ store.profile.age }}</p>


    <!--프로필이 없다면 프로필 생성페이지로 이동!-->
    <br>
    <h4>아직 프로필이 등록되지 않았습니다. <br>
      프로필을 작성해주세요.</h4>
    <button @click="goProfileCreate()">프로필 생성하기</button>
  
  </div>
  <RouterView />
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goProfileCreate = function() {
  router.push({ name:'profileCreate' })
}

import { onMounted } from 'vue'
import { useProfileStore } from '@/stores/profile'
import { useUserStore } from '../../stores/user'

const store = useProfileStore()
// const stores = useUserStore()
const user_pk = store.userPk
const username = store.userName

// 바로바로 정보 가지고 오기
onMounted(() => {
  store.getProfile()
})

// defineProps({
//   profileDetail: Object
// })


const updateprofile = function () {
    router.push({ name:'profileUpdate' })
  }
</script>

<style scoped>

</style>