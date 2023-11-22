from django.db import models

# Create your models here.
# 금융회사---------------------------------------------------------------------------------------------
class FinancialCompany(models.Model):
    fin_co_no = models.TextField(unique=True)
    # 금융회사 코드
    # 이걸 PK로 잡는게 좋을 듯?!?!?
    # PK 잡지말고 나중에 필터 쓰는 걸로 하자
    kor_co_nm = models.TextField()
    # 금융회사 명
    homp_url = models.TextField(blank=True, null=True)
    # 홈페이지 주소
    cal_tel = models.TextField(blank=True, null=True)
    # 콜센터 전화번호


# 예금-----------------------------------------------------------------------------------------------------------------------------
class DepositProduct(models.Model):
    fin_co_no = models.TextField()
    # 금융회사 코드
    kor_co_nm = models.TextField()
    # 금융회사명
    fin_prdt_cd = models.TextField(unique=True)
    # 금융상품 코드
    fin_prdt_nm = models.TextField()
    # 금융상품명
    join_way = models.TextField(blank=True, null=True)
    # 가입 방법
    join_member = models.TextField(blank=True, null=True) 
    # 가입 대상
    join_deny = models.IntegerField(blank=True, null=True) 
    # 가입제한
    max_limit = models.TextField(blank=True, null=True) 
    # 최고한도
    spcl_cnd = models.TextField(blank=True, null=True)
    # 우대조건
    mtrt_int = models.TextField(blank=True, null=True)
    # 만기 후 이자율
    etc_note = models.TextField(blank=True, null=True) 
    # 기타 유의사항


class DepositProductOptions(models.Model):
    # deposit_company = models.ForeignKey(DepositProduct,on_delete=models.CASCADE related_name='deposit_product_option' to_field='fin_co_no')
    # 금융회사 코드
    deposit_product = models.ForeignKey(DepositProduct, on_delete=models.CASCADE, related_name='deposit_product_option', to_field='fin_prdt_cd')
    # 금융상품 코드

    intr_rate_type = models.TextField(blank=True, null=True) 
    # 저축금리유형    
    intr_rate_type_nm = models.TextField(blank=True, null=True) 
    # 저축금리유형명
    intr_rate = models.FloatField(blank=True, null=True) 
    # 저축금리
    intr_rate2 = models.FloatField(blank=True, null=True) 
    # 최고우대금리
    save_trm = models.IntegerField(blank=True, null=True)
    # 저축기간


# 적금------------------------------------------------------------------------------------------------------------------------------
class SavingProduct(models.Model):
    fin_co_no = models.TextField()
    # 금융회사 코드
    kor_co_nm = models.TextField()
    # 금융회사명
    fin_prdt_cd = models.TextField(unique=True) 
    # 금융상품코드
    fin_prdt_nm = models.TextField() 
    # 금융상품명
    join_way = models.TextField(blank=True, null=True) 
    # 가입 방법
    join_member = models.TextField(blank=True, null=True) 
    # 가입 대상
    join_deny = models.IntegerField(blank=True, null=True) 
    # 가입제한
    max_limit = models.TextField(blank=True, null=True) 
    # 최고 한도
    spcl_cnd = models.TextField(blank=True, null=True) 
    # 우대조건
    mtrt_int = models.TextField(blank=True, null=True) 
    # 만기 후 이자율
    etc_note = models.TextField(blank=True, null=True) 
    # 기타 유의사항


class SavingProductOptions(models.Model):
    # fin_co_no = models.ForeignKey(SavingProduct,on_delete=models.CASCADE)
    # 금융회사 코드
    saving_product = models.ForeignKey(SavingProduct, on_delete=models.CASCADE, related_name='saving_product_option', to_field='fin_prdt_cd')
    # 금융상품 코드

    intr_rate_type = models.TextField(blank=True, null=True) 
    # 저축금리유형
    intr_rate_type_nm = models.TextField(blank=True, null=True) 
    # 저축금리유형명
    intr_rate = models.FloatField(blank=True, null=True) 
    # 저축금리
    intr_rate2 = models.FloatField(blank=True, null=True) 
    # 최고우대금리
    save_trm = models.IntegerField(blank=True, null=True) 
    # 저축기간


# 전세자금대출-------------------------------------------------------------------------------------------------------------
class LoanForHome(models.Model):
    fin_co_no = models.TextField()
    # 금융회사 코드
    kor_co_nm = models.TextField()
    # 금융회사명
    fin_prdt_cd = models.TextField(unique=True) 
    # 금융상품코드
    fin_prdt_nm = models.TextField() 
    # 금융상품명
    loan_lmt = models.TextField(blank=True, null=True)
    # 대출한도
    loan_inci_expn = models.TextField(blank=True, null=True)
    # 대출 부대비용
    erly_rpay_fee = models.TextField(blank=True, null=True)
    # 중도상환 수수료
    dly_rate = models.TextField(blank=True, null=True)
    # 연체 이자율


class LoanForHomeOptions(models.Model):
    loan_home_product = models.ForeignKey(LoanForHome, on_delete=models.CASCADE, related_name='loan_home_product_option', to_field='fin_prdt_cd')
    # 금융상품 코드

    lend_rate_type = models.TextField(blank=True, null=True)
    # 대출금리유형 코드
    lend_rate_type_nm = models.TextField(blank=True, null=True)
    # 대출금리유형
    lend_rate_avg = models.TextField(blank=True, null=True)
    # 전월 취급 평균금리 [소수점 2자리]
    lend_rate_min = models.TextField(blank=True, null=True)
    # 대출금리_최저 [소수점 2자리]
    lend_rate_max = models.TextField(blank=True, null=True)
    # 대출금리_최고 [소수점 2자리]

