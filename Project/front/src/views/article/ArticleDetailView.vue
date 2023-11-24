<template>
  <div style="text-align: left;" v-if="articleStore.article">
    <div style="width: 50%; margin: 0 auto;">
    <p>{{ articleStore.article.category.name }}</p>
    <hr>
    <h1>{{ articleStore.article.title }}</h1>
    <div style="border-bottom: 1px solid #005c77; margin: 20px 0;"></div>
    <h5 style="margin-bottom: 20px;">{{ articleStore.article.content }}</h5>
    <div style="text-align: right; font-size: small;">
    <p>작성일: {{ articleStore.article.created_at.slice(0,10) +' ' + articleStore.article.created_at.slice(11,19) }},     
    수정일: {{ articleStore.article.updated_at.slice(0,10) +' ' + articleStore.article.updated_at.slice(11,19) }}</p>
    </div>
    <div style="text-align: right;" v-if="userStore.isLogin && articleStore.article.user === userStore.userPk">
      <button class="btn btn-sm small-submit-btn" @click="goUpdate">수정</button>
      <button class="btn btn-sm small-submit-btn" @click="articleDelete">삭제</button>
    </div>
    <div style="border-bottom: 1px solid #005c77; margin: 20px 0;"></div>
    <CommentItem
      v-for="comment in articleStore.comments"
      :key="comment.id"
      :comment="comment"
    />
    <form @submit.prevent="createComment">
      <label style="margin: 5px;" for="comment">내용 : </label>
      <input class="select-style" type="text" id="comment" v-model="inputComment">
      <input class="btn btn-sm small-submit-btn" style="margin-bottom: 5px;" type="submit" value="댓글 작성">
    </form>
  </div>
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
    url: `${userStore.API_URL}/articles/${articleId.value}/`,
    headers: {
      Authorization: `Token ${userStore.token}`
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
  if (!userStore.isLogin) {
    const confirmResult = confirm("로그인이 필요합니다. 로그인 페이지로 이동하시겠습니까?");
    if (confirmResult) {
      // 로그인 페이지로 이동
      router.push({ name: 'login' });
    }
    return; // 로그인이 되어있지 않으면 이후 코드 실행하지 않음
  }
  
  axios({
    method: 'post',
    url: `${userStore.API_URL}/articles/comment/${articleId.value}/`,
    data: {
      article: articleId.value,
      content: inputComment.value
    },
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then((res) => {
      inputComment.value = ''
      articleStore.getComments(articleId.value)
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>

</style>