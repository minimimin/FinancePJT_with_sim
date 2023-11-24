<template>
  <div>
    <h1>{{ username }}님의 PROFILE 수정 페이지</h1>
    <hr>
    <h4 style="margin: 20px;">정보를 수정해주세요.</h4>
    <!--age, money, salary, job, main_bank, 
      stabillity, banking_products, card_products-->
    <form @submit.prevent="updateProfile">

      <label style="font-size: large; font-weight: 500; margin-bottom: 5px;" for="age">나이</label><br>
      <input class="select-style"  type="number" id="age" v-model.trim='age' min=0 max=200>
      
      <br>
      <br>
      
      <label style="font-size: large; font-weight: 500; margin-bottom: 5px;"  for="money">자산</label>
      <br>
      <input class="select-style"  type="number" id="money" v-model.trim='money'>
      <br>
      <br>

      <label style="font-size: large; font-weight: 500; margin-bottom: 5px;" for="salary">연봉</label>
      <br>
      <input class="select-style" type="number" id="salary" v-model.trim='salary'>
      <br>
      <br>

<!--:disabled=''를 사용하면 선택한 거 안보이게 할 수 있다.-->
      <div>
        <legend  style="font-size: large; font-weight: 500; margin-bottom: 5px;"  >직업</legend>
        <div>
          <input type="radio" id="학생 및 주부" name="job" v-model.trim='job' value="학생 및 주부" />
          <label for="학생 및 주부">학생 및 주부</label>
        </div>

        <div>
          <input type="radio" id="사업가 및 프리랜서" name="job" v-model.trim='job' value="사업가 및 프리랜서" />
          <label for="사업가 및 프리랜서">사업가 및 프리랜서</label>
        </div>

        <div>
          <input type="radio" id="회사원" name="job" v-model.trim='job' value="회사원" />
          <label for="회사원">회사원</label>
        </div>

        <div>
          <input type="radio" id="기타" name="job" v-model.trim='job' value="기타" /> 
          <label for="기타">기타</label>
          <!-- <input type="text" v-model.trim='otherJob' :disabled="job !== '기타'"> -->
          <!--이거때문에 계속 원래값 설정이 안되고 있나봐,,-->
        </div>
      </div>

      <br>
      <div class="stabillity-box">
      <label  style="font-size: large; font-weight: 500; margin-bottom: 0;"  for="stabillity">안정성</label><br>
      <input type="range" id="stabillity" name="stabillity" min="0" max="100"  list="values" v-model.trim='stabillity' >
        <datalist id="values">
          <option value="0" label="매우 모험 추구"></option>
          <option value="25" label="모험 추구"></option>
          <option value="50" label="보통"></option>
          <option value="75" label="안정 추구"></option>
          <option value="100" label="매우 안정 추구"></option>
        </datalist>
      </div>
      <br>
      <br>

      <label  style="font-size: large; font-weight: 500; margin-bottom: 5px;"   for="main_bank">주거래은행 : </label><br>
      <select  class="select-style"  id="main_bank" v-model="mainBank">
        <option disabled value="">은행을 선택하세요</option>
        <option v-for="bank in profileStore.banks" 
        :key="bank.id" :value="bank.name">{{ bank.name }}</option>
        <!--일단 보여지기 위해서 name을 보내는데, 나중에는 id를 보내고 이름을 보여지게 하는 것으로!-->
      </select>
      <br>

      <br>

      <div>
        <legend  style="font-size: large; font-weight: 500; margin-bottom: 5px;" >선호하는 은행 상품 유형(하나만 선택)</legend>

          <div>
            <input type="radio" id="예금" value="예금" name="banking_products" v-model.trim='banking_products' />
            <label for="예금">예금</label>
          </div>

          <div>
            <input type="radio" id="적금" value="적금" name="banking_products" v-model.trim='banking_products' />
            <label for="적금">적금</label>
          </div>

          <div>
            <input type="radio" id="대출" value="대출" name="banking_products" v-model.trim='banking_products' />
            <label for="대출">대출</label>
          </div>

          <div>
            <input type="radio" id="해당없음" value="해당없음" name="banking_products" v-model.trim='banking_products' />
            <label for="해당없음">해당없음</label>
          </div>

      </div>

      <br>

      <div>
        <legend  style="font-size: large; font-weight: 500; margin-bottom: 5px;"  >선호하는 카드 유형(하나만 선택)</legend>
        <div>
          <input type="radio" id="신용카드" name="card" value="신용카드" v-model.trim='card_products' />
          <label for="신용카드">신용카드</label>
        </div>

        <div>
          <input type="radio" id="체크카드" name="card" value="체크카드" v-model.trim='card_products' />
          <label for="체크카드">체크카드</label>
        </div>

        <div>
          <input type="radio" id="해당없음" name="card" value="해당없음" v-model.trim='card_products' />
          <label for="해당없음">해당없음</label>
        </div>
      </div>
      <button class="btn submit-btn" @click="submit">제출</button>
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
const job = ref('')
const otherJob = ref(null)
// if (profileStore.profile.otherJob) {
//   job.value = profileStore.profile.otherJob
// }
// 입력창을 없애면 원래값이 나오게 할 수 있는데,,,이게 어렵네
const mainBank = ref(profileStore.profile.main_bank)
const stabillity = ref(profileStore.profile.stabillity)
const banking_products = ref(profileStore.profile.banking_products)
const card_products = ref(profileStore.profile.card_products)

const updateProfile = function () {
      
      axios({
      method:'put',
      url:`${API_URL}/users/profile/${user_pk}/`,
      data:{
        age: age.value, 
        money: money.value, 
        salary: salary.value,
        job: job.value, 
        main_bank: mainBank.value, 
        stabillity: stabillity.value, 
        banking_products: banking_products.value, 
        card_products: card_products.value,
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
datalist {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  writing-mode: vertical-lr;
  width: 200px;
}

option {
  padding: 0;
}

input[type="range"] {
  width: 200px;
  margin: 0;
}

.stabillity-box {
  display: flex;flex-direction: column;align-items: center;
}
</style>