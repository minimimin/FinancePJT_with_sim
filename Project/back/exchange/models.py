from django.db import models

# Create your models here.
class ExchangeRate(models.Model):
    # result = models.IntegerField()
    # 결과값(1 : 성공, 2 : DATA코드 오류, 3 : 인증코드 오류, 4 : 일일제한횟수 마감)
    # 실패시 에러인건지 일일제한횟수 마감인지 확인하기 위해 받아오기(나중에 삭제 예정)
    # 일일제한횟수가 한정적이라서,,,
    cur_unit = models.TextField()
    # 통화코드
    cur_nm = models.TextField()
    # 국가/통화명
    ttb = models.TextField()
    # 전신환(송금) 받으실때
    tts = models.TextField()
    # 전신환(송금) 보내실때
    deal_bas_r = models.TextField()
    # 매매 기준율
