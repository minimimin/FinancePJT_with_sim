<template>
  <div>
    <h1>[예금 상품 조회]</h1>
<div>
  은행선택 : 
  <select v-model="bankname" >
    <option value="">은행 이름</option>
    <option v-for="bank in profileStore.banks" 
    :key="bank.id" :value="bank.name">{{ bank.name }}</option>
  </select>
</div>

<table>
  <thead>
    <tr>
      <th>은행명</th>
      <th>상품명</th>
      <th>금리유형</th>
      <th>최고한도</th>
      <th colspan="{{ check.length + 1 }}">이자율</th>
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
const goDetail = function(deposit_id) {
  financialProductStore.getDepositProductDetail(deposit_id)
  router.push({ name:'depositProductDetail', params: { deposit_id : deposit_id } })
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