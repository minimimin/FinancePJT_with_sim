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
    <hr>
    <h4>적금 상품 추천</h4>
    <div>{{ result?.sorted_deposit_products_info }}</div>
    <h4>예금 상품 추천</h4>
    <div>{{ result?.sorted_saving_products_info }}</div>
    <h4>대출 상품 추천</h4>
    <div>{{ result?.sorted_loan_home_products_info }}</div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useUserStore } from '@/stores/user'
import axios from 'axios'

const userStore = useUserStore()
const checkList_kr = ref(['나이', '자산', '연봉', '직업', '주거래은행', '안정성', '선호은행상품', '선호카드상품'])
const checkList = ref(['age', 'money', 'salary', 'job', 'main_bank', 'stabillity', 'banking_products', 'card_products'])
const selectedList = ref([])
const allSelected = ref(false)
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

</script>

<style scoped>

</style>