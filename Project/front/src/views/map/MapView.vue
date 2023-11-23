<template>
  <div>
    <h1>내 주변의 은행 찾기</h1>
    <hr>
    <MapItem />
  </div>
</template>

<script setup>
// import { ref, computed, watch, onMounted } from 'vue'
// import { useUserStore } from '@/stores/user'
import MapItem from '@/components/map/MapItem.vue'
// import axios from 'axios'

// const userStore = useUserStore()

// // 선택지
// const sidoList = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', 
//   '세종특별자치시', '경기도', '강원도', '경상북도', '경상남도', '전라북도', '전라남도', '충청북도', '충청남도', '제주특별자치도']
// const regions = ref([])
// const filteredGungu = computed(() => {
//   return regions.value.filter(region => region.sido === selectedSido.value)
// })
// const banks = ['경남은행', '광주은행', '국민은행', '기업은행', '농협', '대구은행', '부산은행', '신한은행', 
//     '외환은행', '우리은행', '제주은행', '전북은행', '하나은행', '한국시티은행', 'SC제일은행']
// const selectedSido = ref('')
// const selectedGungu = ref('')
// const selectedBank = ref('')
// const inputKeyword = ref('')
// const totalKeyword = ref('')

// const updateKeyword = () => {
//     totalKeyword.value = selectedSido.value + ' ' + selectedGungu.value + ' ' 
//     + selectedBank.value + ' ' + inputKeyword.value
// }

// // 선택이 바뀔 때마다 updateKeyword 함수를 호출
// watch([selectedSido, selectedGungu, selectedBank, inputKeyword], () => {
//   updateKeyword()
// })

// // const searchForm = document.getElementById("submit_btn");
// // 		searchForm?.addEventListener("click", function (e) {
// // 		e.preventDefault();
// // 		searchKeywordPlaces();
// // });

// // 경도, 위도 초기값 (구미 캠퍼스)
// // const latitude = ref(36.107793)
// // const longitude = ref(128.416801)

// // 경도, 위도 초기값 (삼성전자 본사)
// // const latitude = ref(37.257836)
// // const longitude = ref(127.053511)

// // 경도, 위도 초기값 (멀티캠퍼스 역삼)
// const latitude = ref(37.501280)
// const longitude = ref(127.039536)

// const createMap = function () {
//   // Kakao Map API를 사용하여 현재 위치를 기반으로 지도 생성
//   const mapContainer = document.getElementById('map')
//   const options = {
//     center: new kakao.maps.LatLng(latitude.value, longitude.value),
//     level: 2,
//   }
//   const map = new kakao.maps.Map(mapContainer, options)

  
//   ///// 여기부터 지도 커스텀 /////
//   // 일반 지도와 스카이뷰로 지도 타입을 전환할 수 있는 지도타입 컨트롤을 생성합니다
//   var mapTypeControl = new kakao.maps.MapTypeControl();
  
//   // 지도 타입 컨트롤을 지도에 표시합니다
//   map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);
  
//   // 지도 확대 축소를 제어할 수 있는  줌 컨트롤을 생성합니다
//   var zoomControl = new kakao.maps.ZoomControl();
//   map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);
  
//   // 마커를 클릭했을 때 해당 장소의 상세정보를 보여줄 커스텀오버레이입니다
// var placeOverlay = new kakao.maps.CustomOverlay({zIndex:1});
// var contentNode = document.createElement('div'); // 커스텀 오버레이의 컨텐츠 엘리먼트 입니다 
// var markers = []; // 마커를 담을 배열입니다
// var currCategory = 'BK9'; // 현재 선택된 카테고리를 가지고 있을 변수입니다

//   // 장소 검색 객체를 생성합니다
// var ps = new kakao.maps.services.Places(map); 

// // 지도에 idle 이벤트를 등록합니다
// kakao.maps.event.addListener(map, 'idle', searchPlaces);

// // 커스텀 오버레이의 컨텐츠 노드에 css class를 추가합니다 
// contentNode.className = 'placeinfo_wrap';

// // 커스텀 오버레이의 컨텐츠 노드에 mousedown, touchstart 이벤트가 발생했을때
// // 지도 객체에 이벤트가 전달되지 않도록 이벤트 핸들러로 kakao.maps.event.preventMap 메소드를 등록합니다 
// addEventHandle(contentNode, 'mousedown', kakao.maps.event.preventMap);
// addEventHandle(contentNode, 'touchstart', kakao.maps.event.preventMap);

