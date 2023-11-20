<template>
  <div>
    <form @submit.prevent="createCategory">
      <label for="category">Category 종류:</label><br>
      <input type="text" id="category" v-model="inputCategory"><br>
      <input type="submit" value="카테고리 생성">
    </form>
    <br>
    <h4>카테고리 목록</h4>
    <p v-for="category in articleStore.categories" :key="category.id">{{ category.name }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useArticleStore } from '@/stores/article'
import axios from 'axios'

const router = useRouter()
const userStore = useUserStore()
const articleStore = useArticleStore()
const inputCategory = ref(null)

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


</script>

<style scoped>

</style>