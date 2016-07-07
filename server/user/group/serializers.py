from rest_framework import serializers

from .models import UserGroup

class UserGroupSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=32)
    permissions = serializers.DictField(
        source='_permissions',
        child=serializers.ListField(
            child=serializers.CharField(max_length=64)
        )
    )

    def validate_name(self, name):
        try:
            UserGroup.objects.get(pk=name)
        except UserGroup.DoesNotExist:
            raise serializers.ValidationError('No user group named \'{0}\''.format(name))
        return name
