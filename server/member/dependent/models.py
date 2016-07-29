from django.db import models
from ext.django.fields import EnumField

from ..basic.gender import Gender
from ..basic.name.models import Name

from .carer.models import Carer
from .carer_rel.models import CarerRel

class Dependent(models.Model):
    kind = 'dependent::Dependent'

    name = models.OneToOneField(Name)
    carers = models.ManyToManyField(Carer, 
        through=CarerRel, 
        through_fields=('dependent', 'carer')
    ) 

    gender = EnumField(enum_type=Gender)
    date_of_birth = models.DateField(null=True)

