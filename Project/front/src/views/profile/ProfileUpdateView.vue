<template>
  <div>
    <h1>{{ username }}님의 PROFILE 수정 페이지</h1>
    <hr>
    <p>정보를 수정해주세요.</p>
    <!--age, money, salary, job, main_bank, 
      stabillity, banking_products, card_products-->
    <form @submit.prevent="updateProfile">

      <label for="age">나이</label><br>
      <input type="number" id="age" v-model.trim='age' min=0 max=200>
      
      <br>
      <br>
      
      <label for="money">자산</label>
      <br>
      <input type="number" id="money" v-model.trim='money'>
      <br>
      <br>

      <label for="salary">연봉</label>
      <br>
      <input type="number" id="salary" v-model.trim='salary'>
      <br>
      <br>

      <label for="main_bank">주거래은행 : </label><br>
      <select id="main_bank" v-model="mainBank">
        <option disabled value="">은행을 선택하세요</option>
        <option v-for="bank in profileStore.banks" 
        :key="bank.id" :value="bank.name">{{ bank.name }}</option>
        <!--일단 보여지기 위해서 name을 보내는데, 나중에는 id를 보내고 이름을 보여지게 하는 것으로!-->
      </select>
      <br>
      <br>
      <button @click="submit">제출</button>
      <br>

    </form>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'
import { useProfileStore } from '@/stores/profile'
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import axios from 'axios'

const router = useRouter()
const userStore = useUserStore()
const profileStore = useProfileStore()

const API_URL = userStore.API_URL
const user_pk = userStore.userPk
const username = userStore.userName

const age = ref(profileStore.profile.age)
const money = ref(profileStore.profile.money)
const salary = ref(profileStore.profile.salary)
const mainBank = ref(profileStore.profile.main_bank)

const updateProfile = function () {
      axios({
      method:'put',
      url:`${API_URL}/users/profile/${user_pk}/`,
      data:{
        age: age.value, 
        money: money.value, 
        salary: salary.value,
        main_bank: mainBank.value, 
      },
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
      .then((response) => {
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