<template>
  <div>
    <h1>게시글 수정 페이지</h1>
    <form @submit.prevent="updateArticle">
      <label for="category">카테고리 선택:</label><br>
      <select id="category" v-model="existingCategory">
        <option disabled value="">카테고리를 선택하세요</option>
        <option v-for="category in store.categories" 
        :key="category.id" :value="category.id">{{ category.name }}</option>
      </select><br>
      <label for="title">제목:</label><br>
      <input type="text" id="title" v-model="existingTitle"><br>
      <label for="content">내용:</label><br>
      <textarea id="content" v-model="existingContent" cols="30" rows="10"></textarea><br>
      <input type="submit" value="게시글 수정">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const store = useArticleStore()
const articleId = ref(route.params.id)

const existingTitle = ref(store.article.title)
const existingContent = ref(store.article.content)
const existingCategory = ref(store.article.category.id)

const updateArticle = function () {
    axios({
      method: 'put',
      url: `${store.API_URL}/articles/${articleId.value}/`,
      data: {
        title: existingTitle.value,
        content: existingContent.value,
        category: existingCategory.value,
      }
    })
      .then((res) => {
        router.push({ name: 'articleDetail', params: { id: articleId.value} })
      })
      .catch((err) => {
        console.log(err)
      })
}
</script>

<style scoped>

</style>