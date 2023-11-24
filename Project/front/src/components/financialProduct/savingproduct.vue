<template>
  <div>
    <h1>적금 상품 조회</h1>
    <div class="select-box">
  은행선택 : 
  <select class="select-style" v-model="bankname" >
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
          <th>금리유형</th>
          <th>최고한도</th>
          <th colspan="4">이자율</th>
          <!-- <th colspan="{{ check.length + 1 }}">이자율</th> -->
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
        <template v-for="saving in savingData" :key="saving.fin_prdt_nm">
        <tr v-show="selectedBank(saving.kor_co_nm)" @click="goDetail(saving.id)">
          <td>{{ saving.kor_co_nm }}</td>
          <td>{{ saving.fin_prdt_nm }}</td>
          <td >{{ saving.saving_product_option[0].intr_rate_type_nm}}</td>
          <td>{{ saving.max_limit }}</td>
          <td v-for="num in check">
            {{ saving.rates[num]}}</td>
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

const check = [6, 12, 24, 36]
const financialProductStore = useFinancialProductStore()
const router = useRouter()
const savingData = ref([])
const goDetail = function(saving_id) {
  financialProductStore.getSavingProductDetail(saving_id)
  router.push({name:'savingProductDetail', params: { saving_id : saving_id}})
}

const profileStore = useProfileStore()
const bankname = ref('')
const selectedBank = function (name) {
  return bankname.value ? bankname.value===name : true
}

onMounted(() => {
  financialProductStore.getSavingProduct().then(()=>{
    savingData.value = financialProductStore.nowSaving?.map(saving =>{
      if (!saving.max_limit) {
        saving.max_limit = '없음'
      }
      const rates = {
        6 :null,
        12 : null,
        24 : null,
        36 :null,
      }
      saving.saving_product_option.forEach(saving_detail => {
        if (!rates[saving_detail.save_trm]) {
          rates[saving_detail.save_trm]=saving_detail.intr_rate2
        }
      })
      check.forEach(num => {
        if (!rates[num]) {
          rates[num] = '-'
        }
      })
    return { ...saving, rates }
    })
  })
})

</script>

<style scoped>

</style>