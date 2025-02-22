from django.urls import path
from .views import github_login, github_callback,check_auth

urlpatterns = [
    path("github/login/", github_login, name="github_login"),
    path("github/callback/", github_callback, name="github_callback"),
    path("check/", check_auth, name="check_auth"),  # Add this line
]
