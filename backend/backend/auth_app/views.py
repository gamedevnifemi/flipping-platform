import requests
from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect
from django.http import JsonResponse
from backend.db.models import CustomUser

GITHUB_ACCESS_TOKEN_URL = "https://github.com/login/oauth/access_token"
GITHUB_USER_URL = "https://api.github.com/user"


def github_login(request):
    client_id = settings.SOCIALACCOUNT_PROVIDERS['github']['APP']['client_id']
    redirect_uri = "http://localhost:8000/auth/github/callback/"
    github_auth_url = f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}"
    return redirect(github_auth_url)


def github_callback(request):
    code = request.GET.get("code")
    if not code:
        return JsonResponse({"error": "No code received"}, status=400)

    data = {
        "client_id": settings.SOCIALACCOUNT_PROVIDERS['github']['APP']['client_id'],
        "client_secret": settings.SOCIALACCOUNT_PROVIDERS['github']['APP']['secret'],
        "code": code,
    }
    headers = {"Accept": "application/json"}
    response = requests.post(GITHUB_ACCESS_TOKEN_URL, data=data, headers=headers)
    response_data = response.json()

    if "access_token" not in response_data:
        return JsonResponse({"error": "Failed to get access token"}, status=400)

    access_token = response_data["access_token"]
    user_info = requests.get(GITHUB_USER_URL, headers={"Authorization": f"token {access_token}"}).json()

    # Handle user creation/authentication with optional email
    defaults = {
        "email": user_info.get("email") or "",  # Use empty string if email is None
        "github_id": user_info.get("id"),
        "avatar_url": user_info.get("avatar_url"),
    }

    user, _ = CustomUser.objects.get_or_create(
        username=user_info["login"], 
        defaults=defaults
        )
        # Specify the authentication backend when logging in
    login(request, user, backend='django.contrib.auth.backends.ModelBackend')

    return redirect('http://localhost:5173/dashboard')

def check_auth(request):
    return JsonResponse({
        'isAuthenticated': request.user.is_authenticated,
        'user': {
            'username': request.user.username,
            'avatar_url': request.user.avatar_url
        } if request.user.is_authenticated else None
    })