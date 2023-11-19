<template>
  <div>
    <!--프로필 페이지에서 값 가지고 와서 수정할 수 있도록 하기-->
    <h1>{{ username }}님의 PROFILE 수정 페이지</h1>
    <hr>
    <p>변경된 정보를 수정해주세요.</p>
    <!--age, money, salary, job, main_bank, 
      stabillity, banking_products, card_products-->
    <form @submit.prevent="updateProfile">
    <!-- <form> -->

      <label for="age">나이</label><br>
      <input type="number" id="age" v-model.trim='age' min=0 max=200>
      
      <br>
      <br>
      
      <label for="money">자산</label>
      <br>
      <input type="number" id="money" v-model.trim='money'>
      <!-- <input type="submit"> -->
      <br>
      <br>

      <label for="salary">연봉</label>
      <br>
      <input type="number" id="salary" v-model.trim='salary'>
      
      <br>
      <button @click="submit">제출</button>
    </form>
  </div>
</template>

<script setup>
// 디폴트로 기존 값을 입력되도록 하고,
// 그걸 수정해서 저장(post로 똑같이 보내기)하기
import { useUserStore } from '@/stores/user'
import { useProfileStore } from '@/stores/profile'
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import axios from 'axios'

const router = useRouter()
const useStore = useUserStore()
const profileStore = useProfileStore()

const API_URL = useStore.API_URL
const user_pk = useStore.userPk
const username = useStore.userName

const age = ref(profileStore.profile.age)
const money = ref(profileStore.profile.money)
const salary = ref(profileStore.profile.salary)

const updateProfile = function () {
      axios({
      method:'put',
      url:`${API_URL}/users/profile/${user_pk}/`,
      data:{
        age: age.value, 
        money: money.value, 
        salary: salary.value,
      },
      headers: {
        Authorization: `Token ${useStore.token}`
      }
    })
      .then((response) => {
        console.log('good')
        router.push({ name: 'profile' })
        
      })
      .catch((error) => {
        console.log(error)
      })
      return {

      }
    }
</script>

<style scoped>

</style>