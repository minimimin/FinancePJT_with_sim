<template>
  <div>
    <h1>커뮤니티</h1>
    <div class="category-box">
      | <template  v-for="category in articleStore.categories" :key="category.id">
      <p class="category-menu">{{ category.name }}</p>  |
      </template>
    </div>
    <RouterLink @click="handleCreateArticle" class="btn submit-btn" :to="{ name: 'articleCreate' }">게시글 생성</RouterLink>
    <ArticleListItem
      v-for="article in articleStore.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useArticleStore } from '@/stores/article'
import ArticleListItem from '@/components/article/ArticleListItem.vue'

const userStore = useUserStore()
const articleStore = useArticleStore()
const router = useRouter()

onMounted(() => {
  articleStore.getArticles()
  articleStore.getCategories()
})

const handleCreateArticle = () => {
  // 로그인 여부 확인
  if (!userStore.isLogin) {
    const confirmResult = confirm("로그인이 필요합니다. 로그인 페이지로 이동하시겠습니까?");
    if (confirmResult) {
      // 로그인 페이지로 이동
      router.push({ name: 'login' });
    }
    return; // 로그인이 되어있지 않으면 이후 코드 실행하지 않음
  } 

  router.push({ name: 'articleCreate' });
}

</script>

<style scoped>
.category-box {
  font-size: 18px;
  font-weight: 500;
  margin: 20px;
  border-top: 2px solid #0c768b;
  border-bottom: 2px solid #0c768b;
}

.category-menu {
  display: inline-block;
  margin: 10px;
}
</style>