// // 커스텀 오버레이 컨텐츠를 설정합니다
// placeOverlay.setContent(contentNode);  

// // 각 카테고리에 클릭 이벤트를 등록합니다
// addCategoryClickEvent();

// // 엘리먼트에 이벤트 핸들러를 등록하는 함수입니다
// function addEventHandle(target, type, callback) {
//     if (target.addEventListener) {
//         target.addEventListener(type, callback);
//     } else {
//         target.attachEvent('on' + type, callback);
//     }
// }

// searchPlaces()

// // 카테고리 검색을 요청하는 함수입니다
// function searchPlaces() {
//     // console.log(totalKeyword.value)
//     if (!currCategory) {
//         return;
//     }
    
//     // 커스텀 오버레이를 숨깁니다 
//     // placeOverlay.setMap(null);

//     // 지도에 표시되고 있는 마커를 제거합니다
//     removeMarker();
    
//     ps.categorySearch(currCategory, placesSearchCB, {useMapBounds:true}); 
// }

// // 장소검색이 완료됐을 때 호출되는 콜백함수 입니다
// function placesSearchCB(data, status, pagination) {
//     if (status === kakao.maps.services.Status.OK) {

//         // 정상적으로 검색이 완료됐으면 지도에 마커를 표출합니다
//         displayPlaces(data);

//         // 페이지 번호를 표출합니다
//         displayPagination(pagination);

//     } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
//         // 검색결과가 없는경우 해야할 처리가 있다면 이곳에 작성해 주세요

//     } else if (status === kakao.maps.services.Status.ERROR) {
//         // 에러로 인해 검색결과가 나오지 않은 경우 해야할 처리가 있다면 이곳에 작성해 주세요
        
//     }
// }

// // 지도에 마커를 표출하는 함수입니다
// function displayPlaces(places) {
//     var listEl = document.getElementById('placesList');
//     var menuEl = document.getElementById('menu_wrap');
//     var fragment = document.createDocumentFragment();

//     // 검색 결과 목록에 추가된 항목들을 제거합니다
//     removeAllChildNods(listEl);

//     // 지도에 표시되고 있는 마커를 제거합니다
//     removeMarker();

//     // 몇번째 카테고리가 선택되어 있는지 얻어옵니다
//     // 이 순서는 스프라이트 이미지에서의 위치를 계산하는데 사용됩니다
//     var order = document.getElementById(currCategory).getAttribute('data-order');

//     for ( var i=0; i<places.length; i++ ) {

//             // 마커를 생성하고 지도에 표시합니다
//             var marker = addMarker(new kakao.maps.LatLng(places[i].y, places[i].x), order);
//             // marker = addMarker(placePosition, i);
//             var itemEl = getListItem(i, places[i]); // 검색 결과 항목 Element를 생성합니다;

//             // 마커와 검색결과 항목을 클릭 했을 때
//             // 장소정보를 표출하도록 클릭 이벤트를 등록합니다
//             // (function(marker, place) {
//             //     kakao.maps.event.addListener(marker, 'click', function() {
//             //         displayPlaceInfo(place);
//             //     });
//             // })(marker, places[i]);
//             // 마커와 검색결과 항목에 mouseover 했을때
//         // 해당 장소에 인포윈도우에 장소명을 표시합니다
//         // mouseout 했을 때는 인포윈도우를 닫습니다
//         (function(marker, place) {
//             kakao.maps.event.addListener(marker, 'click', function() {
//                     displayPlaceInfo(place);
//                 });

//             itemEl.onclick =  function () {
//                 displayPlaceInfo(place);
//             };

//         })(marker, places[i]);

//             fragment.appendChild(itemEl);
//     }
//     // 검색결과 항목들을 검색결과 목록 Element에 추가합니다
//     listEl.appendChild(fragment);
//     menuEl.scrollTop = 0;
// }

// // 검색결과 항목을 Element로 반환하는 함수입니다
// function getListItem(index, places) {

// var el = document.createElement('li'),
// itemStr = '<span class="markerbg marker_' + (index+1) + '"></span>' +
//             '<div class="info">' +
//             '   <h5>' + places.place_name + '</h5>';

// if (places.road_address_name) {
//     itemStr += '    <span>' + places.road_address_name + '</span>' +
//                 '   <span class="jibun gray">' +  places.address_name  + '</span>';
// } else {
//     itemStr += '    <span>' +  places.address_name  + '</span>'; 
// }
             
