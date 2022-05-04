from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, reverse

from .forms import BlogCreationForm
from .models import Blog


# Create your views here.



def blog_create(request):
    msg = ''
    if not request.user.verified:
        msg = "you are not verified as an author"
    
    
    if request.method == 'POST':
        form = BlogCreationForm(request.POST)

        if form.is_valid():
            # print(request.user.email, request.user.id)
            form.save(user = request.user)
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

    form = BlogCreationForm()
    context = {"form": form, "msg":msg}
    return render(request, "blog/blog_create.html", context)




def blog_update(request, pk):

    blog = Blog.objects.get(id = pk)
    
    form = BlogCreationForm(instance = blog)
    msg = ''
    if request.user != blog.author:
        return redirect("blog:list")
    
    # form = BlogCreationForm
    if request.method == 'POST':
        form = BlogCreationForm(request.POST, instance = blog)

        if form.is_valid():
            form.save()

            return redirect("blog:list")

        else:
            print(form.errors)
            print('\n\nForm Invalid!!!')

    context = {"form": form, "msg":msg, "blog":blog}
    return render(request, "blog/blog_create.html", context)





def blog_list(request):
    blogs = Blog.objects.all()
    print(blogs)
    context = {"blogs":blogs}
    return render(request, "blog/blog_list.html", context)
