from django.db import models
from ext.django.managers import RoleManager

class MemberCarers(RoleManager):
    @property
    def model_kind(self):
        from member.models import Member
        return Member.objects.kind

class NonMemberPartnerCarers(models.Manager): 
    @property
    def model_kind(self):
        from member.partner.models import NonMemberPartner
        return NonMemberPartner.objects.kind
