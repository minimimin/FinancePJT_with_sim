<template>
  <div>
    <div style="display: flex; align-items: center;">
  <p style="display: inline-block; flex-grow: 1; margin-right: 10px; margin-bottom: 0;">{{ comment.content }}</p>
  <button class="btn btn-sm small-submit-btn" v-if="userStore.isLogin && comment.user === userStore.userPk" @click="commentDelete">삭제</button>
</div>
<hr>
    <!-- <p style="display: inline-block;">{{ comment.content }}</p>
    <button class="btn btn-sm small-submit-btn" style="margin-bottom: 5px;" v-if="userStore.isLogin && comment.user === userStore.userPk" @click="commentDelete">삭제</button>
    <hr> -->
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useArticleStore } from '@/stores/article'
import axios from 'axios'

const route = useRoute()
const userStore = useUserStore()
const articleStore = useArticleStore()
const articleId = ref(route.params.id)

const props = defineProps({
  comment: Object
})

const commentDelete = function () {
  axios({
    method: 'delete',
    url: `${articleStore.API_URL}/articles/comment/detail/${props.comment.id}/`,
    headers: {
    Authorization: `Token ${userStore.token}`
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