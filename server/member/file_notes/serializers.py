from rest_framework import serializers
from ext.rest_framework.fields import EnumField

from ..serializers import MemberSerializer
from staff.serializers import StaffMemberSerializer
from member.models import Member

from .models import MemberFileNote
from .severity import Severity

class MemberFileNoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    member_id = serializers.IntegerField()
    staff = StaffMemberSerializer(read_only=True)
    created = serializers.DateTimeField(read_only=True)

    message = serializers.CharField()
    pinned = serializers.BooleanField()

    severity = EnumField(enum_type=Severity)

    def validate_member_id(self, value):
        try: 
            Member.objects.get(pk=value)
        except Member.DoesNotExist:
            raise serializers.ValidationError('Member {0} does not exist'.format(member_id))
        return value

    def create(self, validated_data, staff=None):
        if staff is None:
            staff = validated_data.pop('staff', None)
        if staff is None: 
            raise ValueError('\'staff\' must be provided on create')
        return MemberFileNote.objects.create(
            member_id=validated_data.pop('member_id'),
            staff=staff, 
            message=validated_data.pop('message'),
            severity=validated_data.pop('severity')
        )

    def update(self, instance, validated_data):
        instance.severity = validated_data.pop('severity', instance.severity)
        instance.pinned = validated_data.pop('pinned', instance.pinned)
        instance.save()
        return instance




