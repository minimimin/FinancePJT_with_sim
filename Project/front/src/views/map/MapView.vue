<template>
  <div>
    <h1>지도 페이지</h1>
  
    <h4>선택지</h4>
    <div>
      <select v-model="selectedSido">
        <option v-for="sido in regions.sido" :key="sido.id" :value="sido">
          {{ sido }}
        </option>
      </select>
      <!-- <select v-model="selectedGungu">
        <option v-for="area in $data.adminAreas" :key="area.id" :value="area.id">
          {{ area.name }}
        </option>
      </select> -->
    </div>
  </div>
  
  <div class="map_wrap">
    <div id="menu_wrap" class="bg_white">
      <div class="option">
        <div>
          <form onsubmit="searchPlaces(); return false;">
              키워드 : <input type="text" value="" id="keyword" size="15"> 
              <button type="submit">검색하기</button> 
          </form>
        </div>
      </div>
      <hr>
      <ul id="placesList"></ul>
      <div id="pagination"></div>
    </div>

    <div id="container" class="view_map">
      <div id="mapWrapper" style="width:100%;height:100%;position:relative;">
          <div id="map" style="width:100%;height:100%"></div>
          <input type="button" id="btnRoadview" onclick="toggleMap(false)" title="로드뷰 보기" value="로드뷰">
      </div>
      <div id="rvWrapper" style="width:100%;height:100%;position:absolute;top:0;left:0;">
          <div id="roadview" style="height:100%"></div>
          <input type="button" id="btnMap" onclick="toggleMap(true)" title="지도 보기" value="지도">
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import axios from 'axios'

