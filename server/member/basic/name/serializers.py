from rest_framework import serializers

from .models import Name

class NameSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=32)
    last_name = serializers.CharField(max_length=32)
    alias = serializers.CharField(max_length=32, required=False, allow_blank=True)

    def create(self, validated_data, role=None):
        role = role or validated_data.get('role')
        if role is None:
            raise ValueError('A \'role\' must be provided by the parent')
        return Name.objects.create(
            role=role,
            first_name=validated_data.pop('first_name'),
            last_name=validated_data.pop('last_name')
        )    

    def update(self, instance, validated_data):      
        if 'name_kind' in validated_data:
            raise ValueError('Cannot update the \'name_kind\' of a Name')
        instance.first_name = validated_data.get('first_name', instance.first_name) 
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.alias = validated_data.get('alias', instance.alias)
        return instance
