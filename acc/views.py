from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
# Create your views here.
def update(request):
    if request.method == "POST":
        u = request.user
        up = request.POST.get("upass")
        uc = request.POST.get("ucomm")
        um = request.POST.get("umail")
        pi = request.FILES.get("upic")
        if up:
            u.set_password(up)
        u.comment = uc
        u.email = um
        if pi:
            u.pic.delete()
            u.pic = pi
        u.save()
        login(request, u)
        return redirect("acc:profile")
    return render(request, "acc/update.html")

def delete(request):
    request.user.delete()
    return redirect("acc:index")

def profile(request):
    return render(request, "acc/profile.html")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        uc = request.POST.get("ucomm")
        pi = request.FILES.get("upic")
        User.objects.create_user(username=un, password=up, comment=uc, pic=pi)
        return redirect("acc:login")
        # print(un, up, uc, pi)
    return render(request, "acc/signup.html")


def index(request):
    return render(request, "acc/index.html")

def logout_user(request):
    logout(request)
    return redirect("acc:index")

def login_user(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        user = authenticate(username=un, password=up)
        if user:
            login(request, user)
            return redirect("acc:index")
    return render(request, "acc/login.html")

