from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_info),
    path('profile/<int:user_pk>/', views.user_profile),
    # path('profile/<int:user_pk>/deposit/', views.user_profile_deposit),
    # path('profile/<int:user_pk>/saving/', views.user_profile_saving),
    # path('profile/<int:user_pk>/loan/', views.user_profile_loan),
]
