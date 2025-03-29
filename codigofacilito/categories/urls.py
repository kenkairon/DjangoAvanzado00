from django.contrib import admin
from categories.views import index
from django.urls import path

app_name  ='categories'
urlpatterns = [
    path('',index, name='index'),
]