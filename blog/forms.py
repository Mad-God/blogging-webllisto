from django import forms
from .models import Blog, Category
from user.models import User
from datetime import datetime
from django.core.mail import send_mail
from tinymce.widgets import TinyMCE
from django.shortcuts import reverse

# from django.contrib.flatpages.models import FlatPage



class BlogCreationForm(forms.ModelForm):

    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}, mce_attrs={}))


    class Meta:
        model = Blog
        fields = ("title", 'body', 'img','category', "deleted", "published")

    
    def save(self, commit=True, **kwargs):
        m = super(BlogCreationForm, self).save()

        if "deleted" in self.changed_data and self.cleaned_data["deleted"]:

            # send mail
            print("Notify the admin for deletion")
            mail_result = send_mail(
            subject = f'Deletion has been requested for blog: {str(m)}',
            message = f'''Author {m.author} has requested deletion of the blog:
                {m.title}
                {m.body}
            ''',
            from_email = 'satansin2001@gmail.com',
            recipient_list = ['stmsng2001@gmail.com'],
            fail_silently=False,
            )
        return m
    

    def __init__(self, *args, **kwargs):
        # breakpoint()    
        user = None
        if "user" in kwargs:
            user = kwargs.pop('user')

        super(BlogCreationForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget = forms.CheckboxSelectMultiple()
        self.fields['category'].queryset = Category.objects.all()
        
        blog = self.instance
        if user:
            blog.author = user
        



class CategoryCreationForm(forms.ModelForm):


    class Meta:
        model = Category
        fields = ("name",)

    
    def saveasdasd(self, commit=True, **kwargs):
        m = super(BlogCreationForm, self).save()
        if "deleted" in self.changed_data and self.cleaned_data["deleted"]:

            # send mail
            print("Notify the admin for deletion")
            mail_result = send_mail(
            subject = f'Deletion has been requested for blog: {str(m)}',
            message = f'''Author {m.author} has requested deletion of the blog:
                {m.title}
                {m.body}
            ''',
            from_email = 'satansin2001@gmail.com',
            recipient_list = ['stmsng2001@gmail.com'],
            fail_silently=False,
            )
        return m

