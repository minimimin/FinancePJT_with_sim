from django.shortcuts import render
from django.conf import settings
import requests

# Create your views here.
def address_list(request):

    KAKAO_API_KEY = 'a32011f1808041a949ccede88e91bcca'
    KAKAO_API_URL = 'https://dapi.kakao.com/v2/local/geo/regions'

    headers = {
        'Authorization': f'KakaoAK {KAKAO_API_KEY}'
    }

    params = {
        'category_group_code': 'region',
        'page': 1,
        'size': 15  # 한 페이지에 표시할 결과 수
    }

    response = requests.get(KAKAO_API_URL, headers=headers, params=params)
    data = response.json()

    regions = data.get('documents', [])
    for region in regions:
        region_name = region.get('region_1depth_name')
        print(region_name)

