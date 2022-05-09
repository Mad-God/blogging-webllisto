from django.contrib import admin
from django.urls import path
from .views import *
# from shop import views



app_name = "blog"

urlpatterns = [
    path('', blog_create,name = 'create'),
    path('create', blog_create,name = 'create'),
    # path('create', blog_create2,name = 'create2'),
    path('update/<slug>', blog_update,name = 'update'),
    path('list', blog_list,name = 'list'),
    path('category/<slug>', blog_by_category,name = 'category-blog'),
    path('for-deletion', blog_for_deletion,name = 'to-delete-blog'),
    path('delete-blog/<slug>', blog_delete,name = 'blog-delete'),
]