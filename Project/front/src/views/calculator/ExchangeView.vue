<template>
    <div>
        <h1>환율 계산기</h1>
        <p>'나라 및 통화' : {{ calculatorStore.exchange }}</p>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useCalculatorStore } from '@/stores/calculator'

const router = useRouter()
const userStore = useUserStore()
const calculatorStore = useCalculatorStore()

onMounted(() => {
    calculatorStore.getExchangeRate()
    // console.log(calculatorStore.exchange)
    // 전체 리스트가 나오게 된다.
    // v-for 돌려서 하나씩뽑아내기
})
</script>

<style scoped>

</style>