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

    def get_voucher(self):
        """ 
        Returns the voucher associated with this task (if one exists)
        otherwise None
        """
        try: 
            voucher = self.voucher
        except AttributeError: 
            return None
        return voucher.get_subkind_instance()
