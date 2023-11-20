from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExchangeRateSerializer
import requests
from .models import ExchangeRate
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.
@api_view(['GET'])
def exchangeRate(request):
    api_key = settings.EXCHANGE_RATE_API_KEY
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&data=AP01'
    exchange_data=ExchangeRate.objects.all()
    exchange_data.delete()
    response = requests.get(url).json()

    for ctr in response:
        data = {
            # 'result' : ctr['result'],
            'cur_unit' : ctr['cur_unit'],
            'cur_nm' : ctr['cur_nm'],
            'ttb' : ctr['ttb'],
            'tts' : ctr['tts'],
            'deal_bas_r' : ctr['deal_bas_r'],
        }

        serializer = ExchangeRateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    exchangeRates = get_list_or_404(ExchangeRate)
    serializer = ExchangeRateSerializer(exchangeRates, many=True)

    return Response(serializer.data)