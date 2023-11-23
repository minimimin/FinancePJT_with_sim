import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useUserStore } from '@/stores/user'
import axios from 'axios'

export const useFinancialProductStore = defineStore('financialproduct', () => {
  const userStore = useUserStore()

  const depositProduct = ref(null)
  const depositDetail = ref(null)
  const savingProduct = ref(null)
  const savingDetail = ref(null) 
  const loanForHomeProduct = ref(null)
  const loanDetail = ref(null) 

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


  const getDepositProductDetail = function (deposit_id) {
    axios({
      method: 'get',
      url: `${userStore.API_URL}/finanProduct/depositinfo/${deposit_id}/`,
    })
      .then((res) => {
        depositDetail.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }


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

  const getSavingProductDetail = function (saving_id) {
    axios({
      method: 'get',
      url: `${userStore.API_URL}/finanProduct/savinginfo/${saving_id}/`,
    })
      .then((res) => {
        savingDetail.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }


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

  const getLoanHomeProductDetail = function (loan_id) {
    axios({
      method: 'get',
      url: `${userStore.API_URL}/finanProduct/loanforhome/${loan_id}/`,
    })
      .then((res) => {
        loanDetail.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }


  return { 
    userStore, depositProduct, depositDetail, savingProduct, savingDetail, loanForHomeProduct, loanDetail,
    getDepositProduct, getDepositProductDetail, getSavingProduct, getSavingProductDetail, getLoanHomeProduct, getLoanHomeProductDetail,
    nowDeposit, nowSaving, nowLoanHome }
})