from django.db import models

from ext.django.fields import EnumField

from .basic.models import (
    Address, Contact, EnergyAccount, Income, Name, ResidentialStatus
)    
from .basic.gender import Gender
from .membership_term.models import MembershipTerm

from .partner.models import Partner

from .carer.models import Carer
from .dependent.models import Dependent

from .voucher.models import Voucher

from .managers import MemberManager


class Member(models.Model):
    objects = MemberManager()

    kind = objects.kind

    name = models.OneToOneField(
        Name,
        on_delete=models.CASCADE
    )

    gender = EnumField(enum_type=Gender)
    date_of_birth = models.DateField()
    aboriginal_or_torres_strait_islander = models.NullBooleanField()
    register_consent = models.NullBooleanField()

    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE
    )

    term = models.ForeignKey(
        MembershipTerm,
        on_delete=models.CASCADE
    )

    residential_status = models.OneToOneField(
        ResidentialStatus,
        on_delete=models.CASCADE
    )

    contact = models.OneToOneField(
        Contact,
        on_delete=models.CASCADE
    )

    energy_account = models.OneToOneField(
        EnergyAccount,
        on_delete=models.CASCADE
    )

    income = models.OneToOneField(
        Income,
        on_delete=models.CASCADE
    )

    is_partnered = models.NullBooleanField()
    partner = models.OneToOneField(Partner, null=True) 
    carer = models.OneToOneField(Carer, related_name='member_carer')


def create_carer(instance, created, raw, **kwargs):
    #Ignore fixtures and saves for existing courses
    if not created or raw:
        return

    if not instance.carer_id:     
        group, _ = Carer.objects.get_or_create()

    instance.save()

models.signals.post_save.connect(create_carer, sender=Member, dispatch_uid='create_carer')    
