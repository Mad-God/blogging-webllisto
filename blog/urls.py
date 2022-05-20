from django.contrib import admin
from django.urls import path
from .views import *
# from shop import views



app_name = "blog"

urlpatterns = [
    path('', blog_create,name = 'create'),
    # blog urls
    path('list', blog_list,name = 'list'),
    path('create', blog_create,name = 'create'),
    path('detail/<slug>', blog_detail,name = 'detail'),
    path('for-deletion', blog_for_deletion,name = 'to-delete-blog'),
    # path('update/<slug>', blog_update,name = 'update'),
    path('update/<slug>', BlogUpdateView.as_view(),name = 'update'),
    path('delete-blog/<slug>', blog_delete,name = 'blog-delete'),
    
    # catgory urls
    path('category/<slug>', blog_by_category,name = 'category-blog'),
    path('create-category', category_create,name = 'create-category'),
    path('category-delte/<slug>', category_delete,name = 'category-delete'),
    path('category-list', category_list,name = 'category-list'),
]