const userStore = useUserStore()
const regions = ref([])
const selectedSido = ref(null)
const selectedGungu = ref(null)

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

  // 마커를 클릭했을 때 해당 장소의 상세정보를 보여줄 커스텀오버레이입니다
  var placeOverlay = new kakao.maps.CustomOverlay({zIndex:1}), 
      contentNode = document.createElement('div'), // 커스텀 오버레이의 컨텐츠 엘리먼트 입니다 
      markers = [], // 마커를 담을 배열입니다
      currCategory = 'BK9'; // 현재 선택된 카테고리를 가지고 있을 변수입니다

  // 마커를 담을 배열입니다
  var markers = [];

  // 마커를 클릭하면 장소명을 표출할 인포윈도우 입니다
  var infowindow = new kakao.maps.InfoWindow({zIndex:1});

  // 장소 검색 객체를 생성합니다
  var ps = new kakao.maps.services.Places(map); 

  // 카테고리로 은행을 검색합니다
  ps.categorySearch('BK9', placesSearchCB, {useMapBounds:true});

  // 키워드로 장소를 검색합니다
  searchPlaces();

  // 키워드 검색을 요청하는 함수입니다
  function searchPlaces() {

  var keyword = document.getElementById('keyword').value;

  if (!keyword.replace(/^\s+|\s+$/g, '')) {
      alert('키워드를 입력해주세요!');
      return false;
  }

  // 장소검색 객체를 통해 키워드로 장소검색을 요청합니다
  ps.keywordSearch( keyword, placesSearchCB); 
  }

  // 키워드 검색 완료 시 호출되는 콜백함수 입니다
  function placesSearchCB (data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {

      // 정상적으로 검색이 완료됐으면
      // 검색 목록과 마커를 표출합니다
      displayPlaces(data);

      // 페이지 번호를 표출합니다
      displayPagination(pagination);

      } else if (status === kakao.maps.services.Status.ZERO_RESULT) {

      alert('검색 결과가 존재하지 않습니다.');
      return;

      } else if (status === kakao.maps.services.Status.ERROR) {

      alert('검색 결과 중 오류가 발생했습니다.');
      return;
      }
    // if (status === kakao.maps.services.Status.OK) {
      // for (var i=0; i<data.length; i++) {
      //   displayMarker(data[i]);    
      // }       
    // }
  }

  // 지도에 마커를 표시하는 함수입니다
  function displayMarker(place) {
    // 마커를 생성하고 지도에 표시합니다
    var marker = new kakao.maps.Marker({
      map: map,
      position: new kakao.maps.LatLng(place.y, place.x) 
    });

    // 마커에 클릭이벤트를 등록합니다
    kakao.maps.event.addListener(marker, 'click', function() {
      // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
      infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
      infowindow.open(map, marker);
    });
  }
  // 검색 결과 목록과 마커를 표출하는 함수입니다
  function displayPlaces(places) {

  var listEl = document.getElementById('placesList'), 
  menuEl = document.getElementById('menu_wrap'),
  fragment = document.createDocumentFragment(), 
  bounds = new kakao.maps.LatLngBounds(), 
  listStr = '';

  // 검색 결과 목록에 추가된 항목들을 제거합니다
  removeAllChildNods(listEl);

  // 지도에 표시되고 있는 마커를 제거합니다
  removeMarker();

  for ( var i=0; i<places.length; i++ ) {

      // 마커를 생성하고 지도에 표시합니다
      var placePosition = new kakao.maps.LatLng(places[i].y, places[i].x),
          marker = addMarker(placePosition, i), 
          itemEl = getListItem(i, places[i]); // 검색 결과 항목 Element를 생성합니다

      // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
      // LatLngBounds 객체에 좌표를 추가합니다
      bounds.extend(placePosition);

      // 마커와 검색결과 항목에 mouseover 했을때
      // 해당 장소에 인포윈도우에 장소명을 표시합니다
      // mouseout 했을 때는 인포윈도우를 닫습니다
      (function(marker, title) {
          kakao.maps.event.addListener(marker, 'mouseover', function() {
              displayInfowindow(marker, title);
          });

          kakao.maps.event.addListener(marker, 'mouseout', function() {
              infowindow.close();
          });

          itemEl.onmouseover =  function () {
              displayInfowindow(marker, title);
          };

          itemEl.onmouseout =  function () {
              infowindow.close();
          };
      })(marker, places[i].place_name);

      fragment.appendChild(itemEl);
  }

  // 검색결과 항목들을 검색결과 목록 Element에 추가합니다
  listEl.appendChild(fragment);
  menuEl.scrollTop = 0;

  // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
  map.setBounds(bounds);
  }

  // 검색결과 항목을 Element로 반환하는 함수입니다
  function getListItem(index, places) {

  var el = document.createElement('li'),
  itemStr = '<span class="markerbg marker_' + (index+1) + '"></span>' +
              '<div class="info">' +
              '   <h5>' + places.place_name + '</h5>';

  if (places.road_address_name) {
      itemStr += '    <span>' + places.road_address_name + '</span>' +
                  '   <span class="jibun gray">' +  places.address_name  + '</span>';
  } else {
      itemStr += '    <span>' +  places.address_name  + '</span>'; 
  }
              
    itemStr += '  <span class="tel">' + places.phone  + '</span>' +
              '</div>';           

  el.innerHTML = itemStr;
  el.className = 'item';

  return el;
  }

  // 마커를 생성하고 지도 위에 마커를 표시하는 함수입니다
  function addMarker(position, idx, title) {
  var imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png', // 마커 이미지 url, 스프라이트 이미지를 씁니다
      imageSize = new kakao.maps.Size(36, 37),  // 마커 이미지의 크기
      imgOptions =  {
          spriteSize : new kakao.maps.Size(36, 691), // 스프라이트 이미지의 크기
          spriteOrigin : new kakao.maps.Point(0, (idx*46)+10), // 스프라이트 이미지 중 사용할 영역의 좌상단 좌표
          offset: new kakao.maps.Point(13, 37) // 마커 좌표에 일치시킬 이미지 내에서의 좌표
      },
      markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions),
          marker = new kakao.maps.Marker({
          position: position, // 마커의 위치
          image: markerImage 
      });

  marker.setMap(map); // 지도 위에 마커를 표출합니다
  markers.push(marker);  // 배열에 생성된 마커를 추가합니다

  return marker;
  }

  // 지도 위에 표시되고 있는 마커를 모두 제거합니다
  function removeMarker() {
  for ( var i = 0; i < markers.length; i++ ) {
      markers[i].setMap(null);
  }   
  markers = [];
  }

  // 검색결과 목록 하단에 페이지번호를 표시는 함수입니다
  function displayPagination(pagination) {
  var paginationEl = document.getElementById('pagination'),
      fragment = document.createDocumentFragment(),
      i; 

  // 기존에 추가된 페이지번호를 삭제합니다
  while (paginationEl.hasChildNodes()) {
      paginationEl.removeChild (paginationEl.lastChild);
  }

  for (i=1; i<=pagination.last; i++) {
      var el = document.createElement('a');
      el.href = "#";
      el.innerHTML = i;

      if (i===pagination.current) {
          el.className = 'on';
      } else {
          el.onclick = (function(i) {
              return function() {
                  pagination.gotoPage(i);
              }
          })(i);
      }

      fragment.appendChild(el);
  }
  paginationEl.appendChild(fragment);
  }

  // 검색결과 목록 또는 마커를 클릭했을 때 호출되는 함수입니다
  // 인포윈도우에 장소명을 표시합니다
  function displayInfowindow(marker, title) {
  var content = '<div style="padding:5px;z-index:1;">' + title + '</div>';

  infowindow.setContent(content);
  infowindow.open(map, marker);
  }

  // 검색결과 목록의 자식 Element를 제거하는 함수입니다
  function removeAllChildNods(el) {   
  while (el.hasChildNodes()) {
      el.removeChild (el.lastChild);
  }
  }
  
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
  // 시도군구 정보 가져오기
  axios({
    method: 'get',
    url: `${userStore.API_URL}/maps/address/`,
  })
    .then((res) => {
      regions.value = res.data
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })

  // 현재 위치 가져오기
  navigator.geolocation.getCurrentPosition(successCallback, errorCallback)
})

