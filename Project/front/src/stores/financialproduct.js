import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useUserStore } from '@/stores/user'
import axios from 'axios'

export const useFinancialProductStore = defineStore('financialproduct', () => {
  const userStore = useUserStore()

  const depositProduct = ref(null)
  const savingProduct = ref(null)
  const loanForHomeProduct = ref(null)

  const getDepositProduct = function () {
    return axios({
      method: 'get',
      url: `${userStore.API_URL}/finanProduct/depositinfo/`,
    })
      .then((res) =>{
        depositProduct.value = res.data

      })
      .catch((err) => {
        console.log(err)
      })
  }

  const nowDeposit = computed(()=>{
    return depositProduct.value
  })


  const getSavingProduct = function () {
    return axios({
      method: 'get',
      url: `${userStore.API_URL}/finanProduct/savinginfo/`,
    })
      .then((res) =>{
        savingProduct.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const nowSaving = computed(()=>{
    return savingProduct.value
  })

  const getLoanHomeProduct = function () {
    return axios({
      method: 'get',
      url: `${userStore.API_URL}/finanProduct/loanforhome/`,
    })
      .then((res) =>{
        loanForHomeProduct.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const nowLoanHome = computed(()=>{
    return loanForHomeProduct.value
  })


  return { 
    userStore, depositProduct, savingProduct, loanForHomeProduct, 
    getDepositProduct, getSavingProduct, getLoanHomeProduct,
    nowDeposit, nowSaving, nowLoanHome }
})