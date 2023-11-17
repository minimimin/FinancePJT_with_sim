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
      url: `${store.API_URL}/api/v1/category/`,
      data: {
        name: inputCategory.value
      }
    })
      .then((res) => {
        // console.log(res.data)
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }


</script>

<style scoped>

</style>