//   itemStr += '  <span class="tel">' + places.phone  + '</span>' +
//             '</div>';           

// el.innerHTML = itemStr;
// el.className = 'item';

// return el;
// }

// // 마커를 생성하고 지도 위에 마커를 표시하는 함수입니다
// function addMarker(position, order) {

//     var marker = new kakao.maps.Marker({
//             position: position, // 마커의 위치
//         });

//     marker.setMap(map); // 지도 위에 마커를 표출합니다
//     markers.push(marker);  // 배열에 생성된 마커를 추가합니다

//     return marker;
// }

// // 지도 위에 표시되고 있는 마커를 모두 제거합니다
// function removeMarker() {
//     for ( var i = 0; i < markers.length; i++ ) {
//         markers[i].setMap(null);
//     }   
//     markers = [];
// }

// // 검색결과 목록 하단에 페이지번호를 표시는 함수입니다
// function displayPagination(pagination) {
//     var paginationEl = document.getElementById('pagination'),
//         fragment = document.createDocumentFragment(),
//         i; 

//     // 기존에 추가된 페이지번호를 삭제합니다
//     while (paginationEl.hasChildNodes()) {
//         paginationEl.removeChild (paginationEl.lastChild);
//     }

//     for (i=1; i<=pagination.last; i++) {
//         var el = document.createElement('a');
//         el.href = "#";
//         el.innerHTML = i;

//         if (i===pagination.current) {
//             el.className = 'on';
//         } else {
//             el.onclick = (function(i) {
//                 return function() {
//                     pagination.gotoPage(i);
//                 }
//             })(i);
//         }

//         fragment.appendChild(el);
//     }
//     paginationEl.appendChild(fragment);
// }

// // 클릭한 마커에 대한 장소 상세정보를 커스텀 오버레이로 표시하는 함수입니다
// function displayPlaceInfo (place) {
//     var content = '<div class="placeinfo">' +
//                     '   <a class="title" href="' + place.place_url + '" target="_blank" title="' + place.place_name + '">' + place.place_name + '</a>';   

//     if (place.road_address_name) {
//         content += '    <span title="' + place.road_address_name + '">' + place.road_address_name + '</span>' +
//                     '  <span class="jibun" title="' + place.address_name + '">(지번 : ' + place.address_name + ')</span>';
//     }  else {
//         content += '    <span title="' + place.address_name + '">' + place.address_name + '</span>';
//     }                
   
//     content += '    <span class="tel">' + place.phone + '</span>' + 
//                 '</div>' + 
//                 '<div class="after"></div>';

//     contentNode.innerHTML = content;
//     placeOverlay.setPosition(new kakao.maps.LatLng(place.y, place.x));
//     placeOverlay.setMap(map);  
// }

// // 검색결과 목록의 자식 Element를 제거하는 함수입니다
// function removeAllChildNods(el) {   
//     while (el.hasChildNodes()) {
//         el.removeChild (el.lastChild);
//     }
// }

// // 각 카테고리에 클릭 이벤트를 등록합니다
// function addCategoryClickEvent() {
//     var category = document.getElementById('category'),
//         children = category.children;

//     for (var i=0; i<children.length; i++) {
//         children[i].onclick = onClickCategory;
//     }
// }

// // 카테고리를 클릭했을 때 호출되는 함수입니다
// function onClickCategory() {
//     var id = this.id,
//         className = this.className;

//     placeOverlay.setMap(null);

//     if (className === 'on') {
//         currCategory = '';
//         changeCategoryClass();
//         removeMarker();
//     } else {
//         currCategory = id;
//         changeCategoryClass(this);
//         searchPlaces();
//     }
// }

// // 클릭된 카테고리에만 클릭된 스타일을 적용하는 함수입니다
// function changeCategoryClass(el) {
//     var category = document.getElementById('category'),
//         children = category.children,
//         i;

//     for ( i=0; i<children.length; i++ ) {
//         children[i].className = '';
//     }

//     if (el) {
//         el.className = 'on';
//     } 
// } 

// // 키워드 검색
// // 마커를 담을 배열입니다
// var markers2 = [];
// // 장소 검색 객체를 생성합니다
// var ps2 = new kakao.maps.services.Places();
// // 키워드 검색을 요청하는 함수입니다
// function searchKeywordPlaces() {
//     console.log('성공?')
// var keyword = document.getElementById('keyword').value;

