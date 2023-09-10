from django.shortcuts import render

# Create your views here.


def login_view(request):
    return render(request, "members/login.html")


def signup_view(request):
    return render(request, "members/signup.html")
