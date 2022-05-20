from django.contrib import admin
from .models import Blog, Category
from .forms import BlogCreationForm
from guardian.admin import GuardedModelAdmin
# Register your models here.



class CustomBlogAdmin(GuardedModelAdmin):
    pass  
    

admin.site.register(Blog, CustomBlogAdmin)
admin.site.register(Category)

 