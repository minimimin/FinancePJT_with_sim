<template>
  <div class="detail-box">
<h1>{{ financialProductStore.depositDetail?.kor_co_nm }} {{ financialProductStore.depositDetail?.fin_prdt_nm }}</h1>
<!-- deposit_id 이거를 params로 받아온다는 말이지?! -->
<!-- <button @click="goSignUpBank(deposit_id)">가입하기</button> -->
<div class="hr-line"></div>
    <div class="pre-line">
      가입방법 : {{ financialProductStore.depositDetail?.join_way }}<br><br>
      가입 대상 : {{ financialProductStore.depositDetail?.join_member }}<br><br>
      가입 제한 : {{ financialProductStore.depositDetail?.join_deny }}<br><br>
      최고 한도 : {{ financialProductStore.depositDetail?.max_limit }}<br><br>
      우대조건 : {{ financialProductStore.depositDetail?.spcl_cnd }}<br><br>
      만기 후 이자율 : <br>{{ financialProductStore.depositDetail?.mtrt_int }}<br><br>
      유의사항 : <br>{{ financialProductStore.depositDetail?.etc_note }}<br>
    </div>
      <div class="hr-line"></div>
      <!-- 금융상품 목록(총 {{ financialProductStore.depositDetail?.deposit_product_option.length }}개) :  -->
      <div class="d-flex justify-content-center" style="margin-top: 30px;">
      <table  class="table table-hover table-box" style="width: 70%;">
        <thead>
          <tr>
            <th>NO.</th>
            <th>저축금리유형</th>
            <th>저축금리</th>
            <th>최고 우대금리</th>
            <th>저축기간</th>
            <!-- <th>상품 가입</th> -->
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
            <!-- <td><button>가입하기</button></td> -->
          </tr>
        </tbody>
      </table>
    </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useFinancialProductStore } from '@/stores/financialproduct'
import axios from 'axios'


const route = useRoute()
const router = useRouter()
const userStore = useUserStore()
const financialProductStore = useFinancialProductStore()

const deposit_id = ref(route.params.deposit_id)

// const goSignUpBank = function (deposit_id) {
//   axios({
//       method: 'post',
//       url: `${userStore.API_URL}/users/profile/${deposit_id}/deposit/`,
//       data: {
//         deposit_detail_id: financialProductStore.depositDetail.id,
//       },
//       headers: {
//       Authorization: `Token ${userStore.token}`
//       }
//     })
//       .then((res) => {
//         router.push({ name: 'depositProductDetail' })
//       })
//       .catch((err) => {
//         console.log(err)
//       })
// }


// onMounted(() => {
//   financialProductStore.getDepositProductDetail(deposit_id.value)
// })

</script>

<style scoped>
.pre-line {
  white-space: pre-line;
  text-align: left;
  width: 50%;
  margin-left: 28%;
}

.detail-box {
  padding: 30px;
}

.hr-line{
  width: 75%;
  margin: 20px auto;
  border-bottom: 1px solid #005c77;
}
</style>