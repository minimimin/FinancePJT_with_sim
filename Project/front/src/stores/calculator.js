import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useUserStore } from '@/stores/user'
import axios from 'axios'

export const useCalculatorStore = defineStore('calculator', () => {
    const userStore = useUserStore()

    const exchange = ref([])
    const getExchangeRate = function () {
      axios({
        method: 'get',
        url: `${userStore.API_URL}/exchange/`,
      })
        .then((res) =>{
          exchange.value = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }

    return { userStore, exchange, getExchangeRate }
})