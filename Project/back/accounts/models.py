from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # 원하는 추가 필드 작성
    email = models.EmailField(max_length=254, null=True)
    age = models.IntegerField(null=True)
    money = models.IntegerField(null=True)
    salary = models.IntegerField(null=True)
    job = models.CharField(max_length=30, null=True)
    main_bank = models.TextField(null=True)

    # 성향 관련 변수
    stability = models.TextField(null=True)
    banking_products = models.TextField(null=True)
    card_products = models.TextField(null=True)