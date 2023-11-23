from django.urls import path
from . import views

urlpatterns = [
    path('companyinfo/save/', views.financialCompanySave),
    path('companyinfo/', views.financialCompanyGive),
    path('depositinfo/save/', views.depositProductSave),
    path('depositinfo/', views.depositProductGive),
    path('depositinfo/<int:deposit_id>/', views.depositProductDetail),
    path('savinginfo/save/', views.savingProductSave),
    path('savinginfo/', views.savingProductGive),
    path('savinginfo/<int:saving_id>/', views.savingProductDetail),
    path('loanforhome/save/', views.loanForHomeSave),
    path('loanforhome/', views.loanForHomeGive),
    path('loanforhome/<int:loan_id>/', views.loanForHomeDetail),
]
