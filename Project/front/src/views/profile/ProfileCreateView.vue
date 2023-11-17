<template>
  <div>
    <h1>{{ user_pk }}님의 PROFILE</h1>
    <hr>
    <p>상세 정보를 입력해주세요.</p>
    <!--age, money, salary, job, main_bank, 
      stabillity, banking_products, card_products-->
    <form >
      <label for="age">나이 :  </label>
      <input type="number" id="age" min=0 max=200 value="숫자를 입력해주세요">
      
      <br>
      
      <label for="money">자산 : </label>
      <input type="number" id="money" value="숫자를 입력해주세요">
      

      <fieldset>
        <legend>직업</legend>
        <div>
          <input type="radio" id="학생 및 주부" name="job" value="학생 및 주부" checked />
          <label for="학생 및 주부">학생 및 주부</label>
        </div>

        <div>
          <input type="radio" id="사업가 및 프리랜서" name="job" value="사업가 및 프리랜서" />
          <label for="사업가 및 프리랜서">사업가 및 프리랜서</label>
        </div>

        <div>
          <input type="radio" id="회사원" name="job" value="회사원" />
          <label for="회사원">회사원</label>
        </div>

        <div>
          <input type="radio" id="기타" name="job" value="기타" onchange="toggleTextField()"/> 
          <label for="기타">기타</label>
          <input type="text" id="기타TextField" disabled>
        </div>
      </fieldset>
      <!-- <label for="job">직업 : </label>
      <div id="job">
        <input type="radio">
      </div> -->

      

    </form>
  </div>
</template>

<script setup>
const toggleTextField = function() {
      const radio = document.getElementById('기타');
      const textField = document.getElementById('기타TextField');

      // '기타' 라디오 버튼이 선택되었을 때
      if (radio.checked) {
        textField.disabled = false; // 텍스트 필드를 활성화
      } else {
        textField.disabled = true; // 텍스트 필드를 비활성화
      }
    }


</script>

<style scoped>

</style>