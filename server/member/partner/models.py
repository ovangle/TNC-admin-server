from django.db import models
from ext.django.fields import EnumField

from ..basic.contact.models import Contact
from ..basic.gender import Gender
from ..basic.income.models import Income
from ..basic.name.models import Name

from ..carer.models import Carer


class Partner(models.Model):
    pass

class MemberPartner(Partner):
    kind = 'member::MemberPartner'
    _member = models.OneToOneField('member.Member') 

    @property
    def name(self):
        return self._member.name

    @property
    def gender(self):
        return self._member.gender

    @property
    def contact(self):
        return self._member.contact

    @property
    def income(self):
        return self._member.income

    @property
    def carer(self):
        return self._member.carer


class NonMemberPartner(Partner):
    kind = 'member::NonMemberPartner'

    name = models.OneToOneField(Name)
    gender = EnumField(enum_type=Gender)
    contact = models.OneToOneField(Contact)
    income = models.OneToOneField(Income)
    carer = models.OneToOneField(Carer)

