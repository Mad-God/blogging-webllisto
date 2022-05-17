from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, reverse

from .forms import BlogCreationForm, CategoryCreationForm
from .models import Blog, Category
from .decorators import custom_login_required, allowed_users, group_required
from django.contrib.auth.decorators import permission_required

# Create your views here.


# @custom_login_required
# @allowed_users(allowed_users = ['author'])
# @permission_required('blog.add_blog')
@group_required('author')
def blog_create(request):
    msg = ''
    # if not request.user.verified:
    #     msg = "you are not verified as an author"
    
    
    if request.method == 'POST':
        form = BlogCreationForm(request.POST,request.FILES or None, user = request.user)

        if form.is_valid():
            # print(request.user.email, request.user.id)
            bl = form.save()
            # bl.author = request.user
            # bl.save()
            # print(form.cleaned_data)
            # title = form.cleaned_data['title']
            # body = form.cleaned_data['body']
            # author = request.user


            # blog = Blog.objects.create(
            #     author = author,
            #     body = body,
            #     title = title
            # )
            # msg = 'Form Submitted.'
            return redirect("blog:list")

        else:
            print(form.errors)
            print('\n\nForm Invalid!!!')

    form = BlogCreationForm(user = request.user)
    context = {"form": form, "msg":msg}
    return render(request, "blog/blog_create.html", context)




def blog_update(request, slug):

    blog = Blog.objects.get(slug = slug)
    
    form = BlogCreationForm(instance = blog)
    msg = ''
    if request.user != blog.author:
        return redirect("blog:list")
    
    # form = BlogCreationForm
    if request.method == 'POST':
        form = BlogCreationForm(request.POST, request.FILES or None, instance = blog)

        if form.is_valid():
            form.save()
             

            return redirect("blog:list")

        else:
            print(form.errors)
            print('\n\nForm Invalid!!!')

    context = {"form": form, "msg":msg, "blog":blog}
    return render(request, "blog/blog_create.html", context)


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog/blog_detail.html", {"blog":blog})


def blog_list(request):

    
    if request.GET.get("q"):
        # print("\n\n\n\n",self.request.GET.get("q"), "get")
        # queryset = queryset.filter(name__icontains = self.request.GET.get("q"))
        # q2 = Product.objects.filter(index__icontains = self.request.GET.get("q"), shop__pk = self.kwargs['pk'])
        # print(q2)
        # print("final qs: ", queryset)
        # queryset = queryset.union(q2)
        blogs = Blog.objects.filter(title__icontains = request.GET.get("q"))
        print(blogs)
        context = {"blogs":blogs}
        context["categories"] = Category.objects.all()
        return render(request, "blog/blog_list.html", context)


    blogs = Blog.objects.all()
    print(blogs)
    context = {"blogs":blogs}
    context["categories"] = Category.objects.all()
    context["del_request"] = Blog.objects.filter(deleted = True).count()
    return render(request, "blog/blog_list.html", context)


def blog_by_category(request, slug = None):

    if request.GET.get("q"):
        # print("\n\n\n\n",self.request.GET.get("q"), "get")
        # queryset = queryset.filter(name__icontains = self.request.GET.get("q"))
        # q2 = Product.objects.filter(index__icontains = self.request.GET.get("q"), shop__pk = self.kwargs['pk'])
        # print(q2)
        # print("final qs: ", queryset)
        # queryset = queryset.union(q2)
        blogs = Blog.objects.filter(title__icontains = request.GET.get("q"))
        print(blogs)
        context = {"blogs":blogs}
        context["categories"] = Category.objects.all()
        return render(request, "blog/blog_list.html", context)

    cat = Category.objects.get(slug = slug)
    blogs = Blog.objects.category(cat)
    # blogs = Blog.objects.all()
    # print(blogs)
    context = {"blogs":blogs}
    context["categories"] = Category.objects.all()
    context["cat_label"] = cat.name
    return render(request, "blog/blog_list.html", context)


def blog_for_deletion(request):
    blogs = Blog.objects.filter(deleted = True)
    return render(request, "blog/blog_list.html", {"blogs":blogs, "num_del":len(blogs)})


def blog_delete(request, slug):
    if request.user.is_superuser:
        blog = Blog.objects.get(slug = slug)
        blog.delete()
    return redirect("blog:list")


# CATEGORY VIEWS


def category_create(request):
    msg = ''
    if not request.user.is_superuser:
        msg = "you are not verified as a superuser"
    
    
    if request.method == 'POST':
        form = CategoryCreationForm(request.POST)

        if form.is_valid():
            bl = form.save()
            return redirect("blog:list")

        else:
            print(form.errors)
            print('\n\nForm Invalid!!!')

    form = CategoryCreationForm()
    context = {"form": form, "msg":msg}
    return render(request, "blog/category/category_create.html", context)



def category_list(request):


    category = Category.objects.all()
    # print(blogs)
    context = {"categories":category}
    
    return render(request, "blog/category/category_list.html", context)



def category_delete(request, slug):
    if request.user.is_superuser:
        blog = Category.objects.get(slug = slug)
        blog.delete()
    return redirect("blog:list")

