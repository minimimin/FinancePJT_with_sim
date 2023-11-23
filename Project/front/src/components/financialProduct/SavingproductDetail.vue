<template>
  <div>
<h1>[적금 상품 상세]</h1>
    <div class="pre-line">
      <br>
      은행명 : {{ financialProductStore.savingDetail?.kor_co_nm }}
      <br>
      <br>
      상품명 : {{ financialProductStore.savingDetail?.fin_prdt_nm }}
      <br>
      <br>
      가입방법 : {{ financialProductStore.savingDetail?.join_way }}
      <br>
      <br>
      가입 대상 : {{ financialProductStore.savingDetail?.join_member }}
      <br>
      <br>
      가입 제한 : {{ financialProductStore.savingDetail?.join_deny }}
      <br>
      <br>
      최고 한도 : {{ financialProductStore.savingDetail?.max_limit }}
      <br>
      <br>
      우대조건 : 
      <br>{{ financialProductStore.savingDetail?.spcl_cnd }}
      <br>
      <br>
      만기 후 이자율 : 
      <br>{{ financialProductStore.savingDetail?.mtrt_int }}
      <br>
      <br>
      유의사항 : <br>{{ financialProductStore.savingDetail?.etc_note }}
      <br>
      
      <p>
        <hr style="margin-top: 50px;">
      <!-- 금융상품 목록(총 {{ financialProductStore.savingDetail?.saving_product_option.length }}개) :  -->
      <div class="d-flex justify-content-center" style="margin-top: 30px;">
      <table>
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
            <tr v-for="saving_detail in financialProductStore.savingDetail?.saving_product_option" :key="saving_detail.id">
              <td>{{ saving_detail.id }}</td>
              <!-- 사실 id로 하면 안되고,,나오는 순서로 하고 싶은데,,, -->
              <td>{{ saving_detail.intr_rate_type_nm }}</td>
              <td>{{ saving_detail.intr_rate }}</td>
              <td >{{ saving_detail.intr_rate2 }}</td>
              <td>{{ saving_detail.save_trm }}</td>
              <!-- <td><button>가입하기</button></td> -->
            </tr>
          </tbody>
        </table>
      </div>
      <!-- <p v-for="saving_detail in financialProductStore.savingDetail?.saving_product_option">
        <br>
      저축금리유형명 : {{ saving_detail.intr_rate_type_nm }}
      <br>
      저축금리 : {{ saving_detail.intr_rate }}
      <br>
      최고 우대금리: {{ saving_detail.intr_rate2 }}
      <br>
      저축기간 : {{ saving_detail.save_trm }}
      <br>
      <button>가입하기</button>
      </p> -->
      <br>
      <hr>
    </p>
    </div>

  </div>
</template>

<script setup>
// import { ref } from 'vue'
import { useFinancialProductStore } from '@/stores/financialproduct'
const financialProductStore = useFinancialProductStore()
// const savingDetail = ref(financialProductStore.savingDetail)

</script>

<style scoped>
.pre-line {
  white-space: pre-line;
}
</style>