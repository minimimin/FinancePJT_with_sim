<template>
  <!--프로필이 있다면 보여주기 + 수정하기 페이지로 이동할 수 있도록 만들기-->
  <div  v-if="profileStore.isValue">
    <h1>{{ userStore.userName }}님의 프로필</h1>
    <button @click="updateProfile">프로필 수정하기</button>
    <p>나이 : {{ profileStore.profile.age }}</p>
    <p>자산 : {{ profileStore.profile.money }}</p>
    <p>연봉 : {{ profileStore.profile.salary }}</p>
  </div>

    <!--프로필이 없다면 프로필 생성페이지로 이동!-->
  <div v-else>
    <br>
    <h4>아직 프로필이 등록되지 않았습니다. <br>
      프로필을 작성해주세요.</h4>
    <button @click="goProfileCreate">프로필 생성하기</button>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useProfileStore } from '@/stores/profile'

const router = useRouter()
const userStore = useUserStore()
const profileStore = useProfileStore()

const goProfileCreate = function() {
  router.push({ name: 'profileCreate' })
}

// 이건 데이터가 있을때 바로바로 정보 가지고 오기
// if (profileStore.isValue) {
  onMounted(() => {
  profileStore.getProfile()
})
// }


const updateProfile = function () {
    router.push({ name: 'profileUpdate' })
  }
</script>

<style scoped>

</style>