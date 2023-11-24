<template>
  <div>
    <h3>카테고리 수정</h3>
    <form @submit.prevent="updateCategory(categoryId)">
      <label style="margin: 5px;" for="article-category">Category 이름 :</label><br>
      <input class="select-style" type="text" id="article-category" v-model="existingCategory"><br>
      <input class="btn submit-btn" type="submit" value="카테고리 수정">
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useArticleStore } from '@/stores/article'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()
const articleStore = useArticleStore()
const categoryId = ref(route.params.id)
const existingCategory = ref('')

onMounted(() => {
  // articleStore.getCategories()
  const foundCategory = articleStore.categories.find(category => category.id == categoryId.value)
  if (foundCategory) {
    existingCategory.value = foundCategory.name
  }
})

const updateCategory = function (categoryId) {
    axios({
      method: 'put',
      url: `${userStore.API_URL}/articles/category/detail/`,
      data: {id: categoryId, name:existingCategory.value},
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
      .then((res) => {
        articleStore.getCategories()
        router.push({name: 'categoryCreate'})
      })
      .catch((err) => {
        console.log(err)
      })
  }

</script>

<style scoped>

</style>