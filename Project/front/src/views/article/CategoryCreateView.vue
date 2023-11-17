<template>
  <div>
    <form @submit.prevent="createCategory">
      <label for="category">Category 종류:</label><br>
      <input type="text" id="category" v-model="inputCategory"><br>
      <input type="submit" value="카테고리 생성">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'
import axios from 'axios'

const router = useRouter()
const store = useArticleStore()
const inputCategory = ref(null)

const createCategory = function () {
    axios({
      method: 'post',
      url: `${store.API_URL}/articles/category/detail/`,
      data: {
        name: inputCategory.value
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }


</script>

<style scoped>

</style>