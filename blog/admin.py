from django.contrib import admin
from .models import Blog, Category
from .forms import BlogCreationForm
# Register your models here.



# class CustomBlogAdmin(admin.ModelAdmin):
#     form = BlogCreationForm
    

admin.site.register(Blog)
admin.site.register(Category)

 