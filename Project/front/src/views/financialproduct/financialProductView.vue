<template>
  <div>
    <h1>여기는 예적금 조회를 할 곳입니다.</h1>
    <p>우선 은행별, 상품별 조회할 수 있도록 해볼까요?</p>
    <RouterLink :to="{ name: 'depositProduct' }">Deposit</RouterLink>  |
    <RouterLink :to="{ name: 'savingProduct' }">Saving</RouterLink>  |
    <RouterLink :to="{ name: 'loanhome' }">LoanHome</RouterLink>  |
    <RouterLink :to="{ name: 'loanperson' }">LoanPerson</RouterLink>  |
  </div>
  <RouterView/>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useFinancialProductStore } from '@/stores/financialproduct'

const financialProductStore = useFinancialProductStore()

onMounted(() => {
  financialProductStore.getDepositProduct()
})

</script>

<style scoped>

</style>