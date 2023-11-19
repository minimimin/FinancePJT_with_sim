from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_info),
    path('profile/<int:user_pk>/', views.user_profile),
]
