from rest_framework import serializers, validators
from ext.rest_framework.fields import EnumField

from member.basic.serializers import NameSerializer
from staff.models import StaffMember
from staff.staff_type import StaffType
from staff.serializers import StaffMemberSerializer

from .group.models import UserGroup
from .group.serializers import UserGroupSerializer
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True)
    username = serializers.CharField(
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(max_length=128, write_only=True, required=False)

    is_admin = serializers.BooleanField()

    groups = UserGroupSerializer(many=True)
    extra_permissions = serializers.DictField(
        source='_extra_permissions',
        child=serializers.ListField(
            child=serializers.CharField(max_length=64)
        )
    )

    staff_member = StaffMemberSerializer(source='staffmember')

    last_login = serializers.DateTimeField(required=False, read_only=True)

class CreateRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(max_length=128, read_only=True, source='_password')

    username = serializers.CharField(
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    groups = UserGroupSerializer(many=True)

    staff_type = EnumField(enum_type=StaffType, write_only=True)
    staff_name = NameSerializer(write_only=True)

    def create(self, validated_data):
        groups = [
            UserGroup.objects.get(pk=group_data['name']) 
            for group_data in validated_data.pop('groups')
        ]
        user =  User.objects.create(
            username=validated_data.pop('username'), 
            groups=groups
        )
        staff = StaffMember.objects.create(
            user=user,
            type=validated_data.pop('staff_type'),
            name=validated_data.pop('staff_name')
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


