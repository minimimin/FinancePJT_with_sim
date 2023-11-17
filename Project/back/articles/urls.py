from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('category/', views.category_list),
    path('category/detail/', views.category_detail),
    path('comment/<int:article_pk>/', views.comment_list),
    path('comment/detail/<int:comment_pk>/', views.comment_detail),
]