// if (!keyword.replace(/^\s+|\s+$/g, '')) {
//     alert('키워드를 입력해주세요!');
//     return false;
// }

// // 장소검색 객체를 통해 키워드로 장소검색을 요청합니다
// ps2.keywordSearch(keyword, placesKeywordSearchCB); 
// }
// // 장소검색이 완료됐을 때 호출되는 콜백함수 입니다
// function placesKeywordSearchCB(data, status, pagination) {
//     if (status === kakao.maps.services.Status.OK) {

//         // 정상적으로 검색이 완료됐으면
//         // 검색 목록과 마커를 표출합니다
//         displayKeywordPlaces(data);

//         // 페이지 번호를 표출합니다
//         displayKeywordPagination(pagination);

//     } else if (status === kakao.maps.services.Status.ZERO_RESULT) {

//         alert('검색 결과가 존재하지 않습니다.');
//         return;

//     } else if (status === kakao.maps.services.Status.ERROR) {

//         alert('검색 결과 중 오류가 발생했습니다.');
//         return;

//     }
// }
// // 검색 결과 목록과 마커를 표출하는 함수입니다
// function displayKeywordPlaces(places) {

// var listEl2 = document.getElementById('placesList');
// var menuEl2 = document.getElementById('menu_wrap');
// var fragment2 = document.createDocumentFragment();
// var bounds = new kakao.maps.LatLngBounds();

// // 검색 결과 목록에 추가된 항목들을 제거합니다
// removeAllChildNods(listEl2);

// // 지도에 표시되고 있는 마커를 제거합니다
// removeMarker();

// for ( var i=0; i<places.length; i++ ) {

//     // 마커를 생성하고 지도에 표시합니다
//     var placePosition = new kakao.maps.LatLng(places[i].y, places[i].x);
//     var marker2 = addKeywordMarker(placePosition, i);
//     var itemEl2 = getKeywordListItem(i, places[i]); // 검색 결과 항목 Element를 생성합니다

//     // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
//     // LatLngBounds 객체에 좌표를 추가합니다
//     bounds.extend(placePosition);

//     // 마커와 검색결과 항목에 mouseover 했을때
//     // 해당 장소에 인포윈도우에 장소명을 표시합니다
//     // mouseout 했을 때는 인포윈도우를 닫습니다
//     // (function(marker, title) {
//     //     kakao.maps.event.addListener(marker, 'mouseover', function() {
//     //         displayInfowindow(marker, title);
//     //     });

//     //     kakao.maps.event.addListener(marker, 'mouseout', function() {
//     //         infowindow.close();
//     //     });

//     //     itemEl.onmouseover =  function () {
//     //         displayInfowindow(marker, title);
//     //     };

//     //     itemEl.onmouseout =  function () {
//     //         infowindow.close();
//     //     };
//     // })(marker, places[i].place_name);

//     fragment2.appendChild(itemEl2);
// }

// // 검색결과 항목들을 검색결과 목록 Element에 추가합니다
// listEl2.appendChild(fragment2);
// menuEl2.scrollTop = 0;

// // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
// map.setBounds(bounds);
// }

// // 검색결과 항목을 Element로 반환하는 함수입니다
// function getKeywordListItem(index, places) {

// var el = document.createElement('li');
// var itemStr = '<span class="markerbg marker_' + (index+1) + '"></span>' +
//             '<div class="info">' +
//             '   <h5>' + places.place_name + '</h5>';

// if (places.road_address_name) {
//     itemStr += '    <span>' + places.road_address_name + '</span>' +
//                 '   <span class="jibun gray">' +  places.address_name  + '</span>';
// } else {
//     itemStr += '    <span>' +  places.address_name  + '</span>'; 
// }

// itemStr += '  <span class="tel">' + places.phone  + '</span>' +
//             '</div>';           

// el.innerHTML = itemStr;
// el.className = 'item';

// return el;
// }

// // 마커를 생성하고 지도 위에 마커를 표시하는 함수입니다
// function addKeywordMarker(position, idx, title) {
//     var imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png'; // 마커 이미지 url, 스프라이트 이미지를 씁니다
//     var  imageSize = new kakao.maps.Size(36, 37);  // 마커 이미지의 크기
//     var  imgOptions =  {
//             spriteSize : new kakao.maps.Size(36, 691), // 스프라이트 이미지의 크기
//             spriteOrigin : new kakao.maps.Point(0, (idx*46)+10), // 스프라이트 이미지 중 사용할 영역의 좌상단 좌표
//             offset: new kakao.maps.Point(13, 37) // 마커 좌표에 일치시킬 이미지 내에서의 좌표
//         },
//         markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions),
//             marker = new kakao.maps.Marker({
//             position: position, // 마커의 위치
//             image: markerImage 
//         });

