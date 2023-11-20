<template>
  <h1>지도 페이지</h1>
  <nav>

  </nav>
  <div id="container" class="view_map">
    <div id="mapWrapper" style="width:100%;height:100%;position:relative;">
        <div id="map" style="width:100%;height:100%"></div> <!-- 지도를 표시할 div 입니다 -->
        <input type="button" id="btnRoadview" onclick="toggleMap(false)" title="로드뷰 보기" value="로드뷰">
    </div>
    <div id="rvWrapper" style="width:100%;height:100%;position:absolute;top:0;left:0;">
        <div id="roadview" style="height:100%"></div> <!-- 로드뷰를 표시할 div 입니다 -->
        <input type="button" id="btnMap" onclick="toggleMap(true)" title="지도 보기" value="지도">
    </div>
  </div>
  <!-- <div id="map" style="width:1200px;height:700px;"></div> -->
</template>

<script setup>
import { ref, onMounted } from 'vue'

// 경도, 위도 초기값 (구미 캠퍼스)
const latitude = ref(36.107793)
const longitude = ref(128.416801)

const createMap = function () {
  // Kakao Map API를 사용하여 현재 위치를 기반으로 지도 생성
  const mapContainer = document.getElementById('map')
  const options = {
    center: new kakao.maps.LatLng(latitude.value, longitude.value),
    level: 3,
  }
  const map = new kakao.maps.Map(mapContainer, options)

  // 여기부터 지도 커스텀

  // 일반 지도와 스카이뷰로 지도 타입을 전환할 수 있는 지도타입 컨트롤을 생성합니다
  var mapTypeControl = new kakao.maps.MapTypeControl();

  // 지도 타입 컨트롤을 지도에 표시합니다
  map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);

  // 지도 확대 축소를 제어할 수 있는  줌 컨트롤을 생성합니다
  var zoomControl = new kakao.maps.ZoomControl();
  map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);
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
#container {overflow:hidden;width:75vw;height:75vh;position:relative;}
#btnRoadview,  #btnMap {position:absolute;top:5px;left:5px;padding:7px 12px;font-size:14px;border: 1px solid #dbdbdb;background-color: #fff;border-radius: 2px;box-shadow: 0 1px 1px rgba(0,0,0,.04);z-index:1;cursor:pointer;}
#btnRoadview:hover,  #btnMap:hover{background-color: #fcfcfc;border: 1px solid #c1c1c1;}
#container.view_map #mapWrapper {z-index: 10;}
#container.view_map #btnMap {display: none;}
#container.view_roadview #mapWrapper {z-index: 0;}
#container.view_roadview #btnRoadview {display: none;}
</style>

