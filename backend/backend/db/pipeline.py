from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import get_user_model
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

User = get_user_model()

class GitHubAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        github_data = sociallogin.account.extra_data
        
        # Only update if values have changed
        if (user.github_id != github_data.get('id') or 
            user.avatar_url != github_data.get('avatar_url')):
            user.github_id = github_data.get('id')
            user.avatar_url = github_data.get('avatar_url')
            user.save(update_fields=['github_id', 'avatar_url'])
        
        return user

save_github_profile = GitHubAdapter
