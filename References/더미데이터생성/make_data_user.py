# [참고] 현재 코드는 아래 User 모델을 기준으로 작성되어 있습니다.
# class User(AbstractBaseUser):
#     username = models.CharField(max_length=30, unique=True)
#     nickname = models.CharField(max_length=255, blank=True, null=True)
#     email = models.EmailField(max_length=254, blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)
#     money = models.IntegerField(blank=True, null=True)
#     salary = models.IntegerField(blank=True, null=True)
#     # 가입한 상품 목록 리스트를 ,로 구분된 문자열로 저장함
#     financial_products = models.TextField(blank=True, null=True)
    
#     # superuser fields
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

### 우리 모델
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

first_name_samples = "김이박최정강조윤장임한오서신권황안송전홍"
middle_name_samples = "민서예지도하주윤채현지시준우선유은소다가"
last_name_samples = "준윤우원호후서연아은진빈현민율영호정찬혁"
username_samples = "abcdefghijklmnopqrstuvwxyz0123456789"

# username(id) 10자리 랜덤 생성 - 중복이면 안됨
def random_username():
    result = ""
    result += random.choice(username_samples)
    result += random.choice(username_samples)
    result += random.choice(username_samples)
    result += random.choice(username_samples)
    result += random.choice(username_samples)
    result += random.choice(username_samples)
    result += random.choice(username_samples)
    result += random.choice(username_samples)
    return result

username_list = []
N = 10000
i = 0

while i < N:
    rn = random_username()
    if rn in username_list:
        continue
    
    username_list.append(rn)
    i += 1


# 성 제외 이름 2자리 생성
def random_name():
    result = ""
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result

name_list = []
N = 10000
i = 0

while i < N:
    rn = random_name()
    
    name_list.append(rn)
    i += 1


# json 파일 만들기
import json
from collections import OrderedDict

file = OrderedDict()

save_dir = '../user_data.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')
    
    for i in range(N):
        # 랜덤한 데이터를 삽입
        file["model"] = "accounts.User"
        file["pk"] = i+1
        file["fields"] = {
            'username': username_list[i],  # 유저 이름 랜덤 생성
            'first_name': name_list[i], # 이름 랜덤 생성
            'last_name': random.choice(first_name_samples), # 성 랜덤 생성
            'email': username_list[i] + '@ssafy.com',
            'password': "1234",
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

