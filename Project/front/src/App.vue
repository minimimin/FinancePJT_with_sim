<template>
  <div class="container">
    <header class="head-box row">
      <RouterLink class="col-2" :to="{ name: 'main' }">
        <img class="home-logo" src="@/assets/mini_sim_logo_small.png" alt="logo">
      </RouterLink>
      <nav class="d-flex col-10" style="position: relative; ">
        <div class="right-link row">
          <div v-if="!userStore.isLogin"> 
            <RouterLink :to="{ name: 'signup' }">회원가입</RouterLink>
            <RouterLink :to="{ name: 'login' }">로그인</RouterLink>
          </div>
          <div v-if="userStore.isLogin">
            <p>{{ userStore.userName }}님</p>
            <template v-if="userStore.isLogin && userStore.loginUser?.is_superuser">
              <RouterLink :to="{ name: 'categoryCreate' }">카테고리 관리</RouterLink>
            </template>
            <RouterLink :to="{ name: 'profile' }">마이 페이지</RouterLink>
            <button @click="userStore.logOut">로그아웃</button>
          </div>
        </div>
        <div class="left-link row gap-4">
          <RouterLink :to="{ name: 'financialProduct' }">금융상품 정보</RouterLink>
          <RouterLink :to="{ name: 'exchange' }">환율계산기</RouterLink>
          <RouterLink :to="{ name: 'map' }">은행찾기</RouterLink>
          <RouterLink :to="{ name: 'articles' }">게시판</RouterLink>
        </div>
      </nav>
    </header>
    <article class="article-box">
      <RouterView />
    </article>
    <footer>
      <p>ⓒ copyright 2023 Mini_Sim. All rights reserved.</p>
      <p>thanks to. 지피티님, 조현제님, 양건우님</p>
    </footer>
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

</script>

<style scoped>
.head-box {
  background-color: #f6ffff;
  font-family: 'IBM Plex Sans KR', sans-serif;
  border-radius: 20px;
  box-shadow: 5px 5px 5px gainsboro;
  margin: 20px;
}
.home-logo {
  width: 130px;
  height: 130px;
  border-radius: 10px;
  margin: 10px;
}
.left-link {
  flex-wrap: nowrap;
  position: absolute;
  top: 50%;
  left: 35%;
  transform: translate(-50%, -50%);
}
.left-link a {
  width: max-content;
  font-size: 30px;
  font-weight: 500;
  /* color: #005c77; */
}
.right-link {
  position: absolute;
  margin-top: 5px;
  margin-right: 10px;
  right: 0;
}
.right-link a {
  margin: 10px;
}

.right-link p {
  display: inline-block;
}
.article-box {
  margin: 20px;
  text-align: center;
}

button {
  border: none;
  background: none;
}

footer {
  text-align: center;
  background-color: white;
  border-radius: 20px;
  box-shadow: 5px 5px 5px gainsboro;
  margin: 20px;
  padding: 20px;
}

footer p {
  margin: 10px;
}
</style>

<style>
/* 모든 파일에 적용할 CSS */
a {
  text-decoration: none;
  color: black;
}

/* button {
  border: 3px solid #005c77;
  border-radius: 10px;
  background: #f6ffff;
  padding: 3px 10px 3px;
  font-weight: bold;
  color: #005c77;
} */

article > div {
  background-color: white;
  border-radius: 20px;
  padding: 20px;
  box-shadow: 5px 5px 5px gainsboro;
}

/* form input {
  border: 1px solid #1f87a1;
  border-radius: 10px;
} */
.select-box {
  margin: 20px;
}

.hr-line{
  width: 75%;
  margin: 20px auto;
  border-bottom: 1px solid #005c77;
}
.submit-btn {
  background-color: #0c768b;
  color: white;
  padding: 5px 30px;
  margin: 20px;
}

.select-style {
  border: 1px solid #0c768b;
  border-radius: 5px;
}

.small-submit-btn {
  background-color: #0c768b;
  color: white;
  margin: 2px;
}

.medium-title {
  margin: 20px;
  font-size: large;
  font-weight: 500;
}

.medium-legend {
  font-size: large;
  font-weight: 500;
}

</style>