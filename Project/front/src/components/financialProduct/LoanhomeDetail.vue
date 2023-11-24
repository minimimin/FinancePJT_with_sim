<template>
  <div class="detail-box">
    <h1>{{ financialProductStore.loanDetail?.kor_co_nm }} {{ financialProductStore.loanDetail?.fin_prdt_nm }}</h1>
    <div class="hr-line"></div>
    <div  class="pre-line">
        대출한도 : {{ financialProductStore.loanDetail?.loan_lmt }}
      <br>
      <br>
        대출 부대비용 : <br>{{ financialProductStore.loanDetail?.loan_inci_expn }}
      <br>
      <br>
        중도상환 수수료 : <br>{{ financialProductStore.loanDetail?.erly_rpay_fee }}
      <br>
      <br>
        연체 이자율 : <br>{{ financialProductStore.loanDetail?.dly_rate }}
      <br>
      </div>
      <div class="hr-line"></div>

      <h6>금융상품 목록(총 {{ financialProductStore.loanDetail?.loan_home_product_option.length }}개)</h6>
      <!-- 여기서부터 v-for를 돌면서 찾아내야한다! -->
      <p style="font-size: 15px; margin-top: 20px;">* 아래 대출 금리는 소수점 2자리에서 반올림 한 값입니다.</p>
      <!-- 글씨 작게 + 오른쪽 끝으로 정렬되게 만들기! -->
      <div class="d-flex justify-content-center" >
      <table   class="table table-hover table-box" style="width: 70%;">
        <thead>
          <tr>
            <th>NO.</th>
            <th>금리유형</th>
            <th>평균금리</th>
            <th>최저대출금리</th>
            <th>최대대출금리</th>
            <!-- <th>상품가입</th> -->
          </tr>
        </thead>
        <tbody>
          <tr v-for="loan_home in financialProductStore.loanDetail?.loan_home_product_option" :key="loan_home.id">
            <td>{{ loan_home.id }}</td>
            <!-- 사실 id로 하면 안되고 순서로 하고 싶은데,,, -->
            <td>{{ loan_home.lend_rate_type_nm }}</td>
            <td>{{ loan_home.lend_rate_avg }}</td>
            <td >{{ loan_home.lend_rate_min }}</td>
            <td >{{ loan_home.lend_rate_max }}</td>
            <!-- <td><button>가입하기</button></td> -->
          </tr>
        </tbody>
      </table>
      </div>


      <!-- <div v-for="loan_home in financialProductStore.loanDetail?.loan_home_product_option">
        <br>
        <br>
        <br>
          금리유형 : {{ loan_home.lend_rate_type_nm }}
        <br>
        <br>
          평균금리(소수점 2자리) : {{ loan_home.lend_rate_avg }}
        <br>
        <br>
          최저대출금리(소수점 2자리) : {{ loan_home.lend_rate_min }}
        <br>
        <br>
          최대대출금리(소수점 2자리) : {{ loan_home.lend_rate_max }}
        <br>
        <br>
        <button>가입하기</button>
        (가입한 상품 목록에 저장하는 것으로 설정하기!)
      </div> -->
    </div>

</template>

<script setup>
import { useFinancialProductStore } from '@/stores/financialproduct'
const financialProductStore = useFinancialProductStore()

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