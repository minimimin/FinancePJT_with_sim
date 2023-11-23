<template>
  <div>
    <h1>여기는 대출 상세 페이지</h1>
    <div>
      <br>
      <br>
        은행명 : {{ financialProductStore.loanDetail?.kor_co_nm }}
      <br>
      <br>
        상품명 : {{ financialProductStore.loanDetail?.fin_prdt_nm }}
      <br>
      <br>
        대출한도 : {{ financialProductStore.loanDetail?.loan_lmt }}
      <br>
      <br>
        대출 부대비용 : <br>{{ financialProductStore.loanDetail?.loan_inci_expn }}
      <br>
      <br>
        중도상환 수수료 : <br>{{ financialProductStore.loanDetail?.erly_rpay_fee }}
      <br>
      <br>
        연체 이자율 : <br>{{ financialProductStore.loanDetail?.dly_rate }}
      <br>
      <hr>
      <!-- 여기서부터 v-for를 돌면서 찾아내야한다! -->
      금융상품 목록(총 {{ financialProductStore.loanDetail?.loan_home_product_option.length }}개) :
      <div v-for="loan_home in financialProductStore.loanDetail?.loan_home_product_option">
        <br>
        <!-- [{{ loan_home.id }}] -->
        <br>
        <br>
          금리유형 : {{ loan_home.lend_rate_type_nm }}
        <br>
        <br>
          평균금리(소수점 2자리) : {{ loan_home.lend_rate_avg }}
        <br>
        <br>
          최저대출금리(소수점 2자리) : {{ loan_home.lend_rate_min }}
        <br>
        <br>
          최대대출금리(소수점 2자리) : {{ loan_home.lend_rate_max }}
        <br>
        <br>
        <button>가입하기</button>
        (가입한 상품 목록에 저장하는 것으로 설정하기!)
      </div>
    </div>
  </div>
</template>

<script setup>
import { useFinancialProductStore } from '@/stores/financialproduct'
const financialProductStore = useFinancialProductStore()

</script>

<style scoped>

</style>