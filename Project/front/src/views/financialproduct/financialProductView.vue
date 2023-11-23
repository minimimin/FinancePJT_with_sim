<template>
  <div>
    <RouterLink :to="{name: 'recommend'}">추천</RouterLink>
    <button @click="depositTrue">예금</button>  |
    <button @click="savingTrue">적금</button>  |
    <button @click="loanHomeTrue">대출</button>  |
    <!-- <RouterLink :to="{ name: 'depositProduct' }">Deposit</RouterLink>  |
    <RouterLink :to="{ name: 'savingProduct' }">Saving</RouterLink>  |
    <RouterLink :to="{ name: 'loanhome' }">LoanHome</RouterLink>  |
    <RouterLink :to="{ name: 'loanperson' }">LoanPerson</RouterLink>  | -->

    <depositproduct v-show="deposit_show"/>
    <savingproduct v-show="saving_show"/>
    <loanhome v-show="loan_home_show"/>

  </div>
  <RouterView/>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useFinancialProductStore } from '@/stores/financialproduct'

import depositproduct from '@/components/financialProduct/depositproduct.vue'
import savingproduct from '@/components/financialProduct/savingproduct.vue'
import loanhome from '@/components/financialProduct/loanhome.vue'


const financialProductStore = useFinancialProductStore()

const deposit_show = ref(false)
const saving_show = ref(false)
const loan_home_show = ref(false)


const depositTrue = function () {
  deposit_show.value = true
  saving_show.value = false
  loan_home_show.value = false
}

const savingTrue = function () {
  deposit_show.value = false
  saving_show.value = true
  loan_home_show.value = false
}

const loanHomeTrue = function () {
  deposit_show.value = false
  saving_show.value = false
  loan_home_show.value = true
}

onMounted(() => {
  financialProductStore.getDepositProduct()
})

</script>

<style scoped>

</style>