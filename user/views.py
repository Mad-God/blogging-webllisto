from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import auth
from django.contrib import messages

from .forms import CustomUserCreationForm, LoginForm
from .models import User
# from agents.mixins import OrganiserLoginRequiredMixin

# Create your views here.

def index(request):
    return render(request, "index.html", {})





def signup(request):
    msg = ''
    form = CustomUserCreationForm
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        # automatically check all the fields and ensure all fields are filled
        if form.is_valid():
            user = form.save()
            print(user)
            print(user.author)

            msg = 'Form Submitted.'
            return redirect("/login")

        else:
            print(form.errors)
            print('\n\nForm Invalid!!!')

    form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "registration/user_create.html", context)





def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = None
        user = auth.authenticate(email = email, password = password)
        if user:

            auth.login(request, user)
            return redirect("blog:list")
        else:
            print(user)
            print("invalid credentials")
            messages.info(request, user)
            return redirect('login')


    else:
        form = LoginForm()
        return render(request, "registration/login.html", {"form":form})


def logout(request):
    auth.logout(request)
    return redirect("login")





def profile_update(request):
    pass