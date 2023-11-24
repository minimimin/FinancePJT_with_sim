from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommend_product),
    path('signup/', views.signup_product),
]
