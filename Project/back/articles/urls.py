from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('category/', views.category_list),
    path('comment/<int:article_pk>/', views.comment_list),
    path('comment/<int:article_pk>/<int:comment_pk>/', views.comment_detail),
]
