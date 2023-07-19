from typing import Any, Optional
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest

class UsernameEmailBackend(ModelBackend):
    def authenticate(self, request: HttpRequest, username: str | None = ..., password: str | None = ..., **kwargs: Any) -> AbstractBaseUser | None:
        UserModel = get_user_model()
        user = super().authenticate(request, username, password, **kwargs)
        if not user:
            user = UserModel.objects.filter(email = username).first()
            if user and  user.check_password(password):
                return user
            return None
        return user