from django.urls import path
from members.views import login_view, signup_view


urlpatterns = [
    path("login/", login_view, name="members-login"),
    path("signup/", signup_view, name="members-signup"),
]
