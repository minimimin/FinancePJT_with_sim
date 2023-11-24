<template>
  <div>
    <h1>게시글 쓰기</h1>
    <div class="hr-line"></div>
    <form @submit.prevent="createArticle">
      <div class="select-box">
        <label style="margin: 5px;" for="article-category">카테고리 선택:</label><br>
        <select class="select-style" id="article-category" v-model="selectedCategory">
          <option disabled value="">카테고리를 선택하세요</option>
          <option v-for="category in articleStore.categories" 
          :key="category.id" :value="category.id">{{ category.name }}</option>
        </select>
      </div>
      <div class="select-box">
        <label for="title">제목:</label><br>
        <input class="select-style"  type="text" id="title" v-model="inputTitle">
      </div>
      <div class="select-box">
        <label for="content">내용:</label><br>
        <textarea class="select-style"  id="content" v-model="inputContent" cols="30" rows="10"></textarea>
      </div>
      <input class="btn submit-btn" type="submit" value="게시글 생성">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useArticleStore } from '@/stores/article'
import axios from 'axios'

const inputTitle = ref(null)
const inputContent = ref(null)
const selectedCategory = ref('')
const userStore = useUserStore()
const articleStore = useArticleStore()
const router = useRouter()

const createArticle = function () {
    axios({
      method: 'post',
      url: `${userStore.API_URL}/articles/`,
      data: {
        title: inputTitle.value,
        content: inputContent.value,
        category: selectedCategory.value,
      },
      headers: {
      Authorization: `Token ${userStore.token}`
      }
    })
      .then((res) => {
        router.push({ name: 'articles' })
      })
      .catch((err) => {
        console.log(err)
      })
  }
</script>

<style scoped>

</style>