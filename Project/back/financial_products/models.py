from django.db import models

# Create your models here.
# 금융회사---------------------------------------------------------------------------------------------
class FinancialCompany(models.Model):
    fin_co_no = models.TextField()
    # 금융회사 코드
    # 이걸 PK로 잡는게 좋을 듯?!?!?
    # PK 잡지말고 나중에 필터 쓰는 걸로 하자
    kor_co_nm = models.TextField()
    # 금융회사 명
    homp_url = models.TextField(null=True)
    # 홈페이지 주소
    cal_tel = models.TextField(null=True)
    # 콜센터 전화번호


# 예금-----------------------------------------------------------------------------------------------------------------------------
class DepositProduct(models.Model):
    fin_co_no = models.TextField()
    # 금융회사 코드
    kor_co_nm = models.TextField()
    # 금융회사명
    fin_prdt_cd = models.TextField()
    # 금융상품 코드
    fin_prdt_nm = models.TextField()
    # 금융상품명
    join_way = models.TextField(null=True)
    # 가입 방법
    join_member = models.TextField(null=True) 
    # 가입 대상
    join_deny = models.IntegerField(null=True) 
    # 가입제한
    max_limit = models.TextField(null=True) 
    # 최고한도
    spcl_cnd = models.TextField(null=True)
    # 우대조건
    mtrt_int = models.TextField(null=True)
    # 만기 후 이자율
    etc_note = models.TextField(null=True) 
    # 기타 유의사항


class DepositProductOptions(models.Model):
    # deposit_company = models.ForeignKey(DepositProduct,on_delete=models.CASCADE related_name='deposit_product_option' to_field='fin_co_no')
    # 금융회사 코드
    deposit_product = models.ForeignKey(DepositProduct, on_delete=models.CASCADE, related_name='deposit_product_option', to_field='fin_prdt_cd')
    # 금융상품 코드

    fin_prdt_cd = models.TextField(null=True) 
    # 저축금리유형
    intr_rate_type_nm = models.CharField(null=True) 
    # 저축금리유형명
    intr_rate = models.FloatField(null=True) 
    # 저축금리
    intr_rate2 = models.FloatField(null=True) 
    # 최고우대금리
    save_trm = models.IntegerField(null=True)
    # 저축기간


# 적금------------------------------------------------------------------------------------------------------------------------------
class SavingProduct(models.Model):
    fin_co_no = models.TextField()
    # 금융회사 코드
    kor_co_nm = models.TextField()
    # 금융회사명
    fin_prdt_cd = models.TextField() 
    # 금융상품코드
    fin_prdt_nm = models.TextField() 
    # 금융상품명
    join_way = models.TextField(null=True) 
    # 가입 방법
    join_member = models.TextField(null=True) 
    # 가입 대상
    join_deny = models.IntegerField(null=True) 
    # 가입제한
    max_limit = models.TextField(null=True) 
    # 최고 한도
    spcl_cnd = models.TextField(null=True) 
    # 우대조건
    mtrt_int = models.TextField(null=True) 
    # 만기 후 이자율
    etc_note = models.TextField(null=True) 
    # 기타 유의사항


class SavingProductOptions(models.Model):
    # fin_co_no = models.ForeignKey(SavingProduct,on_delete=models.CASCADE)
    # 금융회사 코드
    saving_product = models.ForeignKey(SavingProduct, on_delete=models.CASCADE, related_name='saving_product_option', to_field='fin_prdt_cd')
    # 금융상품 코드
    
    # ForeignKey를 설정

    intr_rate_type = models.TextField(null=True) 
    # 저축금리유형
    intr_rate_type_nm = models.CharField(null=True) 
    # 저축금리유형명
    intr_rate = models.FloatField(null=True) 
    # 저축금리
    intr_rate2 = models.FloatField(null=True) 
    # 최고우대금리
    save_trm = models.IntegerField(null=True) 
    # 저축기간


# 전세자금대출-------------------------------------------------------------------------------------------------------------
class LoanForHome(models.Model):
    fin_co_no = models.TextField()
    # 금융회사 코드
    kor_co_nm = models.TextField()
    # 금융회사명
    fin_prdt_cd = models.TextField() 
    # 금융상품코드
    fin_prdt_nm = models.TextField() 
    # 금융상품명
    loan_lmt = models.TextField(null=True)
    # 대출한도
    loan_inci_expn = models.TextField(null=True)
    # 대출 부대비용
    erly_rpay_fee = models.TextField(null=True)
    # 중도상환 수수료
    dly_rate = models.TextField(null=True)
    # 연체 이자율

    # 여기는 optionList에서 가져오기!

    lend_rate_type = models.TextField(null=True)
    # 대출금리유형 코드
    lend_rate_type_nm = models.TextField(null=True)
    # 대출금리유형
    lend_rate_avg = models.TextField(null=True)
    # 전월 취급 평균금리 [소수점 2자리]
    lend_rate_min = models.TextField(null=True)
    # 대출금리_최저 [소수점 2자리]
    lend_rate_max = models.TextField(null=True)
    # 대출금리_최고 [소수점 2자리]


# 개인신용대출------------------------------------------------------------------------------------------------
class LoanForPerson(models.Model):
    fin_co_no = models.TextField()
    # 금융회사 코드
    kor_co_nm = models.TextField()
    # 금융회사명
    fin_prdt_cd = models.TextField() 
    # 금융상품코드
    fin_prdt_nm = models.TextField() 
    # 금융상품명
    join_way = models.TextField(null=True)
    # 가입 방법
    crdt_prdt_type = models.TextField(null=True)   
    # 대출종류 코드
    crdt_prdt_type_nm = models.TextField(null=True)
    # 대출종류명
    cb_name = models.TextField(null=True)
    # CB(개인신용평가) 회사명


class LoanForPersonOptions(models.Model):
    # fin_co_no = models.ForeignKey(LoanForPerson, on_delete=models.CASCADE)
    # 금융회사 코드
    loan_person_product = models.ForeignKey(LoanForPerson, on_delete=models.CASCADE, related_name='deposit_product_option', to_field='fin_prdt_cd')
    # 금융상품 코드

    # ForeignKey를 설정

    crdt_lend_rate_type = models.TextField(null=True)
    # 금리구분 코드
    crdt_lend_rate_type_nm = models.TextField(null=True)
    # 금리구분
    crdt_grad_avg = models.TextField(null=True)
    # 평균 금리 [소수점 2자리]
    crdt_grad_1 = models.TextField(null=True)
    # 900점 초과 [소수점 2자리]
    crdt_grad_4 = models.TextField(null=True)
    # 801~900점 [소수점 2자리]
    crdt_grad_5 = models.TextField(null=True)
    # 701~800점 [소수점 2자리]


# 가입상품리스트용------------------------------------------------------------------------------------------------
class ChooseProduct(models.Model):
    fin_co_no = models.TextField()
    # 금융회사 코드
    kor_co_nm = models.TextField()
    # 금융회사명
    fin_prdt_cd = models.TextField() 
    # 금융상품코드
    fin_prdt_nm = models.TextField() 
    # 금융상품명

    # 또 뭐를 받을 수 있을까?
    # 상세페이지로 연동될 수 있게 하는 거?..??
    # 상품유형(예금/적금/전세자금대출/개인대출)에 따라 적히는 게 나눠져야하니까
    # 일단 여기는 그냥 이만큼만 받을까..??