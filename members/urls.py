from django.urls import path
from members.views import LoginView, SignupView, LogoutView


urlpatterns = [
    path("login/", LoginView.as_view(), name="members-login"),
    path("logout/", LogoutView.as_view(), name="members-logout"),
    path("signup/", SignupView.as_view(), name="members-signup"),
]
