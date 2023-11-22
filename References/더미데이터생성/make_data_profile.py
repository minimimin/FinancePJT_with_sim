# make_data.py 파일은 랜덤한 더미 데이터를 만드는 예시 파일입니다.
# 반드시, 사용하는 필드를 확인한 후 본인의 프로젝트에 맞게 수정하여 진행해야 합니다.

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
#     deposit_products = models.ManyToManyField(DepositProduct)
#     saving_products = models.ManyToManyField(SavingProduct)
#     loan_home_products = models.ManyToManyField(LoanForHome)
#     loan_person_products = models.ManyToManyField(LoanForPerson)
    
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


import random
import requests

job_list = ['학생 및 주부', '사업가 및 프리랜서', '회사원', '기타']
bank_list = ['우리은행', '한국스탠다드차타드은행', '대구은행', '부산은행', '광주은행', '제주은행', '전북은행', '경남은행', '중소기업은행', '한국산업은행', '국민은행', '신한은행', '농협은행주식회사', '하나은행', '주식회사 케이뱅크', '수협은행', '주식회사 카카오뱅크', '토스뱅크 주식회사']
banking_product_list = ['예금', '적금', '대출', '해당없음']
card_product_list = ['신용카드', '체크카드', '해당없음']

# json 파일 만들기
import json
from collections import OrderedDict

file = OrderedDict()

N=10000

# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = '../profile_data.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')
    
    for i in range(N):
        # 랜덤한 데이터를 삽입
        file["model"] = "accounts.Profile"
        file["pk"] = i+1
        file["fields"] = {
            'user': i+1,
            'deposit_products': [random.randint(1, 38) for _ in range(random.randint(0, 5))],
            'saving_products': [random.randint(1, 62) for _ in range(random.randint(0, 5))],
            'loan_home_products': [random.randint(1, 39) for _ in range(random.randint(0, 5))],
            'age': random.randint(1, 100),  # 나이
            'money': random.randrange(0, 100000000, 100000),    # 현재 가진 금액
            'salary': random.randrange(0, 1500000000, 1000000), # 연봉
            'job': random.choice(job_list),
            'main_bank': random.choice(bank_list),
            'stabillity': str(random.randint(0, 100)),
            'banking_products': random.choice(banking_product_list),
            'card_products': random.choice(card_product_list),
        }

        json.dump(file, f, ensure_ascii=False, indent="\t")
        if i != N-1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')