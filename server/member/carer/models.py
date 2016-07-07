from django.db import models

from .managers import MemberCarers, NonMemberPartnerCarers

class Carer(models.Model):
    """
    A carer simply acts as an abstraction interface for a "dependent container"
    Both members and their partners can both have dependents which they may care for,
    so the carer acts as a container model for the dependents
    """
    kind = 'member::Carer'

    objects = models.Manager()
    member_carers = MemberCarers()
    non_member_partner_carers = NonMemberPartnerCarers()

    @classmethod
    def manager_for_role(cls, role): 
        from ..models import Member
        from ..partner.models import NonMemberPartner
        if role == Member.kind:
            return cls.member_carers
        elif role == NonMemberPartner.kind:
            return cls.non_member_partner_carers
        else:    
            raise ValueError('Invalid role for Carer: {0}'.format(role))
            
    # The type of carer that this applies to.
    # Currently the following models can be carers:
    # - Member
    # - NonMemberPartner
    role = models.CharField(max_length=32)

    @property
    def carer(self):
        from ..models import Member
        from ..partner.models import NonMemberPartner
        if self.role == Member.kind:
            return self.member_carer
        elif self.role == NonMemberPartner.kind:
            return self.non_member_partner_carer
        else:
            raise ValueError('Invalid role for Carer: {0}'.format(self.role))

    @property
    def name(self):
        return self.carer.name

