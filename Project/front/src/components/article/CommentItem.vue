<template>
  <div>
    <p>{{ comment.user }} : {{ comment.content }}</p>
    <button @click="commentDelete">삭제</button>
    <hr>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useArticleStore } from '@/stores/article'
import axios from 'axios'

const route = useRoute()
const store = useArticleStore()
const articleId = ref(route.params.id)

const props = defineProps({
  comment: Object
})

const commentDelete = function () {
  axios({
    method: 'delete',
    url: `${store.API_URL}/articles/comment/detail/${props.comment.id}/`,
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