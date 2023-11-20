<template>
  <div>
    <h1>지도 페이지</h1>
    <div id="map" style="width:800px;height:600px;"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const latitude = ref(36.107793)
const longitude = ref(128.416801)

const createMap = function () {
  // Kakao Map API를 사용하여 현재 위치를 기반으로 지도 생성
  const container = document.getElementById('map')
  const options = {
    center: new kakao.maps.LatLng(latitude.value, longitude.value),
    level: 3,
  }
  const map = new kakao.maps.Map(container, options)
}

function successCallback (position) {
  latitude.value = position.coords.latitude
  longitude.value = position.coords.longitude
  createMap()
}

function errorCallback(error) {
  createMap()
}

onMounted(() => {
  // 현재 위치 가져오기
  navigator.geolocation.getCurrentPosition(successCallback, errorCallback)
})
</script>

<style scoped>

</style>