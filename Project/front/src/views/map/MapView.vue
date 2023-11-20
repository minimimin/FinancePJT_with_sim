<template>
  <div>
    <h1>지도 페이지</h1>
    <div id="map" style="width:800px;height:500px;"></div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  const container = document.getElementById('map');
  const options = {
    center: new kakao.maps.LatLng(33.450701, 126.570667),
    level: 3
  };

  const map = new kakao.maps.Map(container, options);
})  
</script>

<style scoped>

</style>