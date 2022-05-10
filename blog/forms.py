from django import forms
from .models import Blog, Category
from user.models import User
from datetime import datetime
from django.core.mail import send_mail
# from tinymce.widgets import TinyMCE
# from django.shortcuts import reverse


class BlogCreationForm(forms.ModelForm):

    # body = forms.CharField(widget=TinyMCE(mce_attrs={'external_link_list_url': reverse('blog:list')}))


    class Meta:
        model = Blog
        fields = ("title", 'body', 'img','category', "deleted")

    
    def save(self, commit=True, **kwargs):
        # breakpoint()
        m = super(BlogCreationForm, self).save()
        if "deleted" in self.changed_data and self.cleaned_data["deleted"]:

            # send mail
            print("notification was sent to admin")
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


        # m.last_updated = datetime.now() 
        # if "user" in kwargs:
        #     user = kwargs["user"]
        #     m.author = user
            # m.author_id = user.id
        print("m.deleted", m.deleted)
        print("cleaned data deleted", self.cleaned_data["deleted"])
        # m.save()    
        return m

    #   print(m.category)
        # if commit:
        #     m.save()
    #     print(m.get_all_data())
        # m.category.set(self.cleaned_data["category"])
        # return m
    

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

    # body = forms.CharField(widget=TinyMCE(mce_attrs={'external_link_list_url': reverse('blog:list')}))


    class Meta:
        model = Category
        fields = ("name",)

    
    def saveasdasd(self, commit=True, **kwargs):
        m = super(BlogCreationForm, self).save()
        if "deleted" in self.changed_data and self.cleaned_data["deleted"]:

            # send mail
            print("notification was sent to admin")
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
        print("m.deleted", m.deleted)
        print("cleaned data deleted", self.cleaned_data["deleted"])
        return m


    def __init__asdasd(self, *args, **kwargs):
        user = None
        if "user" in kwargs:
            user = kwargs.pop('user')

        super(BlogCreationForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget = forms.CheckboxSelectMultiple()
        self.fields['category'].queryset = Category.objects.all()
        
        blog = self.instance
        if user:
            blog.author = user
        
