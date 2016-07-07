from django.db import models
from ext.django.managers import RoleManager

class MemberNames(RoleManager):
    @property
    def model_kind(self):
        from member.models import Member
        return Member.kind


class NonMemberPartnerNames(RoleManager):  
    @property
    def model_kind(self):
        from member.partner.models import NonMemberPartner
        return NonMemberPartner.kind
  

class DependentNames(models.Manager):
    @property
    def model_kind(self):
        from member.dependent.models import Dependent
        return Dependent.kind


class UserNames(RoleManager):
    @property
    def model_kind(self):
        from user.models import User
        return User.objects.kind
