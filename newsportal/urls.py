from django.contrib import admin
from django.urls import path
from newsportals import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='index'),
    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('news/create/', views.news_create, name='news_create'),  # Added this line
]