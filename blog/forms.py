from django import forms
from .models import Blog, Category
from user.models import User
from datetime import datetime
# from tinymce.widgets import TinyMCE
# from django.shortcuts import reverse


class BlogCreationForm(forms.ModelForm):

    # body = forms.CharField(widget=TinyMCE(mce_attrs={'external_link_list_url': reverse('blog:list')}))


    class Meta:
        model = Blog
        fields = ("title", 'body', 'category')

    
    def save(self, commit=True, **kwargs):

        m = super(BlogCreationForm, self).save(commit = False)

        m.last_updated = datetime.now() 
        if "user" in kwargs:
            user = kwargs["user"]
            m.author = user
            # m.author_id = user.id


    #   print(m.category)
        if commit:
            m.save()
    #     print(m.get_all_data())
        m.category.set(self.cleaned_data["category"])
        return m
    

    def __init__(self, *args, **kwargs):
        super(BlogCreationForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget = forms.CheckboxSelectMultiple()
        self.fields['category'].queryset = Category.objects.all()

