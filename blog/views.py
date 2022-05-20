from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, reverse

from .forms import BlogCreationForm, CategoryCreationForm
from .models import Blog, Category
from .decorators import custom_login_required, allowed_users, group_required
from django.contrib.auth.decorators import permission_required, login_required
from guardian.shortcuts import get_objects_for_user
from .permissions import (IsBlogAuthor, 
            SameUserOnlyMixin,
            is_author_decorator,
            CheckAuthorMixin
)
from django.views.generic import UpdateView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.decorators import method_decorator

# Create your views here.


# @custom_login_required
# @allowed_users(allowed_users = ['author'])
# @permission_required('blog.add_blog')
# @group_required('author')
@permission_required({("blog.view_blog"), ("blog.can_add_new_blog")})
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






# @login_required
# @permission_required("blog.change_blog")
@is_author_decorator
def blog_update(request, slug):

    blog = Blog.objects.get(slug = slug)
    # blogs = get_objects_for_user(request.user, 'blog.can_change_blog', klass = Blog)
    # print(blogs)
    # print(blogs[0])
    # blog = blogs.get(slug=slug)
    print(blog)
    form = BlogCreationForm(instance = blog)
    msg = ''

    # if request.user != blog.author:
    #     return redirect("blog:list")
    
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






class BlogUpdateView(CheckAuthorMixin, UpdateView):
    template_name = 'blog/blog_create.html'
    form_class = BlogCreationForm
    # permission_required = "blog.add_blog"
    # permission_required = (SameUserOnlyMixin,)
    # permission_classes = [IsBlogAuthor]


    def get_success_url(self):

        return reverse('blog:list')     



    # @method_decorator(IsBlogAuthor)
    def get_queryset(self):
        queryset = Blog.objects.all()
        print(queryset)
        return queryset
        
    def get_context_data(self, **kwargs):
        # prod_id = self.kwargs['pk']
        
        # prod = Item.objects.get(id = prod_id)

        context = super().get_context_data(**kwargs)
        context.update({
            'item':"hue hie hieiashsdknakksdn",
            # "prod":prod.product,
        })
        return context


    def form_valid(self, form):
        prod = form.save(commit=False)
        
        prod.save()
        return super(BlogUpdateView, self).form_valid(form)

    # def get_form_kwargs(self):
    #     # self.kwargs
    #     # breakpoint()
    #     it_id = self.kwargs["pk"]
    #     itm = Item.objects.get(id = it_id)
    #     prod = itm.product
    #     kws = super().get_form_kwargs()
    #     kws.update(prod = prod)
    #     return kws







@login_required
@permission_required("blog.view_blog")
def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog/blog_detail.html", {"blog":blog})



@login_required
@permission_required("blog.view_blog")
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


    blogs = Blog.objects.filter(published=True)
    # blogs = get_objects_for_user(request.user, 'blog.view_blog', klass = Blog)
    print(blogs)
    context = {"blogs":blogs}
    context["categories"] = Category.objects.all()
    context["drafts"] = Blog.objects.filter(published=False, author=request.user)
    context["del_request"] = Blog.objects.filter(deleted = True).count()
    print(context["drafts"])
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





#---------------- CATEGORY VIEWS ----------------


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

