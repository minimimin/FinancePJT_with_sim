import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const categories = ref([])
  const comments = ref([])
  const article = ref(null)
  const API_URL = 'http://127.0.0.1:8000'

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/articles/`
    })
      .then((res) => {
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getCategories = function () {
    axios({
      method: 'get',
      url: `${API_URL}/category/`
    })
      .then((res) => {
        categories.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getComments = function (articleId) {
    axios({
      method: 'get',
      url: `${API_URL}/comment/${articleId}`
    })
      .then((res) => {
        comments.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getDetail = function (articleId) {
    axios({
      method: 'get',
      url: `${API_URL}/articles/${articleId}/`,
    })
      .then((res) => {
        article.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  return { articles, categories, comments, article, API_URL, getArticles, getCategories, getComments, getDetail }
}, { persist: true })