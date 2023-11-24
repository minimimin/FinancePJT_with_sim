<template>
  <div>
    <h1>금융 상품 추천</h1>
    <form @submit.prevent="getRecommends">
      <fieldset>
        <p class="medium-title">원하는 추천 조건을 선택하세요</p>

        <table class="table-box top-line bottom-line" >
          <tbody>
            <tr>
              <td><input type="checkbox" value="check-all" v-model="allSelected">
                <label for="check-all">전체</label></td>
              <td></td>    
              <td></td>    
              <td></td>    
              <td></td>     
            </tr>
            <tr>
              <td v-for="(item, index) in checkList.slice(0, 5)" :key="index">
                  <input type="checkbox" :id="item" :value="item" v-model="selectedList">
                  <label :for="item">{{ checkList_kr[index] }}</label>
                  <!-- {{ item }} -->
            </td>
            </tr>
            <tr>
              <td v-for="(item, index) in checkList.slice(5)" :key="index">
                  <input type="checkbox" :id="item" :value="item" v-model="selectedList">
                  <label :for="item">{{ checkList_kr[index+5] }}</label>
            </td>
            <td></td>
            <td></td>
          </tr>
        </tbody>
      </table>
      <input type="submit" class="btn submit-btn  " value="선택 완료">
      </fieldset>
    </form>
    <br>

    <template v-if="result">
      <div class="product-list" v-for="(productName, index) in productList" :key="productName.id">
        <h4>{{ productName }} 상품 추천</h4>
        <hr>
        <table class="table table-hover ">
        <thead>
        <tr>
          <th class="num-td">#</th>
          <th>은행명</th>
          <th>상품명</th>
        </tr>
        </thead>
        <tbody>
        <template v-for="products in result[index]" :key="products.id">
          <tr v-for="(product, index) in products" :key="product.id" @click="goDetail(product.id)">
            <td class="num-td">{{ index+1 }}.</td>
            <td>{{ product.kor_co_nm }}</td>
            <td>{{ product.fin_prdt_nm }}</td>
          </tr>
        </template>
        </tbody>
        </table>
      </div>
    </template>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useFinancialProductStore } from '@/stores/financialproduct'
import axios from 'axios'

const router = useRouter()
const userStore = useUserStore()
const financialProductStore = useFinancialProductStore()

const checkList_kr = ref(['나이', '자산', '연봉', '직업', '주거래은행', '안정성', '선호은행상품', '선호카드상품'])
const checkList = ref(['age', 'money', 'salary', 'job', 'main_bank', 'stabillity', 'banking_products', 'card_products'])
const selectedList = ref([])
const allSelected = ref(false)

const productList = ['예금', '적금', '대출']
const result = ref(null)

watch(allSelected, (newValue) => {
  if (newValue) {
    selectedList.value = [...checkList.value]
  } else {
    selectedList.value = []
  }
})

watch(() => selectedList.value.length, () => {
  allSelected.value = selectedList.value.length === checkList.value.length;
});

const getRecommends = function () {
  if (!userStore.isLogin) {
    const confirmResult = confirm("로그인이 필요합니다. 로그인 페이지로 이동하시겠습니까?");
    if (confirmResult) {
      // 로그인 페이지로 이동
      router.push({ name: 'login' });
    }
    return; // 로그인이 되어있지 않으면 이후 코드 실행하지 않음
  }

  if (selectedList.value.length === 0) {
    alert("조건을 한 개 이상 골라주세요");
    return;
  }

  axios({
    method: 'post',
    url: `${userStore.API_URL}/recommends/`,
    data: {
      selected: selectedList.value,
      user: userStore.loginUser
    },
    headers: {
        Authorization: `Token ${userStore.token}`
      }
  })
    .then((res) => {
      result.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
}

const goDetail = function(deposit_id) {
  financialProductStore.getDepositProductDetail(deposit_id)
  router.push({ name:'depositProductDetail', params: { deposit_id : deposit_id } })
}

</script>

<style scoped>

hr {
  color: #005c77;
  /* border-bottom: 1px dashed #005c77; */
}

td {
  width: 10px;
  text-align: left;
  padding: 5px;
}

.table-box{
  width: 50%;
  margin: 0 auto;
}

label {
  margin-left: 2px;
}

.submit-btn {
  background-color: #0c768b;
  color: white;
  padding: 5px 30px;
  margin: 20px;
}

.medium-title {
  margin: 20px;
  font-size: large;
  font-weight: 500;
}
.top-line{
  border-top: 2px solid #0c768b;
}

.bottom-line{
  border-bottom: 2px solid #0c768b;
}

.product-list {
  width: 80%;
  margin: 0 auto 50px;
}

.num-td {
  text-align: center;
}
</style>