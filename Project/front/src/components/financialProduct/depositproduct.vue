<template>
  <div>
    <h1>예금 상품 조회</h1>
<div class="select-box">
  은행선택 : 
  <select class="select-style" v-model="bankname" >
    <option value="">은행 이름</option>
    <option v-for="bank in profileStore.banks" 
    :key="bank.id" :value="bank.name">{{ bank.name }}</option>
  </select>
</div>
<div>
<div class="d-flex justify-content-center">
  <table class="table table-hover table-box ">
    <thead>
      <tr>
        <th>은행명</th>
        <th>상품명</th>
        <th>금리유형</th>
        <th>최고한도</th>
        <th colspan="4">이자율</th>
        <!--  colspan="{{ check.length + 1 }}" -->
      </tr>
      <tr>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th v-for="num in check">{{ num }}개월</th>

      </tr>
    </thead>
    <tbody>
      <template v-for="deposit in depositData" :key="deposit.fin_prdt_nm">
        <tr v-show="selectedBank(deposit.kor_co_nm)" @click="goDetail(deposit.id)">
          <td>{{ deposit.kor_co_nm }}</td>
          <td>{{ deposit.fin_prdt_nm }}</td>
          <td >{{ deposit.deposit_product_option[0].intr_rate_type_nm}}</td>
          <td>{{ deposit.max_limit }}</td>
          <td v-for="num in check">
            {{ deposit.rates[num]}}</td>
        </tr>
      </template>
    </tbody>
  </table>
  </div>
</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useProfileStore } from '@/stores/profile'
import { useFinancialProductStore } from '@/stores/financialproduct'

const check = [6, 12, 24, 36]
const financialProductStore = useFinancialProductStore()
const router = useRouter()
const depositData = ref([])
const goDetail = function(depositId) {
  financialProductStore.getDepositProductDetail(depositId)
  router.push({ name:'depositProductDetail', params: { deposit_id : depositId } })
}

const profileStore = useProfileStore()
const bankname = ref('')
const selectedBank = function (name) {
  return bankname.value ? bankname.value===name : true
}

onMounted(() => {
  financialProductStore.getDepositProduct().then(()=>{
    depositData.value = financialProductStore.nowDeposit?.map(deposit =>{
      if (!deposit.max_limit) {
        deposit.max_limit = '없음'
      }
      
      const rates = {
        6 :null,
        12 : null,
        24 : null,
        36 :null,
      }
      deposit.deposit_product_option.forEach(deposit_detail => {
        if (!rates[deposit_detail.save_trm]) {
          rates[deposit_detail.save_trm]=deposit_detail.intr_rate2
        }
      })
      check.forEach(num => {
        if (!rates[num]) {
          rates[num] = '-'
        }
      })
    return { ...deposit, rates }
    })
  })
})

</script>

<style scoped>

</style>