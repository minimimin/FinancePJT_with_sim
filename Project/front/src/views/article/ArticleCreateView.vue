<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="createArticle">
      <label for="category">카테고리 선택:</label><br>
      <select id="category" v-model="selectedCategory">
        <option disabled value="">카테고리를 선택하세요</option>
        <option v-for="category in articleStore.categories" 
        :key="category.id" :value="category.id">{{ category.name }}</option>
      </select>
      <br>
      <label for="title">제목:</label><br>
      <input type="text" id="title" v-model="inputTitle">
      <br>
      <label for="content">내용:</label><br>
      <textarea id="content" v-model="inputContent" cols="30" rows="10"></textarea>
      <br>
      <input type="submit" value="게시글 생성">
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