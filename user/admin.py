from django.contrib import admin
from django.contrib.auth.models import Group
from django.core.mail import send_mail


from .models import User
# Register your models here.



class UserAdminConf(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        '''
            check if the 'verified field is changed on the model. If yes, and verified is true, sends the mail.
        '''
        
        # if 'verified' in form.changed_data and obj.verified:
        #     # send mail
        #     print("mail was sent from the signal. to the user")
        #     # using the python inbuilt backend
        #         # send_mail(
        #         #     "verification for author user", # message title
        #         #     f"please verify the user {instance.id} as author", # message
        #         #     "stmsng2001@gmail.com", # message mail
        #         #     ["stmsng2001@gmail.com"], # message recipients
        #         # )
            
        #     print("Notify the author about the verification")
        #     mail_result = send_mail(
        #     subject = 'You have been verified',
        #     message = f'''you have been verified as an author, go to the following link to create blogs:
        #         http://127.0.0.1:9000/blog/create/
        #     ''',
        #     from_email = 'satansin2001@gmail.com',
        #     recipient_list = [obj.email],
        #     fail_silently=False,
        #     )


        if 'verified' in form.changed_data and obj.verified:
            author_group = Group.objects.get(name = "author")
            print(author_group)
            breakpoint()
            print("before",obj.groups)
            obj.groups.add(author_group)
            print("after",obj.groups)
            # obj.save()
        obj.save()

    
admin.site.register(User, UserAdminConf)
