from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, reverse

from .forms import BlogCreationForm, CategoryCreationForm
from .models import Blog, Category
from django.contrib.auth.decorators import user_passes_test




def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False

    return user_passes_test(in_groups, login_url='/login')


def custom_login_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.verified:
            return view_func(request, *args, **kwargs)
        else:
            return redirect("login")
    return wrapper_func


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
        
