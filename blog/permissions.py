from rest_framework import permissions
from django.http import Http404
from django.shortcuts import redirect, HttpResponse
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Blog
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


def is_author_decorator(detail_view):
    def wrapper_func(request, slug, *args, **kwargs):
        blog = Blog.objects.get(slug = slug)
        if request.user and request.user == blog.author:
            return detail_view(request,slug,  *args, **kwargs)
        else:
            return HttpResponse("You are not the auhtor.")
    return wrapper_func

  
class IsBlogAuthor(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return True

    def has_permission(self, request, view, obj):            
        breakpoint()
        return True
    
    

class SameUserOnlyMixin(object):

    def has_permissions(self):
        # Assumes that your Article model has a foreign key called `auteur`.
        return self.get_object().author == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404('You do not have permission. huehuehue')
        return super(SameUserOnlyMixin, self).dispatch(
            request, *args, **kwargs)


class CheckAuthorMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user == self.get_object().author


    def handle_no_permission(self):
        return HttpResponse("You are not the author. I am CheckAuthorMixin")
