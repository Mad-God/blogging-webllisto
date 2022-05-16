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


def allowed_users(allowed_users = []):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                for gp in request.user.groups.all():
                    if gp.name in allowed_users:
                        print("\n\n\nworking\n\n\n")
                        return view_func(request, *args, **kwargs)
                return HttpResponse("You cant view this  page")
        return wrapper_func
    return decorator
        
