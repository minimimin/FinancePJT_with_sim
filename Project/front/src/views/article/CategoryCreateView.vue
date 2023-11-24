<template>
  <div>
    <h3>카테고리 관리</h3>
    <form @submit.prevent="createCategory">
      <label style="margin: 5px;" for="article-category">Category 이름 :</label><br>
      <input class="select-style" type="text" id="article-category" v-model="inputCategory"><br>
      <input class="btn submit-btn" type="submit" value="카테고리 생성">
    </form>
    <div class="hr-line"></div>
    <h4>카테고리 목록</h4>
    <div style="width: 170px; margin: 20px auto;">
    <p style="text-align: right; margin: 5px;" v-for="category in articleStore.categories" :key="category.id">
      {{ category.name }}
      <button class="btn btn-sm small-submit-btn" @click="goCategoryUpdate(category.id)">수정</button>
      <button class="btn btn-sm small-submit-btn"  @click="categoryDelete(category.id)">삭제</button>
    </p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useArticleStore } from '@/stores/article'
import axios from 'axios'

const router = useRouter()
const userStore = useUserStore()
const articleStore = useArticleStore()
const inputCategory = ref(null)

onMounted(() => {
  articleStore.getCategories()
})

const createCategory = function () {
    axios({
      method: 'post',
      url: `${userStore.API_URL}/articles/category/detail/`,
      data: {
        name: inputCategory.value
      },
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
      .then((res) => {
        articleStore.getCategories()
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const goCategoryUpdate = function (categoryId) {
  router.push({ name: 'CategoryUpdate', params: {id : categoryId}})
}

const categoryDelete = function (categoryId) {
  axios({
    method: 'delete',
    url: `${userStore.API_URL}/articles/category/detail/`,
    data: {categoryId},
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then((res) => {
      articleStore.getCategories()
      router.push({ name: 'categoryCreate'})
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>

<style scoped>

</style>