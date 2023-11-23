<template>
  <div>
<h1>여기는 예금 디테일 페이지!</h1>
    <div class="pre-line">
      <br>
      은행명 : {{ financialProductStore.depositDetail?.kor_co_nm }}
      <br>
      <br>
      상품명 : {{ financialProductStore.depositDetail?.fin_prdt_nm }}
      <br>
      <br>
      가입방법 : {{ financialProductStore.depositDetail?.join_way }}
      <br>
      <br>
      가입 대상 : {{ financialProductStore.depositDetail?.join_member }}
      <br>
      <br>
      가입 제한 : {{ financialProductStore.depositDetail?.join_deny }}
      <br>
      <br>
      최고 한도 : {{ financialProductStore.depositDetail?.max_limit }}
      <br>
      <br>
      우대조건 : {{ financialProductStore.depositDetail?.spcl_cnd }}
      <br>
      <br>
      만기 후 이자율 : 
      <br>{{ financialProductStore.depositDetail?.mtrt_int }}
      <br>
      <br>
      유의사항 : <br>{{ financialProductStore.depositDetail?.etc_note }}
      <br>
      
      <p>
        <hr>
      <!-- 금융상품 목록(총 {{ financialProductStore.depositDetail?.deposit_product_option.length }}개) :  -->
      <table>
  <thead>
    <tr>
      <th>NO.</th>
      <th>저축금리유형</th>
      <th>저축금리</th>
      <th>최고 우대금리</th>
      <th>저축기간</th>
      <th>상품 가입</th>/
    </tr>
  </thead>

  <tbody>
    <tr v-for="deposit_detail in financialProductStore.depositDetail?.deposit_product_option" :key="deposit_detail.id">
      <td>{{ deposit_detail.id }}</td>
      <!-- 사실 id로 하면 안되고 순서로 하고 싶은데,,, -->
      <td>{{ deposit_detail.intr_rate_type_nm }}</td>
      <td>{{ deposit_detail.intr_rate }}</td>
      <td >{{ deposit_detail.intr_rate2 }}</td>
      <td>{{ deposit_detail.save_trm }}</td>
      <td><button>가입하기</button></td>
    </tr>
  </tbody>
</table>




      <br>
      <br>
      <!-- <p v-for="deposit_detail in financialProductStore.depositDetail?.deposit_product_option">
        <br>
      저축금리유형명 : {{ deposit_detail.intr_rate_type_nm }}
      <br>
      저축금리 : {{ deposit_detail.intr_rate }}
      <br>
      최고 우대금리: {{ deposit_detail.intr_rate2 }}
      <br>
      저축기간 : {{ deposit_detail.save_trm }} -->
      <!-- <br>
      <button>가입하기</button>
      </p> -->
      <br>
      <hr>
    </p>
    </div>

  </div>
</template>

<script setup>
// import { ref, onMounted } from 'vue'
// import { useRoute } from 'vue-router'
import { useFinancialProductStore } from '@/stores/financialproduct'

// const route = useRoute()
const financialProductStore = useFinancialProductStore()

// const deposit_id = ref(route.params.id)

// onMounted(() => {
//   financialProductStore.getDepositProductDetail(deposit_id.value)
// })

</script>

<style scoped>
.pre-line {
  white-space: pre-line;
}
</style>