from django.db import models
from ext.django.fields import EnumField

from .residential_stability import ResidentialStability
from .residence_type import ResidenceType

class ResidentialStatus(models.Model):
    kind = 'member.basic::ResidentialStatus'

    type = EnumField(enum_type=ResidenceType, default='NOT_DISCLOSED')
    stability = EnumField(enum_type=ResidentialStability, default='NOT_DISCLOSED')