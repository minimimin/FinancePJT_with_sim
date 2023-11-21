<template>
    <div>
        <h1>환율 계산기</h1>
        <!-- <label for=""></label><br> -->
        <!-- <select v-model="cur_nm" @change=""> -->
        <div>
            <h3>[나라별 환율 계산]</h3>
            <select v-model="changeCountry" >
                <option disabled value="">나라 및 통화명</option>
                <option v-for="exchangeAll in calculatorStore.exchange" 
                :key="exchangeAll.cur_unit" :value="exchangeAll.cur_unit">{{ exchangeAll.cur_nm }}({{ exchangeAll.cur_unit }})</option>
            </select>
            <input type="number" v-model="changeMoney" @input="exchangeMoney">
        <br>
            <select v-model="standardCountry" >
                <option disabled value="">나라 및 통화명</option>
                <option v-for="exchangeAll in calculatorStore.exchange" 
                :key="exchangeAll.cur_unit" :value="exchangeAll.cur_unit">{{ exchangeAll.cur_nm }}({{ exchangeAll.cur_unit }})</option>
            </select>
            <input type="number" v-model="reChangeMoney" @input="exchangeMoney2">
        </div>
   
        <br>
        <br>

        <div>
        <!--나라를 정하면 그것의 송금 보낼 때 송금 받을 때 값 넣을 수 있게-->
        <h3>[한국에서 송금/착금 할 때 환율 계산]</h3>
        <!-- <label for="mySelect">
        <input type="text" id="myInput" @input="filterOptions()" placeholder="나라명을 검색하세요">
        </label> -->
        <br>
        <select id='mySelect' v-model="exchangeKorea">
            <option disabled value="">나라 및 통화명</option>
            <option v-for="exchangeAll in calculatorStore.exchange" 
            :key="exchangeAll.cur_unit" :value="exchangeAll.cur_unit">{{ exchangeAll.cur_nm }}</option>
        </select>
        <br>
        <p>보내실때(송금) : {{ exchangeKoreaTTS }}원</p>
        <p>받으실때(송금) : {{ exchangeKoreaTTB }}원</p>
        </div>
        
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useCalculatorStore } from '@/stores/calculator'

const calculatorStore = useCalculatorStore()

const changeCountry = ref('USD')
const changeMoney = ref(0)
// 첫번째 설정값 담아놓을 곳

const standardCountry = ref('KRW')
const reChangeMoney = ref(0)
// 두번째 기준되는 나라 설정값 담아놓을 곳


const exchangeMoney = function () {
    reChangeMoney.value=''
    const temp = calculatorStore.exchange.filter(exchange => exchange.cur_unit === changeCountry.value)
    const temp2 = calculatorStore.exchange.filter(exchange => exchange.cur_unit === standardCountry.value)
    
    if (temp[0].cur_unit === 'JPY(100)' || temp[0].cur_unit === 'IDR(100)') {
        reChangeMoney.value = ((temp[0].deal_bas_r.replace(/,/g,'')/100)/temp2[0].deal_bas_r.replace(/,/g,'')* changeMoney.value).toFixed(2)
    } else if (temp2[0].cur_unit === 'JPY(100)' || temp2[0].cur_unit === 'IDR(100)') {
        reChangeMoney.value = (temp[0].deal_bas_r.replace(/,/g,'')/temp2[0].deal_bas_r.replace(/,/g,'')* changeMoney.value*100).toFixed(2)
    } else {
        reChangeMoney.value = (temp[0].deal_bas_r.replace(/,/g,'')/temp2[0].deal_bas_r.replace(/,/g,'')* changeMoney.value).toFixed(2)
    }
}

const exchangeMoney2 = function () {
    changeMoney.value=''
    const temp2 = calculatorStore.exchange.filter(exchange => exchange.cur_unit === changeCountry.value)
    const temp = calculatorStore.exchange.filter(exchange => exchange.cur_unit === standardCountry.value)
    changeMoney.value = (temp[0].deal_bas_r.replace(/,/g,'')/temp2[0].deal_bas_r.replace(/,/g,'')* reChangeMoney.value).toFixed(2)
    
    if (temp[0].cur_unit === 'JPY(100)' || temp[0].cur_unit === 'IDR(100)') {
        changeMoney.value = ((temp[0].deal_bas_r.replace(/,/g,'')/100)/temp2[0].deal_bas_r.replace(/,/g,'')* reChangeMoney.value).toFixed(2)
    } else if (temp2[0].cur_unit === 'JPY(100)' || temp2[0].cur_unit === 'IDR(100)') {
        changeMoney.value = (temp[0].deal_bas_r.replace(/,/g,'')/temp2[0].deal_bas_r.replace(/,/g,'')* reChangeMoney.value*100).toFixed(2)
    } else {
        changeMoney.value = (temp[0].deal_bas_r.replace(/,/g,'')/temp2[0].deal_bas_r.replace(/,/g,'')* reChangeMoney.value).toFixed(2)
    }
}


const exchangeKorea = ref('')
// const exchangeKoreaTTS = ref(calculatorStore.exchange.filter(exchange => exchange.cur_unit === exchangeKorea.value))
const exchangeKoreaTTS = computed(()=>{
    if(calculatorStore.exchange.filter(exchange => exchange.cur_unit === exchangeKorea.value)[0]) {
        return calculatorStore.exchange.filter(exchange => exchange.cur_unit === exchangeKorea.value)[0].tts
    }
})
const exchangeKoreaTTB =  computed(()=>{
    if(calculatorStore.exchange.filter(exchange => exchange.cur_unit === exchangeKorea.value)[0]) {
        return calculatorStore.exchange.filter(exchange => exchange.cur_unit === exchangeKorea.value)[0].ttb
    }
})


// const filterOptions = function () {
//     // 변수 구성 수정하고 싶어
//     const inputCtr = document.getElementById('myInput').value.toUpperCase()
//     const options = document.getElementById("mySelect").getElementsByTagName("option")

//     for (let i = 0; i < options.length; i++) {
//         option = options[i]
//         if (option.value.toUpperCase().indexOf(inputCtr) > -1) {
//             option.style.display = ''
//         } else {
//             option.style.display = none
//         }  
//     }
// }



onMounted(() => {
    calculatorStore.getExchangeRate()
})
</script>

<style scoped>

</style>