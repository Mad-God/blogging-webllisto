from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.shortcuts import redirect, reverse
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.core.mail import send_mail
from .managers import UserManager



class CustomUserManager(BaseUserManager):

    def create_superuser(self, name, email, password, **other_fields):
        # in case these fields are not entered during creation
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('verified', True)
        other_fields.setdefault('author', True)



        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')


        return self.create_user(email, name, password, **other_fields)


    def create_user(self, email, name, password, **other_fields):
        # since email is required
        if not email:
            raise ValueError('You must provide an email address')
        print(self, email, name, password, other_fields)

        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('verified', False)
        other_fields.setdefault('author', False)

        user = self.model(email=email, 
                          name=name, **other_fields)
        user.set_password(password)
        user.save()
        return user




# the old user model, meant to extend the Abstractuser, but then permissions
# clash with new user model

class User2(AbstractBaseUser):
    
    # email = models.EmailField('email address', unique=True)
    # name = models.CharField(max_length=150)

    # # because abstract user defines this field, and it is required by it. So, setting it as null here
    # username = models.CharField(max_length=150, blank = True, null = True)
    
    # # first_name = models.CharField(max_length=150, blank=True)
    # author = models.BooleanField(default = False)
    # description = models.TextField(max_length=200, blank = True, null = True)
    # verified = models.BooleanField(default = False)

    # # the field which is used for logging in
    # USERNAME_FIELD = 'email'

    # # the fields that are required for creating superuser
    # REQUIRED_FIELDS = ["name"]


    # objects = CustomUserManager()

    # def __str__(self):
    #     return self.name
    
    
    # def save(self, *args, **kwargs):
    #     print("printing stuff from : def save(self, *args, **kwargs):")
    #     print(self, args, kwargs)
    #     # kwargs.update["username"] = "none"
    #     super(User, self).save(*args, **kwargs) 
    pass





# new user model

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    name = models.CharField('first name', max_length=30, blank=True)
    is_active = models.BooleanField( default=True)
    is_staff = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False)
    verified = models.BooleanField(default = False)
    author = models.BooleanField(default = False)
    description = models.TextField(max_length=200, blank = True, null = True)

  

    objects = CustomUserManager()



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']





def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        if instance.author:
            print("mail was sent from the signal.")
            # send_mail(
            #     "verification for author user", # message title
            #     f"please verify the user {instance.id} as author",# message
            #     "stmsng2001@gmail.com",# message mail
            #     ["stmsng2001@gmail.com"],# message recipients
            # )
            
            print("Notify the superuser")
            mail_result = send_mail(
            subject = 'Subject here verification for author user',
            message = f'''please verify the user {instance.name} as author, go to the following link:
                http://127.0.0.1:9000/admin/user/user/{instance.id}/change/
            ''',
            from_email = 'satansin2001@gmail.com',
            recipient_list = ['stmsng2001@gmail.com'],
            fail_silently=False,
            )
        

    else:
        if instance.verified:
            print("mail was sent from the signal. to the user")
            # send_mail(
            #     "verification for author user", # message title
            #     f"please verify the user {instance.id} as author",# message
            #     "stmsng2001@gmail.com",# message mail
            #     ["stmsng2001@gmail.com"],# message recipients
            # )
            
            print("Notify the author about the verification")
            mail_result = send_mail(
            subject = 'You have been verified',
            message = f'''you have been verified as an author, go to the following link to create blogs:
                http://127.0.0.1:9000/blog/create/
            ''',
            from_email = 'satansin2001@gmail.com',
            recipient_list = [instance.email],
            fail_silently=False,
            )


post_save.connect(post_user_created_signal, sender = User)

