<template>
  <div>
<h1>여기는 적금 디테일 페이지!</h1>
    <div>
      <br>
      은행명 : {{ financialProductStore.savingDetail?.kor_co_nm }}
      <br>
      <br>
      상품명 : {{ financialProductStore.savingDetail?.fin_prdt_nm }}
      <br>
      <br>
      가입방법 : {{ financialProductStore.savingDetail?.join_way }}
      <br>
      <br>
      가입 대상 : {{ financialProductStore.savingDetail?.join_member }}
      <br>
      <br>
      가입 제한 : {{ financialProductStore.savingDetail?.join_deny }}
      <br>
      <br>
      최고 한도 : {{ financialProductStore.savingDetail?.max_limit }}
      <br>
      <br>
      우대조건 : {{ financialProductStore.savingDetail?.spcl_cnd }}
      <br>
      <br>
      만기 후 이자율 : 
      <br>{{ financialProductStore.savingDetail?.mtrt_int }}
      <br>
      <br>
      유의사항 : <br>{{ financialProductStore.savingDetail?.etc_note }}
      <br>
      
      <p>
        <hr>
      <!-- 금융상품 목록(총 {{ financialProductStore.savingDetail?.saving_product_option.length }}개) :  -->
      테이블로 만들기
      <br>
      <br>
      <p v-for="saving_detail in financialProductStore.savingDetail?.saving_product_option">
        <!-- [{{ saving_detail.id }}] -->
        <br>
      저축금리유형명 : {{ saving_detail.intr_rate_type_nm }}
      <br>
      저축금리 : {{ saving_detail.intr_rate }}
      <br>
      최고 우대금리: {{ saving_detail.intr_rate2 }}
      <br>
      저축기간 : {{ saving_detail.save_trm }}
      <br>
      <button>가입하기</button>
      </p>
      <br>
      <hr>
    </p>
    </div>

  </div>
</template>

<script setup>
// import { ref } from 'vue'
import { useFinancialProductStore } from '@/stores/financialproduct'
const financialProductStore = useFinancialProductStore()
// const savingDetail = ref(financialProductStore.savingDetail)

</script>

<style scoped>

</style>