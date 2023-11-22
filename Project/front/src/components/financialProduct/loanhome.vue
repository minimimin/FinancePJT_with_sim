<template>
  <div>
    <h1>여기는 전세자금대출상품 조회를 할 곳입니다.</h1>
    <table>
      <thead>
        <tr>
          <th>은행명</th>
          <th>상품명</th>
          <th>대출한도</th>
          <th>금리유형</th>
          <th colspan="{{ check.length + 1 }}">대출금리</th>
        </tr>
        <tr>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th v-for="point in check">{{ point }}</th>
        </tr>
      </thead>

      <tbody>
        <template v-for="loanHome in loanHomeData" :key="loanHome.fin_prdt_cd">
          <tr v-for="loan_home in loanHome.loan_home_product_option" :key="deposit.fin_prdt_nm" @click="goDetail">
            <td>{{ loanHome.kor_co_nm }}</td>
            <td>{{ loanHome.fin_prdt_nm }}</td>
            <td>{{ loanHome.loan_lmt }}</td>
            <td>{{ loan_home.lend_rate_type_nm }}</td>
            <td >{{ loan_home.lend_rate_avg }}</td>
            <td >{{ loan_home.lend_rate_min }}</td>
            <td >{{ loan_home.lend_rate_max }}</td>
            </tr>
        </template>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useFinancialProductStore } from '@/stores/financialproduct'
import { routerKey } from 'vue-router';
const check = ['평균', '최저', '최고']
const financialProductStore = useFinancialProductStore()
const router = useRouter()
const loanHomeData = ref([])
const goDetail = function() {
  router.push({name:'loanhomeDetail'})
}


onMounted(() => {
  financialProductStore.getLoanHomeProduct()
  // .then(()=>{
  //   loanHomeData.value = financialProductStore.nowLoanHome?.map(loanHome =>{
  //     const rates = {
  //       6 :null,
  //       12 : null,
  //       24 : null,
  //       36 :null,
  //     }
      // loanHome.deposit_product_option.forEach(deposit_detail => {
      //   if (!rates[deposit_detail.save_trm]) {
      //     rates[deposit_detail.save_trm]=deposit_detail.intr_rate2
      //   }
      // })
//       check.forEach(num => {
//         if (!rates[num]) {
//           rates[num] = '-'
//         }
//       })
//     return { ...deposit, rates }
//     })
//   })
})

</script>

<style scoped>

</style>