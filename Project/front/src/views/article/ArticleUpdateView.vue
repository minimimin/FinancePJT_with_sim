<template>
  <div>
    <h1>게시글 수정하기</h1>
    <form @submit.prevent="updateArticle">
      <div class="select-box">
      <label style="margin: 5px;" for="article-category">카테고리 선택:</label><br>
      <select class="select-style"  id="article-category" v-model="existingCategory">
        <option disabled value="">카테고리를 선택하세요</option>
        <option v-for="category in articleStore.categories" 
        :key="category.id" :value="category.id">{{ category.name }}</option>
      </select><br>
    </div>
    <div class="select-box">
      <label style="margin: 5px;"  for="title">제목:</label><br>
      <input class="select-style"  type="text" id="title" v-model="existingTitle"><br>
    </div>
    <div class="select-box">
      <label style="margin: 5px;"  for="content">내용:</label><br>
      <textarea class="select-style"  id="content" v-model="existingContent" cols="30" rows="10"></textarea><br>
    </div>
      <input class="btn submit-btn" type="submit" value="게시글 수정">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useArticleStore } from '@/stores/article'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()
const articleStore = useArticleStore()
const articleId = ref(route.params.id)

const existingTitle = ref(articleStore.article.title)
const existingContent = ref(articleStore.article.content)
const existingCategory = ref(articleStore.article.category.id)

const updateArticle = function () {
    axios({
      method: 'put',
      url: `${userStore.API_URL}/articles/${articleId.value}/`,
      data: {
        title: existingTitle.value,
        content: existingContent.value,
        category: existingCategory.value,
      },
      headers: {
        Authorization: `Token ${userStore.token}`
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