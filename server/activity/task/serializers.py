from rest_framework import serializers
from ext.rest_framework.fields import EnumField

from staff.models import StaffMember
from member.models import Member
from member.basic.serializers import NameSerializer

from ..voucher.models import FoodcareVoucher, ChemistVoucher, EAPAVoucher
from ..voucher.serializers import VoucherSerializer, FoodcareVoucherSerializer, ChemistVoucherSerializer, EAPAVoucherSerializer


from .models import Task
from .task_type import TaskType

class TaskSerializer(serializers.Serializer):
    """
    A task is a unit of work, signed by a particular staff member.

    Supported task types are:
        - Issue voucher:
            Issue a voucher to a member
        - Referral     
            Make a referral to an external service
    """        
    id = serializers.IntegerField(read_only=True)

    member_id = serializers.PrimaryKeyRelatedField(queryset=Member.objects.all())

    # The staff member who initialized the task
    staff_id = serializers.PrimaryKeyRelatedField(read_only=True)
    # Include the name for displaying in results
    staff_name = NameSerializer(read_only=True, source='staff.name')

    type = EnumField(enum_type=TaskType)

    at = serializers.DateTimeField(read_only=True)

    voucher = VoucherSerializer(required=False)

    def validate(self, data):
        task_type = data.get('type')
        data = self._check_issue_voucher(data, task_type is TaskType.issue_voucher)
        return data

    def _check_issue_voucher(self, data, is_issue_voucher=False):
        if is_issue_voucher:
            if data.get('voucher') is None:
                raise ValidationError('A `voucher` is required for a task type `ISSUE_VOUCHER`')
        else:    
            if data.get('voucher') is not None:
                raise ValidationError('A `voucher` can only be provided for task type `ISSUE_VOUCHER`')
        return data        

    def create(self, validated_data):      
        staff_member = validated_data.get('staff_member')
        if staff_member is None:
            raise ValueError('A staff member is required to create a Task')
        task_type = validated_data.get('type') 

        task = Task(
            staff=staff_member, 
            member=validated_data.get('member_id'),
            type=task_type,
        )
        task.save()

        if task_type is TaskType.issue_voucher:
            voucher_serializer = VoucherSerializer(data=validated_data.get('voucher'))
            voucher_serializer.is_valid()
            task.voucher = voucher_serializer.save(task=task)
        return task








