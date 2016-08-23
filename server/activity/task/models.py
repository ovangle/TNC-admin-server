from django.db import models
from ext.django.fields import EnumField

from member.models import Member
from staff.models import StaffMember

from .task_type import TaskType

class Task(models.Model):
    # The staff member responsible for adding this task.
    staff = models.ForeignKey(StaffMember)
    # The member which this task applies to
    member = models.ForeignKey(Member)
    type = EnumField(enum_type=TaskType)
    at = models.DateTimeField(auto_now_add=True)
