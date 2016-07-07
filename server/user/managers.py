from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    kind = 'admin.user::User'

    def create(self, username, groups):
        from .models import User
        password = self.make_random_password()
        user = User(username=username) 

        user.set_password(self.make_random_password())
        user.save()

        for group in groups:
            user.groups.add(group)
        user.save()
        user._password = password

        return user

