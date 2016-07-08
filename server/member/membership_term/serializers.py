from rest_framework import serializers
from ext.rest_framework.fields import EnumField

from .term_type import MembershipTermType
from .models import MembershipTerm

class MembershipTermSerializer(serializers.Serializer):
    type = EnumField(enum_type=MembershipTermType)

    joined = serializers.DateTimeField()
    renewed = serializers.DateTimeField(allow_null=True)
    expires = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        if validated_data['renewed'] is not None:
            raise serializers.ValidationError('A joining member must have no renewal date')

        return MembershipTerm.objects.create(
            membership_type=validated_data['type'],
            joined=validated_data['joined'],
        )
