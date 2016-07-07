from django.db import models

from ext.django.fields import EnumField

from .living_arrangement import LivingArrangement
from .relation_type import RelationType

class CarerRel(models.Model):
    kind = 'dependent::CarerRel'

    carer = models.ForeignKey('member.Carer')
    dependent = models.ForeignKey('member.Dependent')

    living_arrangement = EnumField(enum_type=LivingArrangement)
    relation_type = EnumField(enum_type=RelationType)

