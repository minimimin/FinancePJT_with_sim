<template>
  <div>
    <h1>대출 상품 조회</h1>
    <div  class="select-box">
    은행선택 : 
    <select v-model="bankname" >
      <option value="">은행 이름</option>
      <option v-for="bank in profileStore.banks" 
      :key="bank.id" :value="bank.name">{{ bank.name }}</option>
    </select>
    </div>
    <div class="d-flex justify-content-center">
    <table  class="table table-hover table-box ">
      <thead>
        <tr>
          <th>은행명</th>
          <th>상품명</th>
          <th>대출한도</th>
          <!-- <th>금리유형</th> -->
      <th colspan="3">대출금리</th>
          <!-- <th colspan="{{ check.length + 1 }}">대출금리</th> -->
        </tr>
        <tr>
          <th></th>
          <th></th>
          <th></th>
          <!-- <th></th> -->
          <th v-for="point in check">{{ point }}</th>
        </tr>
      </thead>
      
      <tbody>
        <template v-for="loanHome in financialProductStore.nowLoanHome" :key="loanHome.fin_prdt_cd">
        <tr v-show="selectedBank(loanHome.kor_co_nm)" @click="goDetail(loanHome.id)">
          <td>{{ loanHome?.kor_co_nm }}</td>
            <td>{{ loanHome?.fin_prdt_nm }}</td>
            <td>{{ loanHome?.loan_lmt }}</td>
            <!-- <td>{{ loan_home?.lend_rate_type_nm }}</td> -->
            <td >{{ loanHome.loan_home_product_option[0]?.lend_rate_avg }}</td>
            <td >{{ loanHome.loan_home_product_option[0]?.lend_rate_min }}</td>
            <td >{{ loanHome.loan_home_product_option[0]?.lend_rate_max }}</td>
            </tr>
        </template>
      </tbody>
    </table>
  </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useProfileStore } from '@/stores/profile'
import { useFinancialProductStore } from '@/stores/financialproduct'

const check = ['평균', '최저', '최고']
const financialProductStore = useFinancialProductStore()
const router = useRouter()

const goDetail = function(loan_id) {
  financialProductStore.getLoanHomeProductDetail(loan_id)
  router.push({name:'loanhomeDetail', params:{loan_id:loan_id}})
}

const profileStore = useProfileStore()
const bankname = ref('')
const selectedBank = function (name) {
  return bankname.value ? bankname.value===name : true
}

onMounted(() => {
  financialProductStore.getLoanHomeProduct()
})

</script>

<style scoped>

</style>