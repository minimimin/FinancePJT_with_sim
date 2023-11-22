from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from financial_products.models import DepositProduct, SavingProduct, LoanForHome

# Create your models here.
class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    deposit_products = models.ManyToManyField(DepositProduct, blank=True)
    saving_products = models.ManyToManyField(SavingProduct, blank=True)
    loan_home_products = models.ManyToManyField(LoanForHome, blank=True)
    
    # 원하는 추가 필드 작성
    age = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    job = models.CharField(max_length=30, blank=True, null=True)
    main_bank = models.TextField(blank=True, null=True)

    # 유저 성향 관련 필드
    stabillity = models.TextField(blank=True, null=True)
    banking_products = models.TextField(blank=True, null=True)
    card_products = models.TextField(blank=True, null=True)