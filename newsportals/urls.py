from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('news/create/', views.news_create, name='news_create'),
]