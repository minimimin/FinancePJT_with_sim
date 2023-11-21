from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import FinancialCompany, DepositProduct, DepositProductOptions, SavingProduct, SavingProductOptions, LoanForHome, LoanForPerson, LoanForPersonOptions, ChooseProduct
from .serializers import FinancialCompanySerializer, DepositProductSerializer, DepositProductOptionsSerializer, DepositProductWithOptionsSerializer, SavingProductSerializer, SavingProductOptionsSerializer, SavingProductWithOptionsSerializer, LoanForHomeSerializer, LoanForPersonSerializer, LoanForPersonOptionsSerializer, LoanForPersonWithOptionsSerializer, ChooseProductSerializer

# Create your views here.

# 금융회사정보 (DB 저장하는 것 + 저장된 파일을 보내는 것 함수 2개로 짜기)-----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
def financialCompanySave(request):
    api_key = settings.FINLIFE_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/companySearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    financial_company_data=FinancialCompany.objects.all()
    financial_company_data.delete()
    response = requests.get(url).json()

    for fincom in response['result']['baseList']:
        data = {
            'fin_co_no' : fincom['fin_co_no'],
            'kor_co_nm' : fincom['kor_co_nm'],
            'homp_url' : fincom['homp_url'],
            'cal_tel' : fincom['cal_tel'],
        }

        serializer = FinancialCompanySerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse('I Saved')

    # 여기까지가 저장하는 것! 근데 return으로 화면에 띄우는 건 없애자 나중에

@api_view(['GET'])
def financialCompanyGive(request):
    financial_company_data_all = get_list_or_404(FinancialCompany)
    serializer = FinancialCompanySerializer(financial_company_data_all, many=True)
    return Response(serializer.data)

    # 이게 전달해주는 거



# 예금정보 DB 저장하는 것(직렬화 된 것 고려하기)-----------------------------------------------------------------------------------------------------------------------


# 적금정보 DB 저장하는 것(직렬화 된 것 고려하기)-----------------------------------------------------------------------------------------------------------------------


# 전세자금대출정보 DB 저장하는 것-----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
def loanForHomeSave(request):
    api_key = settings.FINLIFE_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json?auth={api_key}&topFinGrpNo=050000&pageNo=1'
    loan_for_home_data=LoanForHome.objects.all()
    loan_for_home_data.delete()
    response = requests.get(url).json()

    for fincom in response['result']['baseList']:
        data = {
            'fin_co_no' : fincom['fin_co_no'],
            'kor_co_nm' : fincom['kor_co_nm'],
            'fin_prdt_cd' : fincom['fin_prdt_cd'],
            'fin_prdt_nm' : fincom['fin_prdt_nm'],
            'loan_lmt' : fincom['loan_lmt'],
            'loan_inci_expn' : fincom['loan_inci_expn'],
            'erly_rpay_fee' : fincom['erly_rpay_fee'],
            'dly_rate' : fincom['dly_rate'],
            # 여기는 옵션에서 가지고 오기
            'lend_rate_type' : fincom['lend_rate_type'],
            'lend_rate_type_nm' : fincom['lend_rate_type_nm'],
            'lend_rate_avg' : fincom['lend_rate_avg'],
            'lend_rate_min' : fincom['lend_rate_min'],
            'lend_rate_max' : fincom['lend_rate_max'],
        }

        serializer = LoanForHomeSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse('I Saved')

    # 여기까지가 저장하는 것! 근데 return으로 화면에 띄우는 건 없애자 나중에


def loanForHomeGive(request):
    loan_for_home_data_all = get_list_or_404(LoanForHome)
    serializer = LoanForHomeSerializer(loan_for_home_data_all, many=True)
    return Response(serializer.data)

    # 이게 전달해주는 거



# 개인대출정보 DB 저장하는 것(직렬화 된 것 고려하기)-----------------------------------------------------------------------------------------------------------------------


# 가입한 상품 정보 DB 저장하는 것-----------------------------------------------------------------------------------------------------------------------