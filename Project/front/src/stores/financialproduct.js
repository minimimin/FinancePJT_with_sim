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
    axios({
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

  const getSavingProduct = function () {
    axios({
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

  const getLoanHomeProduct = function () {
    axios({
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


  return { 
    userStore, depositProduct, savingProduct, loanForHomeProduct, 
    getDepositProduct, getSavingProduct, getLoanHomeProduct }
})