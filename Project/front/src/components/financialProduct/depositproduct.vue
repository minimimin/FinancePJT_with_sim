<template>
  <div>
    <h1>여기는 예금 상품 조회를 할 곳입니다.</h1>
    <p v-for="hi in financialProductStore.depositProduct">
      {{ hi }}
      <p>------------------------------------------------------</p>
      {{ hi.deposit_product_option }}
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
  financialProductStore.getDepositProduct()
})

</script>

<style scoped>

</style>