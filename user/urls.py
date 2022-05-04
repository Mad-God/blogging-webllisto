from django.contrib import admin
from django.urls import path
from .views import *
# from shop import views


app_name = "user"

urlpatterns = [
    path('', index,name = 'index'),
    path('profile/<int:pk>/update', profile_update,name = 'profile-update'),
]