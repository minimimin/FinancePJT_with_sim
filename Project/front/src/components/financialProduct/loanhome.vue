<template>
  <div>
    <h1>여기는 전세자금대출상품 조회를 할 곳입니다.</h1>
    <p v-for="hi in financialProductStore.loanForHomeProduct">
      {{ hi }}
      <p>------------------------------------------------------</p>
      {{ hi.loan_home_product_option }}
      <p>------------------------------------------------------</p>
      <br>
    </p>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useFinancialProductStore } from '@/stores/financialproduct'

const financialProductStore = useFinancialProductStore()

onMounted(() => {
  financialProductStore.getLoanHomeProduct()
})

</script>

<style scoped>

</style>