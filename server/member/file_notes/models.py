from django.db import models
from ext.django.fields import EnumField

from .severity import Severity
from .managers import FileNoteManager 

class MemberFileNote(models.Model):
    objects = FileNoteManager()

    staff = models.ForeignKey('staff.StaffMember')

    member = models.ForeignKey('member.Member')

    # Whether the note is pinned to the member.
    pinned = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    severity = EnumField(enum_type=Severity) 

    message = models.TextField()

