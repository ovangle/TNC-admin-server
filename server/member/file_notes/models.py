from django.db import models
from ext.rest_framework.fields import EnumField

from member.models import Member
from staff.models import StaffMember

from .severity import Severity

class FileNote(models.Model):
    staff = models.ManyToOneField(StaffMember)

    member = models.OneToManyField(Member)

    # Whether the note is pinned to the member.
    pinned = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    severity = EnumField(
        enum_type=Severity,
        default=Severity.info
    )   

    message = models.TextField()

