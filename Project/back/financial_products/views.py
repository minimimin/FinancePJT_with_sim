from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import FinancialCompany, DepositProduct, SavingProduct, LoanForHome
from .serializers import FinancialCompanySerializer, DepositProductSerializer, DepositProductOptionsSerializer, DepositProductWithOptionsSerializer, SavingProductSerializer, SavingProductOptionsSerializer, SavingProductWithOptionsSerializer, LoanForHomeSerializer, LoanForHomeOptionsSerializer, LoanForHomeWithOptionsSerializer

from pprint import pprint as print

# Create your views here.
#  함수 2개로 짜기(DB 저장하는 것 + 저장된 파일을 보내는 것)
# 금융회사정보-----------------------------------------------------------------------------------------------------------------------
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
    return Response('I Saved')
    # JsonResponse은 Json으로 담아서 보내는 것! dict 객체만 가능
    # 여기까지가 저장하는 것! 근데 return으로 화면에 띄우는 건 없애자 나중에


@api_view(['GET'])
def financialCompanyGive(request):
    financial_company_data_all = get_list_or_404(FinancialCompany)
    serializer = FinancialCompanySerializer(financial_company_data_all, many=True)
    return Response(serializer.data)
    # 이게 전달해주는 거



# 예금정보 DB 저장하는 것(직렬화 된 것 고려하기)-----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
def depositProductSave(request):
    api_key = settings.FINLIFE_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    deposit_product_data=DepositProduct.objects.all()
    deposit_product_data.delete()
    response = requests.get(url).json()
    for deposit in response['result']['baseList']:
        data = {
            'fin_co_no' : deposit['fin_co_no'],
            'kor_co_nm' : deposit['kor_co_nm'],
            'fin_prdt_cd' : deposit['fin_prdt_cd'],
            'fin_prdt_nm' : deposit['fin_prdt_nm'],
            'join_way' : deposit['join_way'],
            'join_member' : deposit['join_member'],
            'join_deny' : deposit['join_deny'],
            'max_limit' : deposit['max_limit'],
            'spcl_cnd' : deposit['spcl_cnd'],
            'mtrt_int' : deposit['mtrt_int'],
            'etc_note' : deposit['etc_note'],
        }

        serializer = DepositProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for option in response['result']['optionList']:
        data = {
            
            'intr_rate_type' : option['intr_rate_type'],
            'intr_rate_type_nm' : option['intr_rate_type_nm'],
            'intr_rate' : option['intr_rate'],
            'intr_rate2' : option['intr_rate2'],
            'save_trm' : option['save_trm'],
            'deposit_product' : option['fin_prdt_cd']
        } 

        serializer = DepositProductOptionsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return Response(response)
    # return으로 화면에 띄우는 건 없애자 나중에


@api_view(['GET'])
def depositProductGive(request):
    # deposit_product_data_all = get_list_or_404(DepositProduct)
    deposit_product_data_all = DepositProduct.objects.all()
    serializer = DepositProductWithOptionsSerializer(deposit_product_data_all, many=True)
    return Response(serializer.data)


# 게시글 한 개 불러오기
@api_view(['GET'])
def depositProductDetail(request, deposit_id):
    deposit_detail = DepositProduct.objects.get(pk=deposit_id)
    serializer = DepositProductWithOptionsSerializer(deposit_detail)
    return Response(serializer.data)




# 적금정보 DB 저장하는 것(직렬화 된 것 고려하기)-----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
def savingProductSave(request):
    api_key = settings.FINLIFE_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    saving_product_data=SavingProduct.objects.all()
    saving_product_data.delete()
    response = requests.get(url).json()

    for saving in response['result']['baseList']:
        data = {
            'fin_co_no' : saving['fin_co_no'],
            'kor_co_nm' : saving['kor_co_nm'],
            'fin_prdt_cd' : saving['fin_prdt_cd'],
            'fin_prdt_nm' : saving['fin_prdt_nm'],
            'join_way' : saving['join_way'],
            'join_member' : saving['join_member'],
            'join_deny' : saving['join_deny'],
            'max_limit' : saving['max_limit'],
            'spcl_cnd' : saving['spcl_cnd'],
            'mtrt_int' : saving['mtrt_int'],
            'etc_note' : saving['etc_note'],
        }

        serializer = SavingProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for option in response['result']['optionList']:
        data = {
            'intr_rate_type' : option['intr_rate_type'],
            'intr_rate_type_nm' : option['intr_rate_type_nm'],
            'intr_rate' : option['intr_rate'],
            'intr_rate2' : option['intr_rate2'],
            'save_trm' : option['save_trm'],
            'saving_product' : option['fin_prdt_cd']
        }

        serializer = SavingProductOptionsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return Response('I Saved')
    # return으로 화면에 띄우는 건 없애자 나중에


@api_view(['GET'])
def savingProductGive(request):
    saving_product_data_all = get_list_or_404(SavingProduct)
    serializer = SavingProductWithOptionsSerializer(saving_product_data_all, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def savingProductDetail(request, saving_id):
    saving_detail = SavingProduct.objects.get(pk=saving_id)
    serializer = SavingProductWithOptionsSerializer(saving_detail)
    return Response(serializer.data)




# 전세자금대출정보 DB 저장하는 것(직렬화 된 것 고려하기)-----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
def loanForHomeSave(request):
    api_key = settings.FINLIFE_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    loan_for_home_data=LoanForHome.objects.all()
    loan_for_home_data.delete()
    response = requests.get(url).json()

    for loanhome in response['result']['baseList']:
        if LoanForHome.objects.filter(fin_prdt_cd=loanhome['fin_prdt_cd']).exists():
            continue

        data = {
            'fin_co_no' : loanhome['fin_co_no'],
            'kor_co_nm' : loanhome['kor_co_nm'],
            'fin_prdt_cd' : loanhome['fin_prdt_cd'],
            'fin_prdt_nm' : loanhome['fin_prdt_nm'],
            'loan_lmt' : loanhome['loan_lmt'],
            'loan_inci_expn' : loanhome['loan_inci_expn'],
            'erly_rpay_fee' : loanhome['erly_rpay_fee'],
            'dly_rate' : loanhome['dly_rate'],
        }

        serializer = LoanForHomeSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for option in response['result']['optionList']:
        data = {
            'lend_rate_type' : option['lend_rate_type'],
            'lend_rate_type_nm' : option['lend_rate_type_nm'],
            'lend_rate_avg' : option['lend_rate_avg'],
            'lend_rate_min' : option['lend_rate_min'],
            'lend_rate_max' : option['lend_rate_max'],
            'loan_home_product' : option['fin_prdt_cd']
        }

        serializer = LoanForHomeOptionsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return Response('I Saved')
    # return으로 화면에 띄우는 건 없애자 나중에

@api_view(['GET'])
def loanForHomeGive(request):
    loan_for_home_data_all = get_list_or_404(LoanForHome)
    serializer = LoanForHomeWithOptionsSerializer(loan_for_home_data_all, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def loanForHomeDetail(request, loan_id):
    loan_detail = LoanForHome.objects.get(pk=loan_id)
    serializer = LoanForHomeWithOptionsSerializer(loan_detail)
    return Response(serializer.data)
