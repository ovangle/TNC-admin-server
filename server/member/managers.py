from django.db import models

from .carer.models import Carer

class MemberManager(models.Manager):
    @property
    def kind(self):
        return 'member::Member'

    def create(self, **kwargs):
        kwargs['carer'] = Carer.member_carers.create()
        return super(MemberManager, self).create(**kwargs)