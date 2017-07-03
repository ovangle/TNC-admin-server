from rest_framework import serializers
from .task.serializers import TaskSerializer
from .voucher.serializers import VoucherSerializer

class ActivitySerializer(serializers.Serializer):
    """
    Serializes a generic activity.

    An activity is any model with a unique foreign key 
    into the task model.

    The serializer is called with an instance of Task.
    """

    task = TaskSerializer(source='*')

    # only present if task.type === 'ISSUE_VOUCHER'
    voucher = VoucherSerializer(
        required=False, 
        source='get_voucher'
    )
