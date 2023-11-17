<template>
  <div>
    <p>{{ article.category.name }}</p>
    <h3 @click="goDetail">{{ article.id }}번 글 | {{ article.title }}</h3>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const props = defineProps({
  article: Object
})

const goDetail = function () {
  router.push({ name: 'articleDetail', params: { id: props.article.id }})
}
</script>

<style scoped>

</style>