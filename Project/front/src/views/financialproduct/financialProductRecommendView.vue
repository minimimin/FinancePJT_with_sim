<template>
  <div>
    <h1>금융 상품 추천 페이지</h1>
    <form @submit.prevent="getRecommends">
      <fieldset>
        <legend>내가 원하는 조건 고르기</legend>

        <div>
        <input type="checkbox" value="check-all" v-model="allSelected">
        <label for="check-all">전체</label>
        </div>

        <template v-for="(item, index) in checkList" :key="index">
          <input type="checkbox" :id="item" :value="item" v-model="selectedList">
          <label :for="item">{{ checkList_kr[index] }}</label>
        </template>
      </fieldset>

      <input type="submit" value="검색">
    </form>
    <br>

    <template v-if="result">
      <div class="product-list" v-for="(productName, index) in productList" :key="productName.id">
        <h4>{{ productName }} 상품 추천</h4>
        <hr>
        <table>
        <thead>
        <tr>
          <th></th>
          <th>은행명</th>
          <th>상품명</th>
        </tr>
        </thead>
        <tbody>
        <template v-for="products in result[index]" :key="products.id">
          <tr v-for="(product, index) in products" :key="product.id" @click="goDetail(product.id)">
            <td>{{ index+1 }}.</td>
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
table {
  margin: auto;
  background-color: #f6ffff;
  border-radius: 20px;
  margin-bottom: 20px;
  padding: 20px;
  box-shadow: 5px 5px 5px gainsboro;
}

.product-list{
  margin-bottom: 20px;
}

hr {
  color: #005c77;
}

td {
  padding: 5px;
  margin: 5px;
  text-align: left;
  border-bottom: 1px solid #005c77;
}
</style>