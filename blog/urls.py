from django.contrib import admin
from django.urls import path
from .views import *
# from shop import views


app_name = "blog"

urlpatterns = [
    path('', blog_create,name = 'create'),
    path('create', blog_create,name = 'create'),
    path('update/<int:pk>', blog_update,name = 'update'),
    path('list', blog_list,name = 'list'),
]