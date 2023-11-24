<template>
  <div class="category-box">
    <button @click="recommendTrue">추천</button>  |
    <button @click="depositTrue">예금</button>  |
    <button @click="savingTrue">적금</button>  |
    <button @click="loanHomeTrue">대출</button>
    <!-- <RouterLink :to="{ name: 'depositProduct' }">Deposit</RouterLink>  |
    <RouterLink :to="{ name: 'savingProduct' }">Saving</RouterLink>  |
    <RouterLink :to="{ name: 'loanhome' }">LoanHome</RouterLink>  |
    <RouterLink :to="{ name: 'loanperson' }">LoanPerson</RouterLink>  | -->
  </div>
  <div class="financial-box">
    <financialProductRecommendView v-show="recommend_show"/>
    <depositproduct v-show="deposit_show"/>
    <savingproduct v-show="saving_show"/>
    <loanhome v-show="loan_home_show"/>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useFinancialProductStore } from '@/stores/financialproduct'

import depositproduct from '@/components/financialProduct/depositproduct.vue'
import savingproduct from '@/components/financialProduct/savingproduct.vue'
import loanhome from '@/components/financialProduct/loanhome.vue'
import financialProductRecommendView from '@/views/financialproduct/financialProductRecommendView.vue'


const financialProductStore = useFinancialProductStore()

const deposit_show = ref(false)
const saving_show = ref(false)
const loan_home_show = ref(false)
const recommend_show = ref(false)


const depositTrue = function () {
  deposit_show.value = true
  saving_show.value = false
  loan_home_show.value = false
  recommend_show.value = false
}

const savingTrue = function () {
  deposit_show.value = false
  saving_show.value = true
  loan_home_show.value = false
  recommend_show.value = false
}

const loanHomeTrue = function () {
  deposit_show.value = false
  saving_show.value = false
  loan_home_show.value = true
  recommend_show.value = false
}

const recommendTrue = function () {
  deposit_show.value = false
  saving_show.value = false
  loan_home_show.value = false
  recommend_show.value = true
}

onMounted(() => {
  financialProductStore.getDepositProduct()
})

</script>

<style scoped>
button {
  background-color: white;
  border: none;
}

.financial-box {
  margin-top: 20px;
}

.category-box {
  font-size: 20px;
}
</style>