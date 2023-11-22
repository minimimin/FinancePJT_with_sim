<template>
  <div class="container">
    <header class="head-box">
      <nav class="d-flex justify-content-between">
        <div class="left-link">
          <RouterLink :to="{ name: 'main' }">
            <img class="home-logo" src="@/assets/mini_sim_logo_small.png" alt="logo">
          </RouterLink>
          <RouterLink :to="{ name: 'financialProduct' }">금융상품 정보</RouterLink>
          <RouterLink :to="{ name: 'calculator' }">계산기</RouterLink>
          <RouterLink :to="{ name: 'map' }">은행 찾기</RouterLink>
          <RouterLink :to="{ name: 'articles' }">게시판</RouterLink>
        </div>
        
        <div class="right-link">
          <div v-if="!userStore.isLogin"> 
            <RouterLink :to="{ name: 'signup' }">회원가입</RouterLink>
            <RouterLink :to="{ name: 'login' }">로그인</RouterLink>
          </div>
          <div v-if="userStore.isLogin">
            <template v-if="userStore.isLogin && userStore.loginUser?.is_superuser">
              <RouterLink :to="{ name: 'categoryCreate' }">카테고리 관리</RouterLink>
            </template>
            <RouterLink :to="{ name: 'profile' }">마이 페이지</RouterLink>
            <button @click="userStore.logOut">로그아웃</button>
          </div>
        </div>
      </nav>
    </header>
    <article class="article-box">
      <RouterView />
    </article>
    <footer>

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
.left-link a {
  font-size: 35px;
  margin-right: 50px;
}
.right-link {
  margin-top: 5px;
  margin-right: 10px;
}
.right-link a {
  margin: 10px;
}
.article-box {
  margin: 20px;
  text-align: center;
}
</style>

<style>
/* 모든 파일에 적용할 CSS */
a {
  text-decoration: none;
  color: black;
}

button {
  border: none;
  background: none;
}

article > div {
  background-color: white;
  border-radius: 20px;
  padding: 20px;
  box-shadow: 5px 5px 5px gainsboro;
}
</style>