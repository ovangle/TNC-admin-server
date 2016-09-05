from django.db import models

from .dependent.carer.models import Carer
from .dependent.carer_rel.models import CarerRel

class MemberManager(models.Manager):
    @property
    def kind(self):
        return 'member::Member'

    def create(self, carer_rels=None, **kwargs):
        kwargs['carer'] = Carer.objects.create()

        dependents = kwargs.pop('dependents', list)
        carer_rels = carer_rels or []

        member = super(MemberManager, self).create(**kwargs)

        partner = member.partner

        if (partner is not None):
            partner.set_partner(member)
            partner.save()

        return member
