from django.db import models

from .managers import MemberNames, NonMemberPartnerNames, DependentNames, UserNames

class Name(models.Model):
    kind = 'member.basic::Name'

    objects = models.Manager()
    member_names = MemberNames()
    non_member_partner_names = NonMemberPartnerNames()
    dependent_names = DependentNames()
    user_names = UserNames()

    # The model which this name is contributed to.
    # Currently, the following models have names:
    # - User
    # - Member
    # - NonMemberPartner
    # - Dependent
    # Use the appropriate mananager for the given 
    role = models.CharField(max_length=32)

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    alias = models.CharField(max_length=32, blank=True)
