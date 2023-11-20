<template>
    <div>
        <h1>Region Names:</h1>
    <ul>
        <li v-for="region in regions" :key="region.id">{{ region.region_name }}</li>
    </ul>
    </div>
</template>

<style scoped>

</style>


<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue'

const regions = ref([])
const KAKAO_API_KEY = import.meta.env.VITE_CACAO_MAP_API_KEY
const KAKAO_API_URL = 'https://dapi.kakao.com/v2/local/geo/regions'


onMounted(() => {
    axios({
        method: 'get',
        url: KAKAO_API_URL,
        headers: {
        'Authorization': `KakaoAK ${KAKAO_API_KEY}`
    },
        params: {
            'category_group_code': 'region',
        }
    })
        .then((res) => {
            res.json()
        })
        .then((data) => {
            regions.value = data.documents.map(region => ({ id: region.id, region_name: region.region_1depth_name }))
        })
        .catch(error => console.error('Error fetching region names:', error));
})

</script>
