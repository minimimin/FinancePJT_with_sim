<template>
  <div v-if="store.article">
    <h1>게시글 상세 정보</h1>
    <p>{{ store.article.category.name }}</p>
    <p>{{ store.article.id }}번 글</p>
    <h2>{{ store.article.title }}</h2>
    <hr>
    <p>작성일: {{ store.article.created_at }}</p>
    <p>수정일: {{ store.article.updated_at }}</p>
    <hr>
    <p>{{ store.article.content }}</p>
    <button @click="goUpdate">수정</button>
    <button @click="articleDelete">삭제</button>
    <hr>
    <CommentItem
      v-for="comment in store.comments"
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
import { useArticleStore } from '@/stores/article'
import CommentItem from '@/components/article/CommentItem.vue'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const store = useArticleStore()
const articleId = ref(route.params.id)
const inputComment = ref(null)

onMounted(() => {
  store.getDetail(articleId.value)
  store.getComments(articleId.value)
})

const goUpdate = function () {
  router.push({ name: 'articleUpdate', params: { id: articleId.value}})
}

const articleDelete = function () {
  axios({
    method: 'delete',
    url: `${store.API_URL}/articles/${articleId.value}/`,
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
    url: `${store.API_URL}/articles/comment/${articleId.value}/`,
    data: {
      article: articleId.value,
      content: inputComment.value
    }
  })
    .then((res) => {
      store.getComments(articleId.value)
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>

</style>