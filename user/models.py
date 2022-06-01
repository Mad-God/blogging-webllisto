from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.core.mail import send_mail




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
        if not email:
            raise ValueError('You must provide an email address')

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
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)

  

    objects = CustomUserManager()   



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']




def post_user_created_signal(sender, instance, created, **kwargs):
    
    if created:
        if instance.author:
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


post_save.connect(post_user_created_signal, sender = User)

