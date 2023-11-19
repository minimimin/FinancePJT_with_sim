<template>
  <div>
    <h1>{{ username }}님의 PROFILE</h1>
    <hr>
    <p>상세 정보를 입력해주세요.</p>
    <!--age, money, salary, job, main_bank, 
      stabillity, banking_products, card_products-->
    <form @submit.prevent="createProfile">

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

      <div>
        <legend>직업</legend>
        <div>
          <input type="radio" id="학생 및 주부" name="job" v-model.trim='selectedJobValue' value="학생 및 주부" />
          <label for="학생 및 주부">학생 및 주부</label>
        </div>

        <div>
          <input type="radio" id="사업가 및 프리랜서" name="job" v-model.trim='selectedJobValue' value="사업가 및 프리랜서" />
          <label for="사업가 및 프리랜서">사업가 및 프리랜서</label>
        </div>

        <div>
          <input type="radio" id="회사원" name="job" v-model.trim='selectedJobValue' value="회사원" />
          <label for="회사원">회사원</label>
        </div>

        <div>
          <input type="radio" id="기타" name="job" value="기타" onchange="toggleTextField()"/> 
          <label for="기타">기타</label>
          <input type="text" id="기타TextField" v-model.trim='selectedJobValue' disabled>
        </div>
      </div>


      <!-- <label for="job">직업 : </label>
      <div id="job">
        <input type="radio">
      </div> -->

      <br>

<!--------------------------------------------------------------------------------------------->
      <label for="main_bank">주거래은행 : </label><br>
      <select id="main_bank" v-model="mainBank">
      <!-- <select id="main_bank"> -->
        <option disabled value="">은행을 선택하세요</option>
        <option v-for="bank in profileStore.bank" 
        :key="bank.id" :value="bank.id">{{ bank.name }}</option>
      </select>

      <br>
<!--------------------------------------------------------------------------------------------->

      <br>

  <!-- <label for="stabillity">안정성</label><br>
  <input type="range" id="stabillity" name="stabillity" min="0" max="100"  list="values"> -->
  <!-- <input type="submit" value="Submit"> -->
  <!-- <datalist id="values">
  <option value="0" label="매우 모험 추구(하이 리스크 하이 리턴)"></option>
  <option value="25" label="모험 추구"></option>
  <option value="50" label="보통"></option>
  <option value="75" label="안정 추구"></option>
  <option value="100" label="매우 안정 추구(노 리스트 리를 리턴)"></option>
  </datalist>
  
  <br> -->

<!----------------------------------------------------------------------------------------------->
      
<br>

  <!-- <fieldset>
        <legend>선호하는 은행 상품 유형(모두 선택 가능)</legend>

        <div>
          <input type="checkbox" id="예금" name="예금" checked />
          <label for="예금">예금</label>
        </div>

        <div>
          <input type="checkbox" id="적금" name="적금" />
          <label for="적금">적금</label>
        </div>

        <div>
          <input type="checkbox" id="펀드" name="펀드" />
          <label for="펀드">펀드</label>
        </div>

        <div>
          <input type="checkbox" id="대출" name="대출" />
          <label for="대출">대출</label>
        </div>
      </fieldset> -->

<!---------------------------------------------------------------------------------------------->
      <br>

      <!-- <fieldset>
        <legend>선호하는 카드 유형(하나만 선택)</legend>
        <div>
          <input type="radio" id="신용카드" name="card" value="신용카드" checked />
          <label for="신용카드">신용카드</label>
        </div>

        <div>
          <input type="radio" id="체크카드" name="card" value="체크카드" />
          <label for="체크카드">체크카드</label>
        </div>

        <div>
          <input type="radio" id="카드X" name="card" value="카드X" />
          <label for="카드X">카드를 사용을 희망하지 않음</label>
        </div>
      </fieldset>-->
            
      <br>
      <button @click="submit">제출</button>
      <br>
  </form>
  </div>
</template>


<script setup>
import { useProfileStore } from '@/stores/profile'
import { useUserStore } from '@/stores/user'
import { useRouter, useRoute } from 'vue-router'
import { ref } from 'vue'
import axios from 'axios'

const toggleTextField = function() {
      const radio = document.getElementById('기타')
      const textField = document.getElementById('기타TextField')

      // '기타' 라디오 버튼이 선택되었을 때
      if (radio.checked) {
        textField.disabled = false // 텍스트 필드를 활성화
      } else {
        textField.disabled = true // 텍스트 필드를 비활성화
      }
    }


 //--------------------------------------------------------------------------------------

    const router = useRouter()
    const userStore = useUserStore()
    const profileStore = useProfileStore()


    const age = ref(null)
    const money = ref(null)
    const salary = ref(null)
    // const job = ref(null)
    const mainBank = ref(null)
    // const stabillity = ref(null)
    // const banking_products = ref(null)
    // const card_products = ref(null)
    // const route = useRoute()

    const user_pk = userStore.userPk
    const username = userStore.userName

    const createProfile = function () {
      axios({
      method:'post',
      url:`${userStore.API_URL}/users/profile/${user_pk}/`,
      data:{
        age: age.value, 
        money: money.value, 
        salary: salary.value,
        // job: job.value, 
        main_bank: mainBank.value,
        // stabillity: stabillity.value, 
        // banking_products: banking_products.value, 
        // card_products: card_products.value,
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
    }
</script>

<style scoped>

</style>