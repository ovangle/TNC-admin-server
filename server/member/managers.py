from django.db import models

from .dependent.carer.models import Carer
from .dependent.carer_rel.models import CarerRel

class MemberManager(models.Manager):
    @property
    def kind(self):
        return 'member::Member'

    def create(self, carer_rels=None, **kwargs):
        kwargs['carer'] = Carer.member_carers.create()

        dependents = kwargs.pop('dependents', list)
        carer_rels = carer_rels or []

        member = super(MemberManager, self).create(**kwargs)

        # Overwrite the existing partner on the member's partner
        partner.set_partner(member)

        for carer_rel in carer_rels:
            pass

        partner.save()

        return member
