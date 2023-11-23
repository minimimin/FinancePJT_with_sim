<template>
  <div>
    <h1>커뮤니티</h1>
    <div>
      <p v-for="category in store.categories" :key="category.id">{{ category.name }}</p>
    </div>
    <RouterLink :to="{ name: 'articleCreate' }">게시글 생성</RouterLink>
    <ArticleListItem
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { useArticleStore } from '@/stores/article'
import ArticleListItem from '@/components/article/ArticleListItem.vue'

const store = useArticleStore()

onMounted(() => {
  store.getArticles()
  store.getCategories()
})
</script>

<style scoped>

</style>