
# class User(AbstractUser):
    # username
    # first_name
    # last_name
    # email
    # password
    # date_joined
    # last_login
    # is_superuser
    # is_staff
    # is_active


# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     choice = models.ForeignKey(ChooseProduct, on_delete=models.CASCADE)
    
#     # 원하는 추가 필드 작성
#     age = models.IntegerField(null=True)
#     money = models.IntegerField(null=True)
#     salary = models.IntegerField(null=True)
#     job = models.CharField(max_length=30, null=True)
#     main_bank = models.TextField(null=True)

#     # 유저 성향 관련 필드
#     stabillity = models.TextField(null=True)
#     banking_products = models.TextField(null=True)
#     card_products = models.TextField(null=True)

# 가입상품리스트용------------------------------------------------------------------------------------------------
# class ChooseProduct(models.Model):
#     fin_co_no = models.TextField()
#     # 금융회사 코드
#     kor_co_nm = models.TextField()
#     # 금융회사명
#     fin_prdt_cd = models.TextField() 
#     # 금융상품코드
#     fin_prdt_nm = models.TextField() 
#     # 금융상품명


import random
import requests

first_name_samples = "김이박최정강조윤장임"
middle_name_samples = "민서예지도하주윤채현지"
last_name_samples = "준윤우원호후서연아은진"


def random_name():
    result = ""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result + str(random.randint(1, 100))

# 현재 API 에 들어있는 금융 상품 코드 리스트 저장
DP_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
SP_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

API_KEY = '<API_KEY>'

financial_products = []

params = {
  'auth': API_KEY,
  # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
  'topFinGrpNo': '020000',
  'pageNo': 1
}

# 정기예금 목록 저장
response = requests.get(DP_URL, params=params).json()
baseList = response.get('result').get('baseList')   # 상품 목록

for product in baseList:
    financial_products.append(product['fin_prdt_cd'])

# 적금 목록 저장
response = requests.get(SP_URL, params=params).json()
baseList = response.get('result').get('baseList')   # 상품 목록

for product in baseList:
    financial_products.append(product['fin_prdt_cd'])

dict_keys = ['username', 'gender', 'financial_products', 'age', 'money', 'salary']

# json 파일 만들기
import json
from collections import OrderedDict

file = OrderedDict()

username_list = []
N = 10000
i = 0

while i < N:
    rn = random_name()
    if rn in username_list:
        continue
    
    username_list.append(rn)
    i += 1

    
# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = '../backend/accounts/fixtures/accounts/user_data.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')
    
    for i in range(N):
        # 랜덤한 데이터를 삽입
        file["model"] = "accounts.User"
        file["pk"] = i+1
        file["fields"] = {
            'username': username_list[i],  # 유저 이름 랜덤 생성
            # 랜덤한 0~5개의 상품을 가입하도록 삽입됨
            'financial_products': ','.join([random.choice(financial_products) for _ in range(random.randint(0, 5))]), # 금융 상품 리스트
            'age': random.randint(1, 100),  # 나이
            'money': random.randrange(0, 100000000, 100000),    # 현재 가진 금액
            'salary': random.randrange(0, 1500000000, 1000000), # 연봉
            'password': "1234",
            'nickname': None,
            'is_active': True,
            'is_staff': False,
            'is_superuser': False
        }

        json.dump(file, f, ensure_ascii=False, indent="\t")
        if i != N-1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')