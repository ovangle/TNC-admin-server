from django.db import models

from member.basic.models import Address, Contact, Name
from .availability.models import Availability 


class StaffMemberManager(models.Manager):
    kind = 'staff::StaffMember'

    def create(self, user, name, type):
        return super(StaffMemberManager, self).create(
            user=user,
            name=Name.user_names.create(**name),
            type=type,
            address=Address.objects.create(),
            contact=Contact.objects.create(),
            availability=Availability.objects.create()
        )
