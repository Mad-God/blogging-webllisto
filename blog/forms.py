from django import forms
from .models import Blog
from user.models import User
from datetime import datetime
# from tinymce.widgets import TinyMCE
# from django.shortcuts import reverse


class BlogCreationForm(forms.ModelForm):

    # body = forms.CharField(widget=TinyMCE(mce_attrs={'external_link_list_url': reverse('blog:list')}))


    class Meta:
        model = Blog
        fields = ("title", 'body')

    
    def save(self, commit=True, **kwargs):

        # print(kwargs)/
        m = super(BlogCreationForm, self).save(commit = False)
        # do custom stuff

        # print(type(kwargs["user"]))
        # print(dir(self))
        # print(self.cleaned_data["title"])
        # self.cleaned_data["user"] = User.objects.get(id = kwargs["user"])
        print(self)
        print(m)
        print(type(m))
        print(dir(m))
        m.last_updated = datetime.now()
        if "user" in kwargs:
            user = kwargs["user"]
            m.author = user
            m.author_id = user.id


        if commit:
            m.save()
        return m

