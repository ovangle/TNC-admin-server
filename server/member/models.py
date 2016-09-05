from django.db import models

from ext.django.fields import EnumField

from .basic.models import (
    Address, Contact, EnergyAccount, EnergyAccountType, Gender, Income, Name, ResidentialStatus,
)    
from .membership_term.models import MembershipTerm
from .file_notes.models import MemberFileNote

from .dependent.carer.models import Carer
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
    date_of_birth = models.DateField(null=True)
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

    gas_account = models.OneToOneField(
        EnergyAccount,
        null=True,
        related_name='+'
    )

    electricity_account = models.OneToOneField(
        EnergyAccount,
        null=True,
        related_name='+'
    )

    income = models.OneToOneField(
        Income,
        on_delete=models.CASCADE
    )

    partner = models.OneToOneField('member.Member', null=True, related_name='+') 
    carer = models.OneToOneField(Carer, related_name='member_carer')

    updated = models.DateTimeField(auto_now=True)

    def set_partner(self, partner):
        if partner == self.partner:
            return
        if self.partner is None:
            if partner is not None:
                partner.set_partner(self)
                partner.save()
        else:
            if partner is None:
                self.partner.partner = None
                self.partner.save()
            else:
                self.partner.set_partner(self)
                self.partner.save()
        self.partner = partner

    @property
    def energy_accounts(self):
        return {
            'GAS': self.gas_account,
            'ELECTRICITY': self.electricity_account
        }

def create_carer(instance, created, raw, **kwargs):
    #Ignore fixtures and saves for existing courses
    if not created or raw:
        return

    if not instance.carer_id:     
        group, _ = Carer.objects.get_or_create()

    instance.save()

models.signals.post_save.connect(create_carer, sender=Member, dispatch_uid='create_carer')    
