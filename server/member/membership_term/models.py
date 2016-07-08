from django.db import models
from ext.django.fields import EnumField 

from .term_type import MembershipTermType
from .managers import MembershipTermManager

class MembershipTerm(models.Model):
    objects = MembershipTermManager()

    type = EnumField(enum_type=MembershipTermType)

    joined = models.DateTimeField()
    renewed = models.DateTimeField(null=True)

    expires = models.DateTimeField()