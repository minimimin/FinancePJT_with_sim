<template>
  <div v-if="articleStore.article">
    <h1>게시글 상세 정보</h1>
    <p>{{ articleStore.article.category.name }}</p>
    <p>{{ articleStore.article.id }}번 글</p>
    <h2>{{ articleStore.article.title }}</h2>
    <hr>
    <p>작성일: {{ articleStore.article.created_at }}</p>
    <p>수정일: {{ articleStore.article.updated_at }}</p>
    <hr>
    <p>{{ articleStore.article.content }}</p>
    <div v-if="userStore.isLogin && articleStore.article.user === userStore.userPk">
      <button @click="goUpdate">수정</button>
      <button @click="articleDelete">삭제</button>
    </div>
    <hr>
    <CommentItem
      v-for="comment in articleStore.comments"
      :key="comment.id"
      :comment="comment"
    />
    <form @submit.prevent="createComment">
      <label for="comment">내용 : </label>
      <input type="text" id="comment" v-model="inputComment">
      <input type="submit" value="댓글 작성">
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useArticleStore } from '@/stores/article'
import CommentItem from '@/components/article/CommentItem.vue'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()
const articleStore = useArticleStore()
const articleId = ref(route.params.id)
const inputComment = ref(null)

onMounted(() => {
  articleStore.getDetail(articleId.value)
  articleStore.getComments(articleId.value)
})

const goUpdate = function () {
  router.push({ name: 'articleUpdate', params: { id: articleId.value}})
}

const articleDelete = function () {
  axios({
    method: 'delete',
    url: `${articleStore.API_URL}/articles/${articleId.value}/`,
    headers: {
      Authorization: `Token ${token.value}`
    }
  })
    .then((res) => {
      router.push({ name: 'articles'})
    })
    .catch((err) => {
      console.log(err)
    })
}

const createComment = function () {
  axios({
    method: 'post',
    url: `${articleStore.API_URL}/articles/comment/${articleId.value}/`,
    data: {
      article: articleId.value,
      content: inputComment.value
    },
    headers: {
      Authorization: `Token ${token.value}`
    }
  })
    .then((res) => {
      articleStore.getComments(articleId.value)
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>

</style>