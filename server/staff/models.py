from django.db import models
from ext.django.fields import EnumField

from member.basic.models import Name, Address, Contact
from user.models import User

from .availability.models import Availability
from .induction_survey.models import StaffInductionSurvey
from .staff_type import StaffType
from .managers import StaffMemberManager


class StaffMember(models.Model):
    objects = StaffMemberManager()

    kind = objects.kind

    type = EnumField(enum_type=StaffType)

    user = models.OneToOneField(User)
    name = models.OneToOneField(Name)

    availability = models.OneToOneField(Availability)
    address = models.OneToOneField(Address)
    contact = models.OneToOneField(Contact)

    date_of_birth = models.DateField(null=True)

    induction_survey = models.OneToOneField(StaffInductionSurvey, null=True)