//     marker.setMap(map); // 지도 위에 마커를 표출합니다
//     markers.push(marker);  // 배열에 생성된 마커를 추가합니다

//     return marker;
// }
// }

// function successCallback (position) {
//   latitude.value = position.coords.latitude
//   longitude.value = position.coords.longitude
//   createMap()
// }

// function errorCallback(error) {
//   createMap()
// }

// onMounted(() => {
//   // 시도군구 정보 가져오기
//   axios({
//     method: 'get',
//     url: `${userStore.API_URL}/maps/address/`,
//   })
//     .then((res) => {
//       regions.value = res.data
//     })
//     .catch((err) => {
//       console.log(err)
//     })

//   // 현재 위치 가져오기
//   navigator.geolocation.getCurrentPosition(successCallback, errorCallback)
// })

</script>

<!-- <style>
.map_wrap, .map_wrap * {padding:0;font-family:'Malgun Gothic',dotum,'돋움',sans-serif;font-size:12px;}
.map_wrap a, .map_wrap a:hover, .map_wrap a:active{color:#000;text-decoration: none;}
.map_wrap {position:relative;width:100%;height: 800px;}

#menu_wrap {position:absolute;top:0;left:0;bottom:0;width:250px;height:100%;padding:5px;overflow-y:auto;background:rgba(255, 255, 255, 0.9);z-index: 1;font-size:12px;border-radius: 0 10px 0 10px;}
.bg_white {background:#fff;}
#menu_wrap hr {display: block; height: 1px;border: 0; border-top: 2px solid #5F5F5F;margin:3px 0;}
#menu_wrap .option{text-align: center;}
#menu_wrap .option p {margin:10px 0;}  
#menu_wrap .option button {margin-left:5px;}

#category {position:absolute;top:45px;right:50px;border-radius: 5px; border:1px solid #909090;box-shadow: 0 1px 1px rgba(0, 0, 0, 0.4);background: #fff;overflow: hidden;z-index: 2;}
#category li {float:left;list-style: none;width:50px;border-right:1px solid #acacac;padding:6px 0;text-align: center; cursor: pointer;}
#category li.on {background: #eee;}
#category li:hover {background: #e6f4ff;border-left:1px solid #acacac;margin-left: -1px;}
#category li:last-child{margin-right:0;border-right:0;}
#category li span {display: block;margin:0 auto 3px;width:27px;height: 28px;}
#category li .category_bg {background:url(@/assets/marker_spot.png) no-repeat;background-size: contain;background-position: center center;}
/* #category li .bank {background-position: -10px 0;} */
#category li.on .category_bg {background-position-x:-46px;}

.placeinfo_wrap {position:absolute;bottom:28px;left:-150px;width:300px;}
.placeinfo {position:relative;width:100%;border-radius:6px;border: 1px solid #ccc;border-bottom:2px solid #ddd;padding-bottom: 10px;background: #fff;}
.placeinfo:nth-of-type(n) {border:0; box-shadow:0px 1px 2px #888;}
.placeinfo_wrap .after {content:'';position:relative;margin-left:-12px;left:50%;width:22px;height:12px;background:url('https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/vertex_white.png')}
.placeinfo a, .placeinfo a:hover, .placeinfo a:active{color:#fff;text-decoration: none;}
.placeinfo a, .placeinfo span {display: block;text-overflow: ellipsis;overflow: hidden;white-space: nowrap;}
.placeinfo span {margin:5px 5px 0 5px;cursor: default;font-size:13px;}
.placeinfo .title {font-weight: bold; font-size:14px;border-radius: 6px 6px 0 0;margin: -1px -1px 0 -1px;padding:10px; color: #fff;background: #5087d9;background: #5087d9 url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/arrow_white.png) no-repeat right 14px center;}
.placeinfo .tel {color:#0f7833;}
.placeinfo .jibun {color:#999;font-size:11px;margin-top:0;}

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

<style scoped>
/* 여기는 내가 설정 */
.select-box {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 50px;
}

label {
    margin-right: 10px;
    align-items: center;
}
</style> -->