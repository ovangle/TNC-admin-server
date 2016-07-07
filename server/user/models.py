from functools import reduce

from django.db import models

from django.contrib.postgres.fields import JSONField 

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password, check_password

from ext.django.fields import EnumField

from .group.models import UserGroup
from .permissions import Permissions

from .managers import UserManager

class User(AbstractBaseUser):
    objects = UserManager()

    USERNAME_FIELD = 'username'

    username = models.CharField(max_length=128, unique=True)

    # An admin user has all permissions, without needing to explicitly 
    # specify groups or extra permissions.
    # There can only ever be one admin user
    is_admin = models.BooleanField(default=False)

    # Groups bundle permissions to apply them to many users
    groups = models.ManyToManyField(UserGroup)  

    # Special permissions added to this particular user.
    _extra_permissions = JSONField(default=dict)

    def _get_extra_permissions(self):
        return Permissions.from_json(self._extra_permissions)

    def _set_extra_permissions(self, permissions):
        self._extra_permissions = permissions.to_json()

    extra_permissions = property(_get_extra_permissions, _set_extra_permissions)

    def set_password(self, password):
        self._password = password
        return super(User, self).set_password(password)

    def get_full_name(self): 
        return self.username

    def get_short_name(self):
        return self.username

    def permissions(self):
        group_permissions = map(lambda group: group.permissions)
        return reduce(
            lambda acc, permissions: acc.merge(permissions),
            group_permissions,
            self.extra_permissions
        )

    def has_permission(self, key, action):
        return self.permissions.check_permission(action)
