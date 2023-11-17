from django.urls import path
from . import views

urlpatterns = [
    # path('<int:user_pk>/', views.user_profile)
    path('<int:user_pk>/', views.user_profile)
]
