from django.urls import path
from . import views

urlpatterns = [
    path('companyinfo/save/', views.financialCompanySave),
    path('companyinfo/', views.financialCompanyGive),
    path('depositinfo/save/', views.depositProductSave),
    path('depositinfo/', views.depositProductGive),
    path('savinginfo/save/', views.savingProductSave),
    path('savinginfo/', views.savingProductGive),
    path('loanforhome/save/', views.loanForHomeSave),
    path('loanforhome/', views.loanForHomeGive),
    path('loanforperson/save/', views.loanForPersonSave),
    path('loanforperson/', views.loanForPersonGive),
    # path('detail/<str:fin_prdt_cd>', views.financial),
    # 디테일(상품 상세 페이지로 가게)
    # path('', views.)
]
