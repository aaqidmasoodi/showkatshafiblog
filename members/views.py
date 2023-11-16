from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from .forms import LoginForm, RegisterForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "members/login.html"


class LogoutView(auth_views.LogoutView):
    template_name = "members/logout.html"


class SignupView(generic.CreateView):
    form_class = RegisterForm
    template_name = "members/signup.html"
    success_url = reverse_lazy("members-login")
