from django.db import models
from django.contrib.postgres.fields import JSONField

from ..permissions import Permissions

class UserGroup(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    _permissions = JSONField(default=dict)

    def _get_permissions(self):
        return Permissions.from_json(self._permissions)

    def _set_permissions(self, permissions):
        self._permissions = permissions.to_json

    permissions = property(_get_permissions, _set_permissions)