</script>

<style scoped>
#container {overflow:hidden;width:80vw;height:80vh;position:relative;}
#btnRoadview,  #btnMap {position:absolute;top:5px;left:5px;padding:7px 12px;font-size:14px;border: 1px solid #dbdbdb;background-color: #fff;border-radius: 2px;box-shadow: 0 1px 1px rgba(0,0,0,.04);z-index:1;cursor:pointer;}
#btnRoadview:hover,  #btnMap:hover{background-color: #fcfcfc;border: 1px solid #c1c1c1;}
#container.view_map #mapWrapper {z-index: 10;}
#container.view_map #btnMap {display: none;}
#container.view_roadview #mapWrapper {z-index: 0;}
#container.view_roadview #btnRoadview {display: none;}
.map_wrap, .map_wrap * {margin:0;padding:0;font-size:12px;}
.map_wrap a, .map_wrap a:hover, .map_wrap a:active{color:#000;text-decoration: none;}
.map_wrap {position:relative;width:100%;height:500px;}
#menu_wrap {position:absolute;top:0;left:0;bottom:0;width:250px;margin:10px 0 30px 10px;padding:5px;overflow-y:auto;background:rgba(255, 255, 255, 0.7);z-index: 15;font-size:12px;border-radius: 10px;}
.bg_white {background:#fff;}
#menu_wrap hr {display: block; height: 1px;border: 0; border-top: 2px solid #5F5F5F;margin:3px 0;}
#menu_wrap .option{text-align: center;}
#menu_wrap .option p {margin:10px 0;}  
#menu_wrap .option button {margin-left:5px;}
#placesList li {list-style: none;}
#placesList .item {position:relative;border-bottom:1px solid #888;overflow: hidden;cursor: pointer;min-height: 65px;}
#placesList .item span {display: block;margin-top:4px;}
#placesList .item h5, #placesList .item .info {text-overflow: ellipsis;overflow: hidden;white-space: nowrap;}
#placesList .item .info{padding:10px 0 10px 55px;}
#placesList .info .gray {color:#8a8a8a;}
#placesList .info .jibun {padding-left:26px;background:url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/places_jibun.png) no-repeat;}
#placesList .info .tel {color:#009900;}
#placesList .item .markerbg {float:left;position:absolute;width:36px; height:37px;margin:10px 0 0 10px;background:url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png) no-repeat;}
#placesList .item .marker_1 {background-position: 0 -10px;}
#placesList .item .marker_2 {background-position: 0 -56px;}
#placesList .item .marker_3 {background-position: 0 -102px}
#placesList .item .marker_4 {background-position: 0 -148px;}
#placesList .item .marker_5 {background-position: 0 -194px;}
#placesList .item .marker_6 {background-position: 0 -240px;}
#placesList .item .marker_7 {background-position: 0 -286px;}
#placesList .item .marker_8 {background-position: 0 -332px;}
#placesList .item .marker_9 {background-position: 0 -378px;}
#placesList .item .marker_10 {background-position: 0 -423px;}
#placesList .item .marker_11 {background-position: 0 -470px;}
#placesList .item .marker_12 {background-position: 0 -516px;}
#placesList .item .marker_13 {background-position: 0 -562px;}
#placesList .item .marker_14 {background-position: 0 -608px;}
#placesList .item .marker_15 {background-position: 0 -654px;}
#pagination {margin:10px auto;text-align: center;}
#pagination a {display:inline-block;margin-right:10px;}
#pagination .on {font-weight: bold; cursor: default;color:#777;}
</style>