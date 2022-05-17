from django.contrib import admin
from django.contrib.auth.models import Group
from django.core.mail import send_mail


from .models import User
# Register your models here.



class UserAdminConf(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super(UserAdminConf, self).save_model(request, obj, form, change)
        if change:
            author_group = Group.objects.get(name = "author")
            author_group.user_set.add(obj)
            obj.save()
        
    

 
admin.site.register(User, UserAdminConf)
