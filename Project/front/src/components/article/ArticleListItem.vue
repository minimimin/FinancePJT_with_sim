<template>
  <div>
    <table class="table table-hover table-box " style="width: 70%; margin: 0 auto;">
      <thead>
        <tr>
        <th scope="col">NO.</th>
        <th scope="col">카테고리</th>
        <th scope="col">제목</th>
        </tr>
      </thead>
      <tbody>
        <tr @click="goDetail">
          <td>{{ article.id }}</td>
          <td>{{ article.category.name }}</td>
          <td>{{ article.title }}</td>
        </tr>
      </tbody>
    </table>
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