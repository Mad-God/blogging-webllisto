from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import auth
from django.contrib import messages

from .forms import CustomUserCreationForm, LoginForm
from .models import User

# Create your views here.

def index(request):
    return render(request, "index.html", {})





def signup(request):
    msg = ''
    form = CustomUserCreationForm
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            msg = 'Form Submitted.'
            return redirect("/login")

        else:
            print(form.errors)

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