from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, reverse

from .forms import BlogCreationForm, CategoryCreationForm
from .models import Blog, Category




def custom_login_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.verified:
            return view_func(request, *args, **kwargs)
        else:
            return redirect("login")
    return wrapper_func

    pass
