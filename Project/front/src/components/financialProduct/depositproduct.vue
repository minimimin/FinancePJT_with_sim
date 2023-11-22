<template>
  <div>
    <!-- <h1>여기는 예금 상품 조회를 할 곳입니다.</h1> -->
    <!-- <p v-for="hi in financialProductStore.depositProduct">
      {{ hi }}
      <p>------------------------------------------------------
        <br>
      금융상품 목록 : {{ hi.deposit_product_option }}
      <br>
      ------------------------------------------------------</p>
      <br>
    </p> -->


    <p>
      <!-- <p> -->
      <!-- {{ deposit.id }} -->
      <br>
      은행명 : {{ deposit.kor_co_nm }}
      <br>
      상품명 : {{ deposit.fin_prdt_nm }}
      <br>
      <!--이 아래부터는 디테일에 넣어놓을 것!-->
      가입방법 : {{ deposit.join_way }}
      <br>
      가입 대상 : {{ deposit.join_member }}
      <br>
      {{ deposit.join_deny }}
      <br>
      {{ deposit.max_limit }}
      <br>
      {{ deposit.spcl_cnd }}
      <br>
      <br>
      {{ deposit.mtrt_int }}
      <br>
      <br>
      {{ deposit.etc_note }}
      <br>
      
      <p>------------------------------------------------------
        <br>
      금융상품 목록 : 
      <br>
      {{ deposit.deposit_product_option.length }}
      <p v-for="deposit_detail in deposit.deposit_product_option">
      <br>
      {{ deposit_detail.intr_rate_type_nm }}
      <br>
      {{ deposit_detail.intr_rate }}
      <br>
      {{ deposit_detail.intr_rate2 }}
      <br>
      {{ deposit_detail.save_trm }}
      <br>
      <!--이건 필터써서 동일한 것 뽑아내기?!?!-->
      {{ deposit_detail.deposit_product }}
      </p>
      <br>
      ------------------------------------------------------</p>
      <br>
    </p>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useFinancialProductStore } from '@/stores/financialproduct'

const financialProductStore = useFinancialProductStore()

const props = defineProps({
  deposit: Object
})

onMounted(() => {
  financialProductStore.getDepositProduct()
})

</script>

<style scoped>

</style>