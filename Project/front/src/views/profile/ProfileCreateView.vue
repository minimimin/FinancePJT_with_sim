<template>
  <!--아래 값 받은 걸로 프로필 페이지에 보여질 수 있게 + 수정할 수 있게 설정하기!!-->

  <div>
    <h1>{{ username }}님의 PROFILE</h1>
    <hr>
    <p>상세 정보를 입력해주세요.</p>
    <!--age, money, salary, job, main_bank, 
      stabillity, banking_products, card_products-->
    <!-- <form @submit.prevent="createProfile">

      <label for="age">나이</label><br>
      <input type="number" id="age" v-model.trim='age' min=0 max=200 value="여기 입력받은 값이 연동될 수 있게 하기!">
      
      <br>
      <br>
      
      <label for="money">자산</label>
      <br>
      <input type="number" id="money" v-model.trim='money' value="여기 입력받은 값이 연동될 수 있게 하기!">
      
      <br>
      <br>

      <label for="salary">연봉</label>
      <br>
      <input type="number" id="salary" v-model.trim='salary' value="여기 입력받은 값이 연동될 수 있게 하기!">
      
      <br>
      <br> -->
      <!-- <fieldset>
        <legend>직업</legend>
        <div>
          <input type="radio" id="학생 및 주부" name="job"  v-model.trim='job' value="학생 및 주부" checked />
          <label for="학생 및 주부">학생 및 주부</label>
        </div>

        <div>
          <input type="radio" id="사업가 및 프리랜서" name="job"  v-model.trim='job' value="사업가 및 프리랜서" />
          <label for="사업가 및 프리랜서">사업가 및 프리랜서</label>
        </div>

        <div>
          <input type="radio" id="회사원" name="job"  v-model.trim='job' value="회사원" />
          <label for="회사원">회사원</label>
        </div>

        <div>
          <input type="radio" id="기타" name="job" value="기타" onchange="toggleTextField()"/> 
          <label for="기타">기타</label>
          <input type="text" id="기타TextField" v-model.trim='job' disabled>
        </div>
      </fieldset> -->


      <!-- <label for="job">직업 : </label>
      <div id="job">
        <input type="radio">
      </div> -->

      <br>

<!--------------------------------------------------------------------------------------------->
      <!-- <label for="main_bank">주거래은행 : </label><br> -->
      <!-- <select id="main_bank" v-model="selectedBank"> -->
      <!-- <select id="main_bank">
        <option disabled value="">은행을 선택하세요</option>
        <option v-for="bank in store.bank" 
        :key="bank.id" :value="bank.id">{{ bank.name }}</option>
      </select> -->

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
      </fieldset>

    </form> -->
  </div>
</template>


<script setup>
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

    import { useProfileStore } from '@/stores/profile'
    import { useUserStore } from '@/stores/user'
    import { useRouter, useRoute } from 'vue-router'
    import { ref } from 'vue'
    import axios from 'axios'

    const router = useRouter()
    const selectedBank = ref(null)
    const store = useUserStore()
    const stores = useProfileStore()


    const age = ref(null)
    const money = ref(null)
    const salary = ref(null)
    const job = ref(null)
    const main_bank = ref(null)
    const stabillity = ref(null)
    const banking_products = ref(null)
    const card_products = ref(null)

    // const route = useRoute()

    const user_pk = store.userPk
    const username = store.userName

    const createProfile = function () {
      axios({
      method:'post',
      url:`${store.API_URL}/profile/${user_pk}/`,
      // user_pk를 우선 위에서 받아왔다고 치고, 입력해놓기,,!!
      data:{
        age: age.value, 
        money: money.value, 
        salary: salary.value,
        // job: job.value, 
        // main_bank: main_bank.value, 
        // stabillity: stabillity.value, 
        // banking_products: banking_products.value, 
        // card_products: card_products.value,
      },
      headers: {
        Authorization: `Token ${store.token}`
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

    
//--------------------------------------------------------------------
  //   const createArticle = function () {
  //   axios({
  //     method: 'post',
  //     url: `${store.API_URL}/articles/`,
  //     data: {
  //       title: inputTitle.value,
  //       content: inputContent.value,
  //       bank: selectedBank.value,
  //     }
  //   })
  //     .then((res) => {
  //       router.push({ name: 'articles' })
  //     })
  //     .catch((err) => {
  //       console.log(err)
  //     })
  // }
</script>

<style scoped>